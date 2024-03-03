from sqlalchemy import select

from src.database import async_session_maker
from src.models import User


class UserDAO:
    @classmethod
    async def find_all(cls, user: User):
        async with async_session_maker() as session:
            query = select(User)
            users = await session.execute(query)
            users_models = users.scalars().all()
            if user.is_superuser:
                return users_models
            else:
                result = []
                for user_model in users_models:
                    result.append({
                        "full_name": user_model.full_name,
                        "phone": user_model.phone,
                        "photo": user_model.photo,
                        "position": user_model.position
                    })
                return result
