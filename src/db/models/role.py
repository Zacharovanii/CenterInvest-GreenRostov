from enum import Enum
from sqlalchemy import String, Integer
from sqlalchemy.orm import Mapped, mapped_column
from src.db.base_class import Base


class Role_enum(Enum):
    user = "user"
    organizer = "organizer"
    admin = "admin"


class Role(Base):
    id: Mapped[int] = mapped_column(Integer, primary_key=True, nullable=False)
    role_name: Mapped[str] = mapped_column(String(length=320), nullable=False)
