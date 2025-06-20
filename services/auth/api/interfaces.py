# The abstraction of the authentication service API.

class AuthService:
    def login(self, username: str, password: str) -> str:
        """Authenticate a user and return a token."""
        raise NotImplementedError("This method should be overridden by subclasses.")

    def logout(self, token: str) -> None:
        """Invalidate the user's session."""
        raise NotImplementedError("This method should be overridden by subclasses.")

    def register(self, username: str, password: str) -> None:
        """Register a new user."""
        raise NotImplementedError("This method should be overridden by subclasses.")

    def reset_password(self, username: str, new_password: str) -> None:
        """Reset the user's password."""
        raise NotImplementedError("This method should be overridden by subclasses.")
