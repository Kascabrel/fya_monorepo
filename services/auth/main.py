from fastapi import FastAPI
from api.routes import auth
from infrastructure.db.session import engine
from infrastructure.db.models import UserDB

app = FastAPI()

# Crée les tables à partir du modèle UserDB
UserDB.metadata.create_all(bind=engine)

app.include_router(auth.router, prefix="/auth")
