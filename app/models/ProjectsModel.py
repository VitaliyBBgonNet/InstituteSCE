# app/models/user.py
from sqlalchemy import Column, Integer, String, UUID
from app.db.session import Base


class Projects(Base):
    __tablename__ = 'projects'

    id = Column(Integer, primary_key=True, index=True)
    projectsName = Column(String, unique=True, nullable=False)
