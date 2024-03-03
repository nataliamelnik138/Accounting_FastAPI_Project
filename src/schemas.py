from typing import Optional

from fastapi_users import schemas
from pydantic import BaseModel


class UserRead(schemas.BaseUser[int]):
    id: int
    username: str
    email: str
    full_name: str
    phone: str
    photo: str
    position: str
    salary: float
    role_id: int

    class Config:
        orm_mode = True


class UserCreate(schemas.BaseUserCreate):
    username: str
    email: str
    password: str
    full_name: Optional[str] = "null"
    phone: Optional[str] = "null"
    photo: Optional[str] = "null"
    position: Optional[str] = "null"
    role_id: Optional[int] = 1
    salary: Optional[int] = 0
    is_active: Optional[bool] = True
    is_superuser: Optional[bool] = False
    is_verified: Optional[bool] = False


class UserUpdate(schemas.BaseUserUpdate):
    password: Optional[str] = None
    email: Optional[str] = None
    photo: Optional[str] = None


class UserS(BaseModel):
    full_name: str
    phone: str
    photo: str
    position: str
