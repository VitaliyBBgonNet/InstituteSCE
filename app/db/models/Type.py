from sqlalchemy import Column, Integer, String
from app.db import Base

class Type(Base):
    __tablename__ = 'types'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)

    def __repr__(self):
        return f"<Type(id={self.id}, name={self.name})>"