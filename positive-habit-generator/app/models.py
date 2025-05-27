from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import relationship
from app.database import Base

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    habits = relationship("Habit", back_populates="user")

class Category(Base):
    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    habits = relationship("Habit", back_populates="category")

class Habit(Base):
    __tablename__ = 'habits'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    frequency = Column(String)
    start_date = Column(Date)

    user_id = Column(Integer, ForeignKey('users.id'))
    category_id = Column(Integer, ForeignKey('categories.id'))

    user = relationship("User", back_populates="habits")
    category = relationship("Category", back_populates="habits")
