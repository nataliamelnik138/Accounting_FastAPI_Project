# Accounting_FastAPI_Project ()

Данный проект является  веб-приложением с API интерфейсом. Проект дает возможность бухгалтеру регистрировать в системе новых пользователей (логин, пароль) с указанием общей информации о пользователе (ФИО, телефоном, фотография, должность) и устанавливать им З/П.
Каждый работник, получивший логин/пароль от бухгалтера, имеет возможность авторизоваться в системе. 
Каждый пользователь, авторизованный в системе, должен имеет возможность просмотреть список пользователей и общую информацию о них (ФИО, телефон, фотография, должность) и дополнительно информацию о своей (только своей) З/П. 
Информация о З/П всех пользователей доступна только бухгалтеру.
#
[![Python](https://img.shields.io/badge/-Python-464646?style=flat-square&logo=Python)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/-FastAPI-464646?style=flat-square&logo=FastAPI)](https://fastapi.tiangolo.com/ru/)
[![PostgreSQL](https://img.shields.io/badge/-PostgreSQL-464646?style=flat-square&logo=PostgreSQL)](https://www.postgresql.org/)

### Технологии:
- Python 3.11
- FastAPI
- Alembic
- PostgreSQL
- Asyncpg
- Pytest


### Инструкция по развертыванию проекта:

Клонирование проекта:
```
git clone https://github.com/nataliamelnik138/Accounting_FastAPI_Project
```
Запуск:
1. Создайте виртуальное окружение
```
python -m venv venv
```
2. Активируйте виртуальное окружение
```
venv/Skripts/activate
```
4. Установите зависимости
```
pip install -r requirements.txt
```
6. Создайте в папке проекта файл .env, который должен содержать значение переменных из файла .env.sample
7. Примените миграции
```
alembic upgrade head
```
6. Запустите проект
```
uvicorn src.main:app --reload
```
7. Создайте суперпользователя (бухгалтера), запустив файл src/command.py

### Документация 
http://127.0.0.1:8000/docs

#### Автор проекта: Мельник Наталья
