from services.auth.core.models.user import User
from services.auth.infrastructure.db.models import UserDB


def userdb_to_user(user_db: UserDB) -> User:
    return User(
        id=user_db.id,
        email=user_db.email,
        hashed_password=user_db.password_hash,
        role=user_db.role
    )