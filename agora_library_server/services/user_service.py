from jose import jwt, JWTError

from agora_library_server.core.settings import config
from agora_library_server.crud.user import create_user, get_user_by_username
from sqlalchemy.orm import Session
from fastapi import HTTPException, Depends
from http import HTTPStatus

from agora_library_server.db.session import get_db
from agora_library_server.models.user import User
from agora_library_server.schemas.user import UserCreate, UserPublic
from agora_library_server.schemas.token import TokenData
from agora_library_server.core.security import pwd_context, oauth2_scheme

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password):
    return pwd_context.hash(password)

async def get_current_user(
    db: Session = Depends(get_db),
    token: str = Depends(oauth2_scheme)
) -> User:
    credentials_exception = HTTPException(
        status_code=HTTPStatus.UNAUTHORIZED,
        detail="Não foi possível validar as credenciais",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, config.SECRET_KEY, algorithms=[config.ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        user = get_user_by_username(username=username, db=db)
        if user is None:
            raise credentials_exception
        return user
    except JWTError:
        raise credentials_exception
