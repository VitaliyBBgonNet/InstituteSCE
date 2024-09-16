# app/models/user.py
from sqlalchemy import Column, Integer, String, UUID
from app.db.session import Base

class Types(Base):
    __tablename__ = 'types'

    id = Column(Integer, primary_key=True, index=True)
    typeName = Column(String, unique=True, nullable=False)