from contextlib import asynccontextmanager

from fastapi import FastAPI

from api.auth_endpoints import router
from db import Base, engine


@asynccontextmanager
async def lifespan(app: FastAPI):
    # 💡create the table by start
    Base.metadata.create_all(bind=engine)
    yield  # server start here


app = FastAPI(title="Authservice", lifespan=lifespan)

app.include_router(router)
