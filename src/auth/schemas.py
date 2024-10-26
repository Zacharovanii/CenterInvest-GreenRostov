from typing import Optional
from fastapi_users import schemas
from pydantic import EmailStr
from datetime import datetime


class UserRead(schemas.BaseUser[int]):
    id: int

    name: str
    lastname: str
    surname: str

    email: EmailStr
    phone_number: str

    level: int
    points: int
    achievements: list

    # is_active: bool = True
    # is_superuser: bool = False

    role_id: int
    registered_at: datetime

    class Config:
        orm_mode = True


class UserCreate(schemas.BaseUserCreate):
    name: str
    lastname: str
    surname: str

    phone_number: str
    email: EmailStr
    password: str

    role_id: int = 0
    level: int = 0
    points: int = 0

    achievements: list = None
    events: list = None

    registered_at: datetime = datetime.utcnow()

    is_active: Optional[bool] = True
    # is_superuser: Optional[bool] = False
    # is_verified: Optional[bool] = False

class UserResponse:
    def __init__(self, user):
        self.id = user.id
        self.name = user.name
        self.lastname = user.lastname
        self.surname = user.surname
        self.email = user.email
        self.phone_number = user.phone_number
        self.level = user.level
        self.points = user.points
        self.achievements = user.achievements
        self.role_id = user.role_id
        self.registered_at = user.registered_at
        self.is_active = user.is_active
        