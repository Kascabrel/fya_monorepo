from dataclasses import dataclass

from services.auth.infrastructure.db.models.db_user import UserDB


@dataclass
class User:
    id: str
    email: str
    hashed_password: str
    role: str

