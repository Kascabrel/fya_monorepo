from pydantic import BaseModel
from typing import Optional

from services.auth_service.app.schemas.user import UserOut  # pour LoginResponse (facultatif mais pratique)


class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"


class TokenData(BaseModel):
    # Utilisé après décodage du token JWT
    sub: Optional[str] = None  # ex: user_id ou email
    exp: Optional[int] = None  # timestamp d’expiration (optionnel)


class RefreshTokenRequest(BaseModel):
    refresh_token: str


class RefreshTokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"


class LoginResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
    user: UserOut
