from fya.auth.api.dto import RegisterRequest, LoginRequest, TokenResponse

def test_register_request():
    dto = RegisterRequest(username="bob", email="bob@example.com", password="123")
    assert dto.username == "bob"
    assert dto.email == "bob@example.com"

def test_token_response_defaults():
    res = TokenResponse(access_token="abc123")
    assert res.token_type == "Bearer"
