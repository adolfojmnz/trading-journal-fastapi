from fastapi import APIRouter

from app.api.endpoints import trades, assets, users


api_router = APIRouter()
api_router.include_router(users.router, prefix="/users", tags=["users"])
api_router.include_router(assets.router, prefix="/assets", tags=["assets"])
api_router.include_router(trades.router, prefix="/trades", tags=["trades"])