from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.db import Base

class Type(Base):
    __tablename__ = 'types'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)

    details = relationship(
        "Detail",
        back_populates="type",
        cascade="all, delete",
        passive_deletes=True
    )

    def __repr__(self):
        return f"<Type(id={self.id}, name={self.name})>"