from fya.auth.api.interfaces import AuthApi
from fya.auth.api.dto import RegisterRequest, LoginRequest, UserDTO
from fya.auth.api.events import UserRegisteredEvent
from fya.auth.api.utils.json import to_json

class AuthApiImpl(AuthApi):
    def register(self, dto: RegisterRequest) -> UserDTO:
        # Dummy logic: simply returns a user with a static ID
        print(f"Received registration: {dto.email}")
        user = UserDTO(id="user-1", email=dto.email)

        # Emit registration event
        event = UserRegisteredEvent(
            user_id=user.id,
            email=user.email
        )
        print(f"Publishing event: {to_json(event)}")

        return user

    def login(self, dto: LoginRequest) -> str:
        # Dummy logic: always returns a fake JWT
        print(f"Login requested for {dto.email}")
        return "fake-jwt-token"
