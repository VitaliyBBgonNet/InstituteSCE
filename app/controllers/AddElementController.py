from PySide6.QtWidgets import QApplication, QMainWindow
from app.views.AddElement import AddElement
from app.db.models.Details import Detail
from app.db.models.Type import Type
from app.db.models.Status import Status
from app.db.models.Project import Project
from app.db.models.Department import Department
from app.db.models.User import User
from app.db import SessionLocal
from datetime import datetime


class AddElementController(QMainWindow):
    def __init__(self, parent=None):
        super(AddElementController, self).__init__(parent)
        self.addAddElementInterface = AddElement()
        self.addAddElementInterface.setupUi(self)
        self.checkDatabase()
        self.addAddElementInterface.PB_Add_ELEMENT_2.clicked.connect(self.print_test)

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
            self.addAddElementInterface.Box_Status.addItem(temp.name)

        for temp in departments:
            self.addAddElementInterface.Box_Name_Subdivade.addItem(temp.name)

    def print_test(self):
        db_session = SessionLocal()
        type_obj = Type(name="Test Type")
        status_obj = Status(name="Test Status")
        project_obj = Project(name="Test Project")
        department_obj = Department(name="Test Department")
        user_obj = User(full_name="Test User")

        for i in range(int(self.addAddElementInterface.Text_Count.toPlainText())):
            print(i)

            new_detail = Detail(
                name=self.addAddElementInterface.Text_Name.toPlainText(),
                type=type_obj,  # Присваиваем объект типа
                status=status_obj,  # Присваиваем объект состояния
                project=project_obj,  # Присваиваем объект проекта
                department=department_obj,  # Присваиваем объект подразделения
                user=user_obj,  # Присваиваем объект пользователя
                data=datetime.now(),  # Текущая дата
                note="This is a test note"  # Примечание
            )

            db_session.add(new_detail)
            db_session.commit()
