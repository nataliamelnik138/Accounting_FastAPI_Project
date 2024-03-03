from fastapi_users.db import SQLAlchemyBaseUserTable
from sqlalchemy import JSON, Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import DeclarativeMeta, declarative_base

Base: DeclarativeMeta = declarative_base()


class Role(Base):
    """
    Модель данных для ролей в SQLAlchemy.
    Атрибуты:
        id (Column): Уникальный идентификатор роли
        name (Column): Название роли
        permissions (Column): JSON-объект, содержащий ролевые разрешения
    """

    __tablename__ = "role"

    id = Column(Integer, primary_key=True, doc="Уникальный идентификатор роли")
    name = Column(String, nullable=False, doc="Название роли")
    permissions = Column(
        JSON,
        doc="JSON-объект, содержащий ролевые разрешения"
    )


class User(SQLAlchemyBaseUserTable[int], Base):
    """
    Модель данных для пользователей в SQLAlchemy.

    Атрибуты:
        id (Column): Уникальный идентификатор пользователя
        email (Column): Email
        username (Column): Username
        full_name (Column): ФИО пользователя
        phone (Column): Номер телефона пользователя
        hashed_password (Column): Хэш пароля пользователя
        photo (Column): URL-адрес фотографии
        position (Column): Должность
        salary(Column): Заработная плата
        role_id (Column): Идентификатор связанной с пользователем роли
    """

    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True,
                doc="Уникальный идентификатор пользователя")
    email = Column(String(length=320), unique=True, index=True, nullable=False)
    username = Column(String, unique=True, index=True)
    full_name = Column(String, nullable=True, doc="ФИО пользователя")
    phone = Column(String, doc="Номер телефона пользователя", nullable=True)
    hashed_password = Column(
        String,
        nullable=False,
        doc="Хэш пароля пользователя"
    )
    photo = Column(String, doc="Фото", nullable=True)  # URL to the photo
    position = Column(String, doc="Должность", nullable=True)
    salary = Column(Integer, doc="Заработная плата", nullable=True)
    role_id = Column(
        Integer,
        ForeignKey(Role.id, ondelete="CASCADE"),
        doc="Идентификатор связанной с пользователем роли"
    )
    is_active = Column(Boolean, default=True, nullable=False)
    is_superuser = Column(Boolean, default=False, nullable=False)
    is_verified = Column(Boolean, default=False, nullable=False)
