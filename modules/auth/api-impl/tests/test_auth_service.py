# tests/test_auth_api_impl.py
from fya_auth_api_impl.auth.api.impl import AuthApiImpl
from fya.auth.api.dto import RegisterRequest, LoginRequest

def test_register():
    api = AuthApiImpl()
    req = RegisterRequest(username="john", email="steve@example.com", password="pwd123")
    user = api.register(req)
    assert user.email == "steve@example.com"
    assert user.id == "user-1"

def test_login():
    api = AuthApiImpl()
    req = LoginRequest(email="steve@example.com", password="pwd123")
    token = api.login(req)
    assert token == "fake-jwt-token"
