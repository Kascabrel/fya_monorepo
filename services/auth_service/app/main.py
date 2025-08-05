from fastapi import FastAPI

from api.auth_endpoints import router

app = FastAPI(title="Authservice")

app.include_router(router)
