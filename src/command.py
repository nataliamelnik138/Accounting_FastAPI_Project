import asyncio
import contextlib

from fastapi_users.exceptions import UserAlreadyExists

from src.database import get_async_session, get_user_db
from src.manager import get_user_manager
from src.schemas import UserCreate

get_async_session_context = contextlib.asynccontextmanager(get_async_session)
get_user_db_context = contextlib.asynccontextmanager(get_user_db)
get_user_manager_context = contextlib.asynccontextmanager(get_user_manager)


async def create_user(username: str, email: str, password: str, full_name: str):
    try:
        async with get_async_session_context() as session:
            async with get_user_db_context(session) as user_db:
                async with get_user_manager_context(user_db) as user_manager:
                    user = await user_manager.create(
                        UserCreate(
                            username=username,
                            email=email,
                            password=password,
                            is_superuser=True,
                            role_id=2,
                            full_name=full_name
                        )
                    )
                    print(f"User created {user}")
    except UserAlreadyExists:
        print(f"User {email} already exists")

if __name__ == "__main__":
    asyncio.run(create_user("admin4", "admin4@mail.ru", "guinevere", "admin4"))
