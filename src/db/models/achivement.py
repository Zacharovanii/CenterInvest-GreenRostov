from sqlalchemy import String, Integer
from sqlalchemy.orm import Mapped, mapped_column
from src.db.base_class import Base


class Achivement(Base):
    id: Mapped[int] = mapped_column(Integer, primary_key=True, nullable=False)
    name: Mapped[str] = mapped_column(String(length=320), nullable=False)