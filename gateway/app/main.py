from fastapi import FastAPI

from app.api.routes.auth import router

gateway_app = FastAPI(title="Gateway_app")
gateway_app.include_router(router)