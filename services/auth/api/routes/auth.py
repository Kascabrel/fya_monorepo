from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from core.models.loging import TokenResponse, LoginRequest
from infrastructure.db.dependency import get_db
from infrastructure.repositories.sql_user_repository import SQLUserRepository
from services.auth_service import ImplAuthService

router = APIRouter()


@router.post("/login", response_model=TokenResponse)
def login(request: LoginRequest, db: Session = Depends(get_db)):
    user_repo = SQLUserRepository(db)
    auth_service = ImplAuthService(user_repo)

    try:
        token = auth_service.login(request.email, request.password)
        return TokenResponse(token=token, message="Login successful")
    except ValueError as e:
        raise HTTPException(status_code=401, detail=str(e))
