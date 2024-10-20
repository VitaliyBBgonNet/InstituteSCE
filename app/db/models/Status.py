from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.db import Base

class Status(Base):
    __tablename__ = 'statuses'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)

    status = relationship(
        "Detail",
        back_populates="status",
        cascade="all, delete",
        passive_deletes=True
    )

    def __repr__(self):
        return f"<Status(id={self.id}, name={self.name})>"
