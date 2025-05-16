from agora_library_server.crud.user import create_user, get_user_by_username
from sqlalchemy.orm import Session
from fastapi import HTTPException
from http import HTTPStatus
from agora_library_server.schemas.user import UserCreate

def register_user( user: UserCreate, db: Session):
    if get_user_by_username(user.username, db) is not None:
        raise HTTPException(status_code=HTTPStatus.BAD_REQUEST, detail="username already exists")
    new_user = create_user(db, user)
    return new_user
