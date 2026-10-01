from app import create_app
from app.models import Category, Question, db

app = create_app()

with app.app_context():
    cat = db.session.scalar(db.select(Category).where(Category.name == "Python"))
    if cat is None:
        cat = Category(name="Python")
        db.session.add(cat)
        db.session.commit()

    q = db.session.get(Question, 1)
    q.category = cat
    db.session.commit()

    print(q.category_id, q.category)   # 1 <Category 1: Python>
    print(cat.questions)