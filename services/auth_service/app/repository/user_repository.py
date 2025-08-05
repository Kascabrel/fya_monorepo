from sqlalchemy.orm import Session

from app.core.security import get_password_hash, verify_password
from app.db.models.user import User
from app.schemas.user import UserCreate


# Récupérer un utilisateur par email
def get_by_email(db: Session, email: str) -> User | None:
    return db.query(User).filter(User.email == email).first()


# Créer un utilisateur (registre)
def create_user(db: Session, user_create: UserCreate) -> User:
    hashed_password = get_password_hash(user_create.password)
    user = User(
        email=str(user_create.email),
        hashed_password=hashed_password,
        is_active=True
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


# Authentifier un utilisateur (login)
def authenticate_user(db: Session, email: str, password: str) -> User | None:
    user = get_by_email(db, email)
    if not user:
        return None
    if not verify_password(password, user.hashed_password):
        return None
    return user


# Activer un utilisateur
def activate_user(db: Session, user: User) -> User:
    user.is_active = True
    db.commit()
    db.refresh(user)
    return user


# Désactiver un utilisateur
def deactivate_user(db: Session, user: User) -> User:
    user.is_active = False
    db.commit()
    db.refresh(user)
    return user


# Supprimer un utilisateur
def delete_user(db: Session, user: User):
    db.delete(user)
    db.commit()
