from fastapi import APIRouter
from app.api.routes.base import base_router
from app.api.routes.public import public_router


root = APIRouter()
root.include_router(base_router)
root.include_router(public_router, prefix="/api")
