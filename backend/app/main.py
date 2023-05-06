from fastapi import FastAPI
from app import models
from app.routers import api_router
from app.database import engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(api_router, prefix="/api")
