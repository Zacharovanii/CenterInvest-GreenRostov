from typing import Optional
from fastapi_users import schemas
from pydantic import EmailStr

class UserRead(schemas.BaseUser[int]):
    id: int
    name: str
    email: EmailStr
    level: int
    is_active: bool = True
    is_superuser: bool = False
    role_id: int

    class Config:
        orm_mode = True

class UserCreate(schemas.BaseUserCreate):
    name: str
    lastname: str
    surname: str

    email: EmailStr
    hashed_password: str
    role_id: int

    level: Optional[int]
    points: Optional[int]
    achievements: Optional[list]

    is_active: Optional[bool] = True
    is_superuser: Optional[bool] = False
    is_verified: Optional[bool] = False