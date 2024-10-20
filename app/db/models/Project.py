from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.db import Base


class Project(Base):
    __tablename__ = 'projects'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)

    project = relationship(
        "Detail",
        back_populates="project",
        cascade="all, delete",
        passive_deletes=True
    )

    def __repr__(self):
        return f"<Project(id={self.id}, name={self.name})>"
