from typing import Optional
from fastapi import Depends, Request
from fastapi_users import BaseUserManager, IntegerIDMixin
from src.db.models.user import User
from src.auth.utils import get_user_db
from src.settings import settings


class UserManager(IntegerIDMixin, BaseUserManager[User, int]):
    reset_password_token_secret = settings.SECRET_MANAGER_USER

    async def on_after_register(self, user: User, request: Optional[Request] = None):
        pass#print(f"User with id: {user.id} has registered.")

async def get_user_manager(user_db=Depends(get_user_db)):
    yield UserManager(user_db)