# app/models/user.py
from sqlalchemy import Column, Integer, String, UUID
from app.db.session import Base


class Status(Base):
    __tablename__ = 'status'

    id = Column(Integer, primary_key=True, index=True)
    statusName = Column(String, unique=True, nullable=False)
