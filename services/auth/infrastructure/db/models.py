from sqlalchemy import Column, String

from services.auth.infrastructure.db.session import Base


class UserDB(Base):
    __tablename__ = 'users'

    id = Column(String(36), primary_key=True, nullable=False)
    email = Column(String(120), unique=True, nullable=False)
    password_hash = Column(String(128), nullable=False)
    role = Column(String(120), nullable=False)

    def __repr__(self):
        return f"<UserDB(id={self.id}, email={self.email})>"

    def verify_password(self, password):
        from werkzeug.security import check_password_hash
        return check_password_hash(self.password_hash, password)
