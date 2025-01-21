from sqlalchemy import ForeignKey
from sqlalchemy.orm import (
    declared_attr,
    mapped_column,
    Mapped,
    relationship,
)


class UserRelationMixin:

    user_id: Mapped[int] = mapped_column(
        ForeignKey("users_table.id")
    )

    @declared_attr
    def user(self):
        return relationship("User")

    @declared_attr
    def user_id(self):
        return
