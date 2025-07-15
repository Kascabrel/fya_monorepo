from typing import Optional
from sqlalchemy.orm import Session

from core.models.user import User
from core.repository.user_repository import UserRepository
from infrastructure.db.models import UserDB
from infrastructure.mappers.user_mapper import userdb_to_user


class SQLUserRepository(UserRepository):
    def __init__(self, db_session: Session):
        self.db_session = db_session

    def get_user_by_id(self, user_id: str) -> Optional[User]:
        user = self.db_session.query(UserDB).filter(UserDB.id == user_id).first()
        return userdb_to_user(user) if user else None

    def get_user_by_email(self, email: str) -> Optional[User]:
        user = self.db_session.query(UserDB).filter(UserDB.email == email).first()
        return userdb_to_user(user) if user else None

    def create_user(self, user_data: dict) -> Optional[User]:
        if self.get_user_by_email(user_data['email']):
            return None
        new_user = UserDB(**user_data)
        self.db_session.add(new_user)
        self.db_session.commit()
        return userdb_to_user(new_user)

    def update_user(self, user_id: str, user_data: dict) -> Optional[User]:
        user = self.db_session.query(UserDB).filter(UserDB.id == user_id).first()
        if not user:
            return None
        for key, value in user_data.items():
            setattr(user, key, value)
        self.db_session.commit()
        return userdb_to_user(user)


    def delete_user(self, user_id: str) -> bool:
        user = self.db_session.query(UserDB).filter(UserDB.id == user_id).first()
        if not user:
            return False
        self.db_session.delete(user)
        self.db_session.commit()
        return True

    def verify_password(self, user_id: str, password: str) -> bool:
        user = self.get_user_by_id(user_id)
        if not user:
            return False
        user_db = UserDB(id=user.id, email=user.email, password_hash=user.hashed_password, role=user.role)
        return user_db.verify_password(password)