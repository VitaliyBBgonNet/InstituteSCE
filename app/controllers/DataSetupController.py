from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QTableWidget, QMessageBox
from app.views.DataSetup import DataSetupWindow


class DataSetupController(QMainWindow):
    def __init__(self, parent=None):
        super(DataSetupController, self).__init__(parent)
        self.Data_Setup_Settings = DataSetupWindow()
        self.Data_Setup_Settings.setupUi(self)
