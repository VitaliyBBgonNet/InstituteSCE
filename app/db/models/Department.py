from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.db import Base

class Department(Base):
    __tablename__ = 'departments'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)

    department = relationship(
        "Detail",
        back_populates="department",
        cascade="all, delete",
        passive_deletes=True
    )

    def __repr__(self):
        return f"<Department(id={self.id}, name={self.name})>"
