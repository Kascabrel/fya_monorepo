# src/fya_auth_api_impl/auth/api/interfaces.py
from abc import ABC, abstractmethod
from .dto import LoginRequest, RegisterRequest, TokenResponse

class AuthApi(ABC):
    @abstractmethod
    def register(self, request: RegisterRequest) -> TokenResponse:
        pass

    @abstractmethod
    def login(self, request: LoginRequest) -> TokenResponse:
        pass
