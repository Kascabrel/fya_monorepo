# src/fya_auth_api_impl/auth/api/dto.py
from dataclasses import dataclass


@dataclass
class RegisterRequest:
    username: str
    email: str
    password: str


@dataclass
class LoginRequest:
    email: str
    password: str


@dataclass
class TokenResponse:
    access_token: str
    token_type: str = "Bearer"


@dataclass
class UserDTO:
    id: str
    email: str