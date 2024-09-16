# app/models/user.py
from sqlalchemy import Column, Integer, String, UUID
from app.db.session import Base

class User(Base):
    __tablename__ = 'users'

    id = Column(UUID, primary_key=True, index=True)
    username = Column(String, unique=True, nullable=False)