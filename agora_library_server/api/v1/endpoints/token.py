from datetime import timedelta
from http import HTTPStatus

from fastapi.security import OAuth2PasswordRequestForm

from agora_library_server.core.settings import config
from agora_library_server.schemas.token import Token
from agora_library_server.services import token_service
from fastapi import APIRouter, HTTPException, Depends

from agora_library_server.services.login_service import authenticate_user

token_router = APIRouter()

@token_router.post('', response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = await authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=HTTPStatus.UNAUTHORIZED,
            detail="Usuário ou senha incorretos",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=config.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = token_service.create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}
