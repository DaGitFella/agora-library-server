from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from agora_library_server.db.session import get_db
from agora_library_server.schemas.user import UserCreate, UserList, UserPublic
from agora_library_server.services import user_service

user_router = APIRouter()


@user_router.get('', response_model=UserList)
def get_all_users(db: Session = Depends(get_db)):
    return user_service.get_all_users(db)


@user_router.get('/{id}', response_model=UserPublic)
def get_user(id: int, db: Session = Depends(get_db)):
    return user_service.get_user(id, db)


@user_router.post('/', response_model=UserPublic)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    return user_service.create_user(user, db)
