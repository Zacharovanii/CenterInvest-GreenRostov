from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Integer, DateTime, ARRAY
from sqlalchemy.ext.mutable import MutableList
from src.db.base_class import Base
from datetime import datetime


class Event(Base):
    id: Mapped[int] = mapped_column(Integer, primary_key=True, nullable=False)

    title: Mapped[str] = mapped_column(String(length=120), nullable=False)
    description: Mapped[str] = mapped_column(String(length=320), nullable=False)
    
    date: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, nullable=False)
    performers: Mapped[list[int]] = mapped_column(MutableList.as_mutable(ARRAY(Integer)), nullable=False)