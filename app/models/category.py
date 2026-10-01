from typing import TYPE_CHECKING
from sqlalchemy import String
from app.models import db


if TYPE_CHECKING:
    from app.models.questions import Question

class Category(db.Model):
    __tablename__ = "categories"

    id: db.Mapped[int] = db.mapped_column(primary_key=True)
    name: db.Mapped[str] = db.mapped_column(String(100), nullable=False, unique=True)
    questions: db.Mapped[list["Question"]] = db.relationship(back_populates="category")

    def __repr__(self):
        return f"<Category {self.id}: {self.name}>"