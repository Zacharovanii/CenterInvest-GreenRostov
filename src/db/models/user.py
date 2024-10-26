from typing import Optional
from datetime import datetime
from fastapi_users.db import SQLAlchemyBaseUserTable
from sqlalchemy import ARRAY, TIMESTAMP, Boolean, ForeignKey, String, Integer
from sqlalchemy.orm import Mapped, mapped_column
from src.db.base_class import Base


class User(SQLAlchemyBaseUserTable[int], Base):
    id: Mapped[int] = mapped_column(Integer, primary_key=True, nullable=False)
    email: Mapped[str] = mapped_column(String(length=320), unique=True, index=True, nullable=False)
    
    hashed_password: Mapped[str] = mapped_column(String(length=1024), nullable=False)
    phone_number: Mapped[str] = mapped_column(String(length=20), unique=True, index=True, nullable=False)

    name: Mapped[str] = mapped_column(String(length=320), nullable=False)
    lastname: Mapped[str] = mapped_column(String(length=320), nullable=False)
    surname: Mapped[Optional[str]] = mapped_column(String(length=320))
    
    level: Mapped[int] = mapped_column(Integer)
    points: Mapped[int] = mapped_column(Integer)
    role_id: Mapped[int] = mapped_column(Integer)

    achievements: Mapped[Optional[list]] = mapped_column(ARRAY(Integer))
    events: Mapped[Optional[list]] = mapped_column(ARRAY(Integer))
    
    

    is_active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)
    is_superuser: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
    is_verified: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
    registered_at: Mapped[datetime] = mapped_column(TIMESTAMP, default=datetime.utcnow, nullable=False)
