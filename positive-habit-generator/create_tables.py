from app.database import Base, engine
from app.models import User, Category, Habit

Base.metadata.create_all(engine)
print("Tables created successfully!")
