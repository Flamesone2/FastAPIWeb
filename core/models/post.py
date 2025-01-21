from .base import Base
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship,
)
from sqlalchemy import String, Text, ForeignKey
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .user import User


class Post(Base):
    title: Mapped[str] = mapped_column(
        String(100),
        unique=False,
    )
    body: Mapped[str] = mapped_column(
        Text,
        default="",
        server_default="",
    )
    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id"),
    )
    user: Mapped[User] = relationship(back_populates="posts")
