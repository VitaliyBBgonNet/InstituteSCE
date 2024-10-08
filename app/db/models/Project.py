from sqlalchemy import Column, Integer, String
from app.db import Base

class Project(Base):
    __tablename__ = 'projects'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)

    def __repr__(self):
        return f"<Project(id={self.id}, name={self.name})>"
