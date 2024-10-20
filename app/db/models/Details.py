from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
import uuid
from app.db import Base

class Detail(Base):
    __tablename__ = 'details'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    name = Column(String, nullable=False)  # Наименование

    type_id = Column(Integer, ForeignKey('types.id', ondelete='SET NULL'), nullable=True)  # Тип
    type = relationship("Type", back_populates="details")

    status_id = Column(Integer, ForeignKey('statuses.id', ondelete='SET NULL'), nullable=True)  # Состояние
    status = relationship("Status", back_populates="status")

    project_id = Column(Integer, ForeignKey('projects.id', ondelete='SET NULL'), nullable=True)  # Проект
    project = relationship("Project", back_populates="project")

    department_id = Column(Integer, ForeignKey('departments.id', ondelete='SET NULL'), nullable=True)  # Подразделение
    department = relationship("Department", back_populates="department")

    users = Column(String,nullable=True)
    data = Column(DateTime, nullable=True)
    note = Column(String, nullable=True)

    def __repr__(self):
        return f"<Detail(id={self.id}, name={self.name}, type_id={self.type_id}, status_id={self.status_id})>"
