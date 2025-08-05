from fastapi import FastAPI
from app.auth.api.routes import auth_routes
from app.auth.infrastructure.db.session import engine
from app.auth.infrastructure.db.models import UserDB

app = FastAPI()

# Crée les tables à partir du modèle UserDB
UserDB.metadata.create_all(bind=engine)

app.include_router(auth.router, prefix="/auth_service")
