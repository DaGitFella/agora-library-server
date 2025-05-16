from http import HTTPStatus
from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from agora_library_server.crud.user import get_all
from agora_library_server.db.session import get_db
from agora_library_server.schemas.user import UserCreate, UserPublic
from agora_library_server.services import user_service

user_router = APIRouter()


@user_router.get('/')
def get_all_users(db: Session = Depends(get_db)):
    return get_all(db)


@user_router.get('/{id}', response_model=UserPublic)
def get_user(id: int, db: Session = Depends(get_db)):
    return user_service.get_user(id, db)


@user_router.post('/', response_model=UserPublic, status_code=HTTPStatus.CREATED)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    return user_service.register_user(user, db)
