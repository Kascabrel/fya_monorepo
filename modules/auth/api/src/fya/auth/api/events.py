# src/fya_auth_api_impl/auth/api/events.py
from dataclasses import dataclass
from datetime import datetime, timezone

@dataclass
class UserRegisteredEvent:
    user_id: str
    email: str
    created_at: datetime = datetime.now(timezone.utc)
@dataclass
class UserDeletedEvent:
    user_id: str
    deleted_at: datetime = datetime.now(timezone.utc)

@dataclass
class PasswordChangedEvent:
    user_id: str
    changed_at: datetime = datetime.now(timezone.utc)

@dataclass
class EmailChangedEvent:
    user_id: str
    old_email: str
    new_email: str
    changed_at: datetime = datetime.now(timezone.utc)

@dataclass
class UserLoggedInEvent:
    user_id: str
    login_time: datetime = datetime.now(timezone.utc)

@dataclass
class UserLoggedOutEvent:
    user_id: str
    logout_time: datetime = datetime.now(timezone.utc)

@dataclass
class LoginFailedEvent:
    email: str
    reason: str
    failed_at: datetime = datetime.now(timezone.utc)
