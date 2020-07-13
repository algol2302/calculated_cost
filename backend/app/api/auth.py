import os
from fastapi import Request
from fastapi_users import FastAPIUsers
from fastapi_users.authentication import JWTAuthentication
from fastapi_users.db import SQLAlchemyUserDatabase

from db.session import database
from schemas.user import User, UserCreate, UserUpdate, UserDB
from models.user import User as UserModel

SECRET = os.getenv('SECRET')

user_db = SQLAlchemyUserDatabase(UserDB, database, UserModel.__table__)


def on_after_register(user: UserDB, request: Request):
    print(f"User {user.id} has registered.")


def on_after_forgot_password(user: UserDB, token: str, request: Request):
    print(f"User {user.id} has forgot their password. Reset token: {token}")


jwt_authentication = JWTAuthentication(
    secret=SECRET,
    lifetime_seconds=3600,
    tokenUrl="/auth/jwt/login",
)

fastapi_users = FastAPIUsers(
    user_db, [jwt_authentication], User, UserCreate, UserUpdate, UserDB,
)
