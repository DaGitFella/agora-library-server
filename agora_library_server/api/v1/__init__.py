from fastapi import APIRouter
from agora_library_server.api.v1.endpoints import user, token
api_router = APIRouter()
api_router.include_router(user.user_router, prefix="/users", tags=["users"])
api_router.include_router(token.token_router, prefix="/token", tags=["token"])
