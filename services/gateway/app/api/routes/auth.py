import httpx
from fastapi import Header
from fastapi import APIRouter, Request

router = APIRouter()

from shared.schemas.user import UserCreate, UserOut
from shared.schemas.token import (
    RefreshTokenRequest,
    RefreshTokenResponse,
    LoginResponse,
    TokenData,
)


@router.get("/home")
async def home():
    async with httpx.AsyncClient(base_url="http://auth-service:8000") as client:
        response = await client.get("/home")
        return response.json()


@router.post("/login", response_model=LoginResponse)
async def login(request: Request):
    async with httpx.AsyncClient(base_url="http://auth-service:8000") as client:
        response = await client.post("/auth/login", data=await request.form())
        return response.json()


@router.post("/register", response_model=UserOut)
async def register(user_create: UserCreate, request: Request):
    async with httpx.AsyncClient(base_url="http://auth-service:8000") as client:
        response = await client.post("/auth/register", json=await request.json())
        return response.json()


@router.post("/refresh-token", response_model=RefreshTokenResponse)
async def refresh_token(request: Request):
    async with httpx.AsyncClient(base_url="http://auth-service:8000") as client:
        response = await client.post("/auth/refresh-token", json=await request.json())
        return response.json()


@router.get("/me",  response_model=UserOut)
async def get_me(authorization: str = Header(...)):
    headers = {"Authorization": authorization}
    async with httpx.AsyncClient(base_url="http://auth-service:8000") as client:
        response = await client.get("/auth/me", headers=headers)
        return response.json()
