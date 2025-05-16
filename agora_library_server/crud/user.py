from sqlalchemy.orm import Session

from agora_library_server.models.user import User
from agora_library_server.schemas.user import *


def get_user_by_username(username: str, db: Session):
    user = db.query(User).filter(User.username == username).first()
    return user

def create_user(db: Session, user: UserCreate):
    db_user = User(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_all(db: Session):
    return db.query(User).all()