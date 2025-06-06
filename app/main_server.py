from fastapi import FastAPI
from app.api import route_v1
from app.core.config import settings

app = FastAPI(title="FastAPI Restful服务")

app.include_router(route_v1.router, prefix="/api/v1")

@app.get("/")
def read_root() -> dict:
    return {"msg": "Welcome to FastAPI Platform!", "env": settings.APP_ENV}

@router.get("/resource/greeting/{name}")
def greeting_resource(name: str):
    return get_greeting(name)