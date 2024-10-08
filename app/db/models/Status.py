from sqlalchemy import Column, Integer, String
from app.db import Base

class Status(Base):
    __tablename__ = 'statuses'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)

    def __repr__(self):
        return f"<Status(id={self.id}, name={self.name})>"
