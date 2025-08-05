from fastapi import APIRouter
from fastapi.security import OAuth2PasswordBearer

router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


@router.post("/home")
def hello_world():
    return {"hello": "world"}
