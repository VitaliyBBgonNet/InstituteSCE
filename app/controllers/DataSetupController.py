from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QTableWidget, QMessageBox
from app.views.DataSetup import DataSetup


class DataSetupController(QMainWindow):
    def __init__(self, parent=None):
        super(DataSetupController, self).__init__(parent)
        self.dataSetupInterface = DataSetup()
        self.dataSetupInterface.setupUi(self)
