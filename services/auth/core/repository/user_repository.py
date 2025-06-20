from abc import ABC, abstractmethod
from typing import Optional

from services.auth.core.models.user import User


class UserRepository(ABC):
    @abstractmethod
    def get_user_by_id(self, user_id: str) -> Optional[User]:
        """
        Retrieves a user by their ID.

        :param user_id: The unique identifier of the user.
        :return: User object or None if not found.
        """
        raise NotImplementedError("This method should be overridden by subclasses.")

    @abstractmethod
    def get_user_by_email(self, email: str) -> Optional[User]:
        """
        Retrieves a user by their email address.

        :param email: The email address of the user.
        :return: User object or None if not found.
        """
        raise NotImplementedError("This method should be overridden by subclasses.")

    @abstractmethod
    def create_user(self, user_data: dict) -> User:
        """
        Creates a new user with the provided data.

        :param user_data: A dictionary containing user information.
        :return: The created User object.
        """
        raise NotImplementedError("This method should be overridden by subclasses.")

    @abstractmethod
    def update_user(self, user_id: str, user_data: dict) -> User:
        """
        Updates an existing user with the provided data.

        :param user_id: The unique identifier of the user to update.
        :param user_data: A dictionary containing updated user information.
        :return: The updated User object.
        """
        raise NotImplementedError("This method should be overridden by subclasses.")

    @abstractmethod
    def delete_user(self, user_id: str) -> bool:
        """
        Deletes a user by their ID.

        :param user_id: The unique identifier of the user to delete.
        :return: True if deletion was successful, False otherwise.
        """
        raise NotImplementedError("This method should be overridden by subclasses.")