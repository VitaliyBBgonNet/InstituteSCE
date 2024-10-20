from PySide6.QtWidgets import QApplication, QMainWindow
from app.views.AddElement import AddElement
from app.db.models.Details import Detail
from app.db.models.Type import Type
from app.db.models.Status import Status
from app.db.models.Project import Project
from app.db.models.Department import Department
from app.db import SessionLocal
from datetime import datetime


class AddElementController(QMainWindow):
    def __init__(self, parent=None):
        super(AddElementController, self).__init__(parent)
        self.addAddElementInterface = AddElement()
        self.addAddElementInterface.setupUi(self)
        self.addAddElementInterface.dateTimeEdit.setDate(datetime.now())
        self.clearAllBeforeLoadUI()
        self.checkDatabase()
        self.addAddElementInterface.PB_Add_ELEMENT_2.clicked.connect(self.addElement)

    def checkDatabase(self):
        db_session = SessionLocal()

        types = db_session.query(Type).all()
        states = db_session.query(Status).all()
        projects = db_session.query(Project).all()
        departments = db_session.query(Department).all()

        for temp in types:
            self.addAddElementInterface.Box_Type.addItem(temp.name)

        for temp in states:
            self.addAddElementInterface.Box_Status.addItem(temp.name)

        for temp in projects:
            self.addAddElementInterface.Box_Project_Name.addItem(temp.name)

        for temp in departments:
            self.addAddElementInterface.Box_Name_Subdivade.addItem(temp.name)

    def clearAllBeforeLoadUI(self):
        self.addAddElementInterface.Box_Type.clear()
        self.addAddElementInterface.Box_Status.clear()
        self.addAddElementInterface.Box_Project_Name.clear()
        self.addAddElementInterface.Box_Name_Subdivade.clear()

    def addElement(self):
        db_session = SessionLocal()

        # Извлекаем текущие типы, статусы, проекты и подразделения
        existing_types = {t.name: t for t in db_session.query(Type).all()}
        existing_statuses = {s.name: s for s in db_session.query(Status).all()}
        existing_projects = {p.name: p for p in db_session.query(Project).all()}
        existing_departments = {d.name: d for d in db_session.query(Department).all()}

        # Получаем выбранные значения из интерфейса
        type_name = self.addAddElementInterface.Box_Type.currentText()
        status_name = self.addAddElementInterface.Box_Status.currentText()
        project_name = self.addAddElementInterface.Box_Project_Name.currentText()
        department_name = self.addAddElementInterface.Box_Name_Subdivade.currentText()

        # Проверяем существование типа
        if type_name not in existing_types:
            raise ValueError(f"Тип '{type_name}' не существует в базе данных. Пожалуйста, добавьте его.")

        # Проверяем существование статуса
        if status_name not in existing_statuses:
            raise ValueError(f"Статус '{status_name}' не существует в базе данных. Пожалуйста, добавьте его.")

        # Проверяем существование проекта
        if project_name not in existing_projects:
            raise ValueError(f"Проект '{project_name}' не существует в базе данных. Пожалуйста, добавьте его.")

        # Проверяем существование подразделения
        if department_name not in existing_departments:
            raise ValueError(
                f"Подразделение '{department_name}' не существует в базе данных. Пожалуйста, добавьте его.")

        # Получаем или используем существующие записи
        type_instance = existing_types[type_name]
        status_instance = existing_statuses[status_name]
        project_instance = existing_projects[project_name]
        department_instance = existing_departments[department_name]

        # Добавляем нужное количество деталей
        count = int(self.addAddElementInterface.Text_Count.toPlainText())

        for _ in range(count):
            new_detail = Detail(
                name=self.addAddElementInterface.Text_Name.toPlainText(),
                type=type_instance,
                status=status_instance,
                project=project_instance,
                department=department_instance,
                users=self.addAddElementInterface.Text_FIO_2.toPlainText(),
                data=self.addAddElementInterface.dateTimeEdit.text(),
                note=self.addAddElementInterface.Text_Note_2.toPlainText()
            )

            db_session.add(new_detail)

        db_session.commit()  # Закоммитим все добавленные детали в конце

