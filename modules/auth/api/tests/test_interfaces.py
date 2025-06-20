import pytest
from fya.auth.api.interfaces import AuthApi

def test_auth_api_is_abstract():
    with pytest.raises(TypeError):
        AuthApi()  # Ne doit pas pouvoir être instanciée
