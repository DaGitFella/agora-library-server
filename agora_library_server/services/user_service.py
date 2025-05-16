from agora_library_server.crud.user import create_user, get_user_by_username
from sqlalchemy.orm import Session
from fastapi import HTTPException

from agora_library_server.schemas.user import UserCreate

def register_user(db: Session, user: UserCreate):
    if get_user_by_username(db, user.username) is not None:
        raise HTTPException(status_code=400, detail="username already exists")
    new_user = create_user(db, user)
    return new_user
