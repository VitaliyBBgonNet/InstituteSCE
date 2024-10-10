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
        self.addAddElementInterface.dateTimeEdit.setDate(datetime.now())
        self.clearAllBeforeLoadUI()
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
            self.addAddElementInterface.Box_Project_Name.addItem(temp.name)

        for temp in departments:
            self.addAddElementInterface.Box_Name_Subdivade.addItem(temp.name)

    def clearAllBeforeLoadUI(self):
        self.addAddElementInterface.Box_Type.clear()
        self.addAddElementInterface.Box_Status.clear()
        self.addAddElementInterface.Box_Project_Name.clear()
        self.addAddElementInterface.Box_Name_Subdivade.clear()

    def print_test(self):
        db_session = SessionLocal()

        for temp in range(int(self.addAddElementInterface.Text_Count.toPlainText())):

            new_detail = Detail(
                name = self.addAddElementInterface.Text_Name.toPlainText(),
                type = Type(name = self.addAddElementInterface.Box_Type.currentText()),
                status = Status(name = self.addAddElementInterface.Box_Status.currentText()),
                project = Project(name = self.addAddElementInterface.Box_Project_Name.currentText()),
                department = Department(name = self.addAddElementInterface.Box_Project_Name.currentText()),
                users = self.addAddElementInterface.Text_FIO_2.toPlainText(),
                data = self.addAddElementInterface.dateTimeEdit.text(),
                note = self.addAddElementInterface.Text_Note_2.toPlainText()
            )

            db_session.add(new_detail)
            db_session.commit()
