from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from agora_library_server.crud.user import get_user_by_username
from agora_library_server.db.session import get_db
from agora_library_server.models.user import User
from agora_library_server.schemas.user import UserPublic, UserCreate
from agora_library_server.services import user_service
from agora_library_server.services.user_service import get_password_hash

user_router = APIRouter()


@user_router.post("/register")
async def register_user(user: UserCreate, db: Session = Depends(get_db)):
    if get_user_by_username(user.username, db):
        raise HTTPException(status_code=400, detail="Usuário já existe")
    db_user = User(**user.dict())
    db_user.password = get_password_hash(user.password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return {"message": "Usuário criado com sucesso"}

@user_router.get("/me", response_model=UserPublic)
async def read_users_me(current_user: User = Depends(user_service.get_current_user)):
    return current_user
