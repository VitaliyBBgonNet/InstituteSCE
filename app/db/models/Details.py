from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
import uuid
from app.db import Base


class Detail(Base):
    __tablename__ = 'details'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    name = Column(String, nullable=False)  # Наименование

    type_id = Column(Integer, ForeignKey('types.id'), nullable=False)  # Тип
    type = relationship("Type")

    status_id = Column(Integer, ForeignKey('statuses.id'), nullable=False)  # Состояние
    status = relationship("Status")

    project_id = Column(Integer, ForeignKey('projects.id'), nullable=False)  # Проект
    project = relationship("Project")

    department_id = Column(Integer, ForeignKey('departments.id'), nullable=False)  # Подразделение
    department = relationship("Department")

    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)  # Пользователи
    user = relationship("User")

    data = Column(DateTime, nullable=False)  # Дата
    note = Column(String, nullable=True)  # Примечание

    def __repr__(self):
        return f"<Detail(id={self.id}, name={self.name}, type_id={self.type_id}, status_id={self.status_id})>"
