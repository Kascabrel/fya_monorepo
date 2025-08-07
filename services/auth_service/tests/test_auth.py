import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.api.auth_endpoints import get_db
from app.core.security import create_access_token
from app.db import Base
from shared.schemas.user import UserCreate

from app.repository.user_repository import create_user
from app.main import app

# Use SQLite for testing
SQLALCHEMY_DATABASE_URL = "sqlite:///./tests.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

# Create tests DB
Base.metadata.create_all(bind=engine)


# Dependency override
def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


# Override DB dependency in FastAPI app
app.dependency_overrides[get_db] = override_get_db  # type: ignore
client = TestClient(app)

# Sample tests user
TEST_USER = {
    "email": "tests@example.com",
    "password": "testpassword"
}


@pytest.fixture(autouse=True)
def setup_and_teardown():
    # Clear the DB before each tests
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)


def test_register_user():
    response = client.post("/auth/register", json=TEST_USER)
    assert response.status_code == 201
    assert response.json()["email"] == TEST_USER["email"]


def test_register_user_existing():
    # Register once
    client.post("/auth/register", json=TEST_USER)
    # Register again
    response = client.post("/auth/register", json=TEST_USER)
    assert response.status_code == 400
    assert response.json()["detail"] == "Email already registered"


def test_login_user():
    # Register
    client.post("/auth/register", json=TEST_USER)
    # Login
    response = client.post(
        "/auth/login",
        data={"username": TEST_USER["email"], "password": TEST_USER["password"]},
        headers={"Content-Type": "application/x-www-form-urlencoded"},
    )
    assert response.status_code == 200
    data = response.json()
    assert "access_token" in data
    assert data["user"]["email"] == TEST_USER["email"]


def test_login_user_invalid_password():
    client.post("/auth/register", json=TEST_USER)
    response = client.post(
        "/auth/login",
        data={"username": TEST_USER["email"], "password": "wrongpass"},
        headers={"Content-Type": "application/x-www-form-urlencoded"},
    )
    assert response.status_code == 401


def test_get_me():
    db = next(override_get_db())
    user = UserCreate(**TEST_USER)
    user_db = create_user(db, user)
    token = create_access_token({"sub": user.email})

    response = client.get(
        "/auth/me",
        headers={"Authorization": f"Bearer {token}"}
    )
    assert response.status_code == 200
    assert response.json()["email"] == user.email


def test_refresh_token():
    db = next(override_get_db())
    user = UserCreate(**TEST_USER)
    create_user(db, user)

    # Simuler un token d'actualisation avec le même access token
    token = create_access_token({"sub": user.email})
    response = client.post(
        "/auth/refresh-token",
        json={"refresh_token": token}
    )
    assert response.status_code == 200
    assert "access_token" in response.json()
