from services.auth.infrastructure.db import db


class UserDB(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.String(36), primary_key=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    role = db.Column(db.String(120), nullable=False)

    def __repr__(self):
        return f"<UserDB(id={self.id}, email={self.email})>"
