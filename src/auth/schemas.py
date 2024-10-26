from typing import Optional
from fastapi_users import schemas
from pydantic import EmailStr
from datetime import datetime
class UserRead(schemas.BaseUser[int]):
    id: int
    name: str
    email: EmailStr
    level: int
    is_active: bool = True
    is_superuser: bool = False
    role_id: int
    registered_at: datetime
    class Config:
        orm_mode = True

class UserCreate(schemas.BaseUserCreate):
    name: str
    lastname: str
    surname: str
    email: EmailStr
    password: str
    role_id: int = 1
    registered_at: datetime = datetime.utcnow()
    is_active: Optional[bool] = True
    is_superuser: Optional[bool] = False
    is_verified: Optional[bool] = False
