from app.database import Session
from app.models import User, Habit, Category
from datetime import date

def create_user(name):
    session = Session()
    user = User(name=name)
    session.add(user)
    session.commit()
    session.close()

def create_habit(user_id, name, frequency, category_name):
    session = Session()

    category = session.query(Category).filter_by(name=category_name).first()
    if not category:
        category = Category(name=category_name)
        session.add(category)
        session.commit()

    habit = Habit(
        name=name,
        frequency=frequency,
        start_date=date.today(),
        user_id=user_id,
        category_id=category.id
    )

    session.add(habit)
    session.commit()
    session.close()
