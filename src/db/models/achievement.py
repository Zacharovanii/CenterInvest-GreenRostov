from sqlalchemy import ARRAY, String, Integer
from sqlalchemy.orm import Mapped, mapped_column
from src.db.base_class import Base
from sqlalchemy.ext.mutable import MutableList


class Achievement(Base):
    id: Mapped[int] = mapped_column(Integer, primary_key=True, nullable=False)
    title: Mapped[str] = mapped_column(String(length=320), unique=True, nullable=False)
    description: Mapped[str] = mapped_column(String(length=320))
    owners: Mapped[list[int]] = mapped_column(MutableList.as_mutable(ARRAY(Integer)), default=[], nullable=False)