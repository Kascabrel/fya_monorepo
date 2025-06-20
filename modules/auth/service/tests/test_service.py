import pytest
from fya.auth.service.services.auth_service import AuthService
from fya.auth.api.dto import RegisterRequest, LoginRequest, TokenResponse


def test_register_returns_token_response():
    service = AuthService()
    request = RegisterRequest(username= "test user", email="test@example.com", password="123456")

    response = service.register(request)

    assert isinstance(response, TokenResponse)
    assert response.access_token == "dummy_token_from_register"
    assert response.token_type == "bearer"


def test_login_returns_token_response():
    service = AuthService()
    request = LoginRequest(email="test@example.com", password="123456")

    response = service.login(request)

    assert isinstance(response, TokenResponse)
    assert response.access_token == "dummy_token_from_login"
    assert response.token_type == "bearer"
