from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.api.auth_endpoints import router
from app.db import engine, Base


@asynccontextmanager
async def lifespan(app: FastAPI):
    # 💡create the table by start
    Base.metadata.create_all(bind=engine)
    yield  # server start her


app = FastAPI(title="Authservice", lifespan=lifespan)

app.include_router(router, prefix="/auth", tags=["auth"])
