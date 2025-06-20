from fya.auth.api.interfaces import AuthApi
from fya.auth.api.dto import RegisterRequest, LoginRequest, TokenResponse
from fya.auth.api.events import UserRegisteredEvent
from fya.auth.api.utils.json import to_json


class AuthService(AuthApi):
    def register(self, request: RegisterRequest) -> TokenResponse:
        # Dummy logic for user registration
        print(f"Registering user: {request.email}")

        # Create event
        event = UserRegisteredEvent(
            user_id="dummy-id",  # Replace with actual user ID later
            email=request.email
        )
        print(f"Publishing event: {to_json(event)}")

        return TokenResponse(
            access_token="dummy_token_from_register",
            token_type="bearer"
        )

    def login(self, request: LoginRequest) -> TokenResponse:
        # Dummy login logic
        print(f"Login attempt for: {request.email}")
        return TokenResponse(
            access_token="dummy_token_from_login",
            token_type="bearer"
        )
