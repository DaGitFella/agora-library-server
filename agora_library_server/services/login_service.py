from fastapi import HTTPException
from sqlalchemy.orm import Session

from agora_library_server.crud.user import get_user_by_username
from agora_library_server.services.user_service import verify_password


async def authenticate_user(db: Session, username: str):
    user = await get_user_by_username(db, username)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    if not verify_password(user.password, user.hashed_password):
        raise HTTPException(status_code=404, detail="Incorrect password")
    return user

