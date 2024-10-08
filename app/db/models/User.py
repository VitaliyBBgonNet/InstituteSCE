
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    full_name = Column(String, nullable=False)  # ФИО

    def __repr__(self):
        return f"<User(id={self.id}, full_name={self.full_name})>"