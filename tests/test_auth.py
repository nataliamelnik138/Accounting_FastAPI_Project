from sqlalchemy import insert, select

from src.models import Role
from tests.conftest import async_session_maker, client


async def test_add_role():
    async with async_session_maker() as session:
        stat = insert(Role.__tablename__).values(
            id=1,
            name="admin",
            permissions=None
        )
        await session.execute(stat)
        await session.commit()

        query = select(Role.__tablename__)
        result = await session.execute(query)
        assert result.all() == [(1, "admin", None)], "Роль не добавилась"


def test_register():

    response = client.post("users/register", json={
        "email": "string",
        "is_active": True,
        "is_superuser": False,
        "is_verified": False,
        "username": "string",
        "full_name": "string",
        "phone": "string",
        "photo": "string",
        "position": "string",
        "salary": 0,
        "role_id": 0
    })

    assert response.status_code == 201
