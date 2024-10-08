from sqlalchemy import Column, Integer, String
from app.db import Base

class Department(Base):
    __tablename__ = 'departments'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)

    def __repr__(self):
        return f"<Department(id={self.id}, name={self.name})>"
