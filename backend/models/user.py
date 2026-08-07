from sqlalchemy import Column, Integer, String
from database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)

    age = Column(Integer, nullable=True)
    occupation = Column(String, nullable=True)
    goals = Column(String, nullable=True)
    interests = Column(String, nullable=True)
    reading_style = Column(String, nullable=True)
    bio = Column(String, nullable=True)
    zodiac= Column(String, nullable=True)