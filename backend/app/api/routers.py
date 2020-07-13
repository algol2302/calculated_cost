from fastapi import APIRouter

from api import calculated_cost
from api.auth import (
    fastapi_users, jwt_authentication,
    on_after_register, on_after_forgot_password,
    SECRET
)

api_router = APIRouter()

# calculated_cost
api_router.include_router(calculated_cost.router, tags=["calculated_cost"])

# users
api_router.include_router(
    fastapi_users.get_auth_router(jwt_authentication),
    prefix="/auth/jwt", tags=["auth"]
)
api_router.include_router(
    fastapi_users.get_register_router(on_after_register),
    prefix="/auth", tags=["auth"]
)
api_router.include_router(
    fastapi_users.get_reset_password_router(
        SECRET, after_forgot_password=on_after_forgot_password
    ),
    prefix="/auth",
    tags=["auth"],
)
api_router.include_router(
    fastapi_users.get_users_router(), prefix="/users", tags=["users"]
)
