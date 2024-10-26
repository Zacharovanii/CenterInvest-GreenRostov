from fastapi_users import schemas
from pydantic import EmailStr
from datetime import datetime

class UserRead(schemas.BaseUser[int]):
    id: int
    name: str
    lastname: str
    surname: str
    email: EmailStr
    registered_at: datetime
    role_id: int
    level: int
    achievements: list
    is_active: bool = True
    is_superuser: bool = False
    is_verified: bool = False

    class Config:
        orm_mode = True

class UserCreate(schemas.BaseUserCreate):
    id: int
    name: str
    email: EmailStr
    password: str
    registered_at: datetime
    is_active: bool = True
    is_superuser: bool = False
    is_verified: bool = False
    
class UserResponse:
    def __init__(self, user):
        self.id = user.id
        self.name = user.name
        self.lastname = user.lastname
        self.surname = user.surname
        self.email = user.email
        self.registered_at = user.registered_at
        self.is_active = user.is_active
        self.is_superuser = user.is_superuser
        self.is_verified = user.is_verified
