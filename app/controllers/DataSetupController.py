from PySide6.QtWidgets import QMainWindow

from app.db import SessionLocal
from app.db.models.Department import Department
from app.db.models.Project import Project
from app.db.models.Status import Status
from app.db.models.Type import Type
from app.views.DataSetup import DataSetup


class DataSetupController(QMainWindow):
    def __init__(self, parent=None):
        super(DataSetupController, self).__init__(parent)
        self.dataSetupInterface = DataSetup()
        self.dataSetupInterface.setupUi(self)
        self.checkDatabase()
        self.dataSetupInterface.PB_Add_Type.clicked.connect(lambda: self.addEntry('type'))
        self.dataSetupInterface.PB_Add_State.clicked.connect(lambda: self.addEntry('status'))
        self.dataSetupInterface.PB_Add_Project.clicked.connect(lambda: self.addEntry('projects'))
        self.dataSetupInterface.PB_Add_Sabdvide.clicked.connect(lambda: self.addEntry('department'))

    def addEntry(self, entry_type: str):
        db_session = SessionLocal()

        try:

            model_class = None
            text_to_add = ""

            # Определяем логику для каждого типа
            if entry_type == 'type':
                text_to_add = self.dataSetupInterface.Text_Type.toPlainText()
                if db_session.query(Type).filter(Type.name == text_to_add).first():
                    raise ValueError("Такой тип уже существует.")
                model_class = Type

            elif entry_type == 'status':
                text_to_add = self.dataSetupInterface.Text_State.toPlainText()
                if db_session.query(Status).filter(Status.name == text_to_add).first():
                    raise ValueError("Такой статус уже существует.")
                model_class = Status

            elif entry_type == 'projects':
                text_to_add = self.dataSetupInterface.Text_Project.toPlainText()
                if db_session.query(Project).filter(Project.name == text_to_add).first():
                    raise ValueError("Такой проект уже существует.")
                model_class = Project

            elif entry_type == 'department':
                text_to_add = self.dataSetupInterface.Text_Subdive.toPlainText()
                if db_session.query(Department).filter(Department.name == text_to_add).first():
                    raise ValueError("Такой отдел уже существует.")
                model_class = Department

            else:
                raise ValueError("Неверный тип записи. Ожидалось 'type', 'status', 'projects' или 'department'.")

            # Проверяем, что текст не пустой
            if not text_to_add.strip():
                raise ValueError("Текст не может быть пустым.")

            # Создаём и добавляем новую запись в базу данных
            entry = model_class(name=text_to_add)
            db_session.add(entry)
            db_session.commit()

        except ValueError as e:
            print(f"Ошибка: {e}")
            db_session.rollback()  # Откат изменений при ошибке

        except Exception as e:
            print(f"Неожиданная ошибка: {e}")
            db_session.rollback()  # Откат изменений при любой ошибке

        finally:
            self.dataSetupInterface.Text_Type.clear()
            self.dataSetupInterface.Text_State.clear()
            self.dataSetupInterface.Text_Subdive.clear()
            self.dataSetupInterface.Text_Project.clear()
            self.checkDatabase()
            db_session.close()  # Закрываем сессию

    def checkDatabase(self):
        db_session = SessionLocal()
        self.dataSetupInterface.Box_Type.clear()
        self.dataSetupInterface.Box_State.clear()
        self.dataSetupInterface.Box_Project.clear()
        self.dataSetupInterface.Box_Subdive.clear()

        types = db_session.query(Type).all()
        states = db_session.query(Status).all()
        projects = db_session.query(Project).all()
        departments = db_session.query(Department).all()

        for temp in types:
            self.dataSetupInterface.Box_Type.addItem(temp.name)

        for temp in states:
            self.dataSetupInterface.Box_State.addItem(temp.name)

        for temp in projects:
            self.dataSetupInterface.Box_Project.addItem(temp.name)

        for temp in departments:
            self.dataSetupInterface.Box_Subdive.addItem(temp.name)
        db_session.commit()
