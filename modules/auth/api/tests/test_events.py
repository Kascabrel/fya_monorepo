# tests/test_events.py
from fya.auth.api.events import (
    UserRegisteredEvent, UserDeletedEvent, PasswordChangedEvent,
    EmailChangedEvent, UserLoggedInEvent, UserLoggedOutEvent,
    LoginFailedEvent
)
import re

def test_user_created_event():
    evt = UserRegisteredEvent(user_id="u1", email="a@b.com")
    assert evt.user_id == "u1"
    assert evt.email == "a@b.com"

def test_user_deleted_event():
    evt = UserDeletedEvent(user_id="u2")
    assert evt.user_id == "u2"

def test_password_changed_event():
    evt = PasswordChangedEvent(user_id="u3")
    assert evt.user_id == "u3"

def test_email_changed_event():
    evt = EmailChangedEvent(user_id="u4", old_email="old@x.com", new_email="new@x.com")
    assert evt.old_email == "old@x.com"
    assert evt.new_email == "new@x.com"

def test_user_logged_in_event():
    evt = UserLoggedInEvent(user_id="u5")
    assert evt.user_id == "u5"

def test_user_logged_out_event():
    evt = UserLoggedOutEvent(user_id="u6")
    assert evt.user_id == "u6"

def test_login_failed_event():
    evt = LoginFailedEvent(email="fail@me.com", reason="bad password")
    assert evt.reason == "bad password"
    assert re.match(r".+@.+\..+", evt.email)  # email format
