import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget,QTableWidget, QMessageBox, QMessageBox
from sqlalchemy.orm.sync import clear

from app.views.Information import Information
from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QFileDialog
from app.db import SessionLocal, Detail
from app.db.models.Type import Type
from app.db.models.Status import Status
from app.db.models.Project import Project
from app.db.models.Department import Department
import uuid
from sqlalchemy.orm import joinedload

# 8379e672-aa8b-4629-9682-e0c9653f341e
class InformationWindowController(QMainWindow):
    def __init__(self, parent=None):
        super(InformationWindowController, self).__init__(parent)
        self.UiInformationInterface = Information()
        self.UiInformationInterface.setupUi(self)
        self.clerInformationFormBeforLoad()
        self.checkDatabase()
        self.UiInformationInterface.pushButton.clicked.connect(self.serchDetail)
        self.UiInformationInterface.PB_Add_ELEMENT_2.clicked.connect(self.changesDetail)
        self.UiInformationInterface.PB_DeleteElement.clicked.connect(self.deleteDetail)

    def deleteDetail(self):
        db_session = SessionLocal()
        searchIdDetail = uuid.UUID(self.UiInformationInterface.text_id_object.toPlainText())
        searchDetail = db_session.query(Detail).filter(Detail.id == searchIdDetail).first()
        db_session.delete(searchDetail)
        db_session.commit()

    def entitySearch(self):
        db_session = SessionLocal()
        searchIdDetail = self.UiInformationInterface.text_id_object.toPlainText()
        searchIdDetail = uuid.UUID(searchIdDetail)
        searchDetail = db_session.query(Detail).filter(Detail.id == searchIdDetail).options(
            joinedload(Detail.type),
            joinedload(Detail.status),
            joinedload(Detail.project),
            joinedload(Detail.department),
        ).first()

        return searchDetail

    def serchDetail(self):
        db_session = SessionLocal()
        searchDetail = self.entitySearch()

        self.UiInformationInterface.text_name_object.setText(searchDetail.name)
        self.UiInformationInterface.Box_object_fio.setText(searchDetail.users)
        self.UiInformationInterface.dateEdit_time.setDate(searchDetail.data)
        self.UiInformationInterface.Text_Name_3.setText(searchDetail.note)

        # Выдвигаем приоритетный тип
        indexType = self.UiInformationInterface.Box_object_type.findText(searchDetail.type.name)
        self.UiInformationInterface.Box_object_type.setCurrentIndex(indexType)

        indexStatus = self.UiInformationInterface.Box_object_State.findText(searchDetail.status.name)
        self.UiInformationInterface.Box_object_State.setCurrentIndex(indexStatus)

        indexProject = self.UiInformationInterface.Box_object_project.findText(searchDetail.project.name)
        self.UiInformationInterface.Box_object_project.setCurrentIndex(indexProject)

        indexDepartment = self.UiInformationInterface.Box_object_subdive.findText(searchDetail.department.name)
        self.UiInformationInterface.Box_object_project.setCurrentIndex(indexDepartment)

    def changesDetail(self):
        db_session = SessionLocal()

        searchIdDetailForUpdata = self.UiInformationInterface.text_id_object.toPlainText()
        searchIdDetailForUpdata = uuid.UUID(searchIdDetailForUpdata)
        updataDetail = db_session.query(Detail).filter(Detail.id == searchIdDetailForUpdata).options(
            joinedload(Detail.type),
            joinedload(Detail.status),
            joinedload(Detail.project),
            joinedload(Detail.department),
        ).first()

        selectType = db_session.query(Type).filter(Type.name == self.UiInformationInterface.Box_object_type.currentText()).first()
        selectStatus = db_session.query(Status).filter(Status.name == self.UiInformationInterface.Box_object_State.currentText()).first()
        selectDepartment = db_session.query(Department).filter(Department.name == self.UiInformationInterface.Box_object_subdive.currentText()).first()
        selectProject = db_session.query(Project).filter(Project.name == self.UiInformationInterface.Box_object_project.currentText()).first()

        updataDetail.type = selectType
        updataDetail.status = selectStatus
        updataDetail.department = selectDepartment
        updataDetail.project = selectProject

        updataDetail.name = self.UiInformationInterface.text_name_object.toPlainText()
        updataDetail.users = self.UiInformationInterface.Box_object_fio.toPlainText()
        updataDetail.note = self.UiInformationInterface.Text_Name_3.toPlainText()

        db_session.commit()

    def checkDatabase(self):
        db_session = SessionLocal()

        types = db_session.query(Type).all()
        states = db_session.query(Status).all()
        projects = db_session.query(Project).all()
        departments = db_session.query(Department).all()

        for temp in types:
            self.UiInformationInterface.Box_object_type.addItem(temp.name)

        for temp in states:
            self.UiInformationInterface.Box_object_State.addItem(temp.name)

        for temp in projects:
            self.UiInformationInterface.Box_object_project.addItem(temp.name)

        for temp in departments:
            self.UiInformationInterface.Box_object_subdive.addItem(temp.name)

    def clerInformationFormBeforLoad(self):
        self.UiInformationInterface.Box_object_type.clear()
        self.UiInformationInterface.Box_object_State.clear()
        self.UiInformationInterface.Box_object_project.clear()
        self.UiInformationInterface.Box_object_subdive.clear()