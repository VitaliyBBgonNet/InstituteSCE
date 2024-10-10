from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
import uuid
from app.db import Base

class Detail(Base):
    __tablename__ = 'details'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    name = Column(String, nullable=False)  # Наименование

    type_id = Column(Integer, ForeignKey('types.id'), nullable=True)  # Тип
    type = relationship("Type")

    status_id = Column(Integer, ForeignKey('statuses.id'), nullable=True)  # Состояние
    status = relationship("Status")

    project_id = Column(Integer, ForeignKey('projects.id'), nullable=True)  # Проект
    project = relationship("Project")

    department_id = Column(Integer, ForeignKey('departments.id'), nullable=True)  # Подразделение
    department = relationship("Department")

    users = Column(String,nullable=True)

    data = Column(DateTime, nullable=True)
    note = Column(String, nullable=True)

    def __repr__(self):
        return f"<Detail(id={self.id}, name={self.name}, type_id={self.type_id}, status_id={self.status_id})>"
