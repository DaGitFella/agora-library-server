from pydantic import BaseModel, EmailStr


class UserCreate(BaseModel):
    id: int
    name: str
    username: str
    email: EmailStr
    password: str


class UserPublic(BaseModel):
    id: int
    name: str
    username: str
    email: EmailStr


class UserList(BaseModel):
    user: list[UserPublic]
