from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session

from db import sessionLocal

router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


def get_db():
    db = sessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/home")
def hello_world(db: Session = Depends(get_db)):
    return {"hello": "world"}
