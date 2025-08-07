from pydantic import BaseModel, EmailStr, Field, ConfigDict


class UserBase(BaseModel):
    email: EmailStr


class UserCreate(UserBase):
    password: str = Field(..., min_length=8)


class UserLogin(UserBase):
    password: str


from pydantic import BaseModel, ConfigDict


class UserOut(BaseModel):
    id: int
    email: str
    is_active: bool = True

    model_config = ConfigDict(from_attributes=True)


class UserInDB(UserBase):
    id: int
    hashed_password: str
    is_active: bool = True
