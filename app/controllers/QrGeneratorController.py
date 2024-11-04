import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QTableWidget, QMessageBox, QTableWidgetItem
from PySide6.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QCheckBox, QVBoxLayout, QWidget
from app.views.QrsGenerator import QrGenerator
from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QFileDialog
from app.db import SessionLocal
from app.db.models.Type import Type
from app.db.models.Status import Status
from app.db.models.Project import Project
from app.db.models.Department import Department
from app.db.models.Details import Detail

class QrGeneratorController(QMainWindow):
    def __init__(self, parent=None):
        super(QrGeneratorController, self).__init__(parent)
        self.qrInterface = QrGenerator()
        self.qrInterface.setupUi(self)
        self.checkDatabase()
        self.qrInterface.PbSearch.clicked.connect(self.searchElements)

    def checkDatabase(self):
        db_session = SessionLocal()

        types = db_session.query(Type).all()
        states = db_session.query(Status).all()
        projects = db_session.query(Project).all()
        departments = db_session.query(Department).all()

        for temp in types:
            self.qrInterface.BoxType.addItem(temp.name)

        for temp in states:
            self.qrInterface.BoxStatus.addItem(temp.name)

        for temp in projects:
            self.qrInterface.BoxProject.addItem(temp.name)

        for temp in departments:
            self.qrInterface.BoxDepartment.addItem(temp.name)

    def searchElements(self):

        type = self.qrInterface.BoxType.currentText()
        status = self.qrInterface.BoxStatus.currentText()
        project = self.qrInterface.BoxProject.currentText()
        departments = self.qrInterface.BoxDepartment.currentText()

        dbSession = SessionLocal()

        try:
            query = dbSession.query(Detail)

            if type:
                query = query.filter(Detail.type.has(name = type))

            if status:
                query = query.filter(Detail.status.has(name = status))

            if project:
                query = query.filter(Detail.project.has(name = project))

            if departments:
                query = query.filter(Detail.department.has(name = project))

            result = query.all()

            for i in result:
                print(i)

            return result

        except Exception as e:
            QMessageBox.critical(self, "Search Error")
        finally:
            dbSession.close()
