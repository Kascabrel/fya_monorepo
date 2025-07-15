from api.interfaces import AuthService
from infrastructure.repositories.sql_user_repository import SQLUserRepository


class ImplAuthService(AuthService):
    def __init__(self, user_repo: SQLUserRepository):
        self.user_repo = user_repo

    def login(self, email: str, password: str) -> str:
        user = self.user_repo.get_user_by_email(email)
        if not user or not user.verify_password(password):
            raise ValueError("Invalid username or password")
        return user.generate_token()

    def logout(self, token: str) -> None:
        self.user_repo.invalidate_token(token)

    def register(self, username: str, password: str) -> None:
        if self.user_repo.get_user_by_username(username):
            raise ValueError("Username already exists")
        self.user_repo.create_user(username, password)

    def reset_password(self, username: str, new_password: str) -> None:
        user = self.user_repo.get_user_by_username(username)
        if not user:
            raise ValueError("User not found")
        user.set_password(new_password)
        self.user_repo.update_user(user)

