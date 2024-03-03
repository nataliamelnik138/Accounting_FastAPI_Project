from typing import Annotated
from fastapi import FastAPI, Depends
from fastapi_users import FastAPIUsers

from src.auth_config import auth_backend
from src.dao import UserDAO
from src.database import User
from src.manager import get_user_manager
from src.schemas import UserRead, UserCreate, UserUpdate, UserS

app = FastAPI(
    title="Accounting"
)

fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)

app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["auth"],
)

app.include_router(
    fastapi_users.get_register_router(UserRead, Annotated[UserCreate, Depends()]),
    prefix="/users",
    tags=["users"],
)

current_user = fastapi_users.current_user()
current_active_user = fastapi_users.current_user(active=True)


app.include_router(
    fastapi_users.get_users_router(UserRead, UserUpdate),
    prefix="/users",
    tags=["users"],
)


@app.get("/users_list", response_model=list[UserS])
async def get_users(user: User = Depends(current_active_user)):
    users = await UserDAO.find_all(user)
    return users
