# init_db.py
from app.database import Base, engine
from app.models import User, Category, Habit

def init_db():
    # Create all tables
    Base.metadata.create_all(bind=engine)
    print("Database tables created successfully!")

if __name__ == "__main__":
    init_db()