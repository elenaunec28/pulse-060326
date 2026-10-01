from typing import TYPE_CHECKING
from app.models import db

if TYPE_CHECKING:
    from app.models.answers import Answer
    from app.models.category import Category

class Question(db.Model):
    __tablename__ = 'questions'

    id: db.Mapped[int] = db.mapped_column(primary_key=True)
    text: db.Mapped[str] = db.mapped_column(db.String(255))

    answers: db.Mapped[list["Answer"]] = db.relationship(
        back_populates="question", cascade="all, delete-orphan"
    )

    category_id: db.Mapped[int | None] = db.mapped_column(
        db.ForeignKey("categories.id", ondelete="SET NULL"),
        index=True,
    )
    category: db.Mapped["Category | None"] = db.relationship(back_populates="questions")

    def __repr__(self):
        return f"<Question {self.id}: {self.text}>"


