from sqlalchemy import Boolean, String, Integer
from sqlalchemy.orm import Mapped, mapped_column
from src.db.base_class import Base


class Role(Base):
    id: Mapped[int] = mapped_column(Integer, primary_key=True, nullable=False)
    role_name: Mapped[str] = mapped_column(String(length=320), nullable=False)

    events_management: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)
    events_parttake: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)
    roles_edit: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
    users_block: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
