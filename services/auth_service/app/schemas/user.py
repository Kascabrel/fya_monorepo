from pydantic import BaseModel, EmailStr, Field
from typing import Optional


class UserBase(BaseModel):
    email: EmailStr


class UserCreate(UserBase):
    password: str = Field(..., min_length=8)


class UserLogin(UserBase):
    password: str


class UserOut(UserBase):
    id: int
    is_active: bool = True

    class Config:
        orm_mode = True


class UserInDB(UserBase):
    id: int
    hashed_password: str
    is_active: bool = True


