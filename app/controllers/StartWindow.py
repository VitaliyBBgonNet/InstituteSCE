from PySide6.QtWidgets import QApplication, QMainWindow, QWidget
from app.views.StartWindow import StartWindow
from InformationController import InformationWindowController
from AddElementController import AddElementController
from DataSetupController import DataSetupController
from QrGeneratorController import QrGeneratorController

from app.db import init_db
import sys


class Interface(QMainWindow):
    def __init__(self, parent=None):
        super(Interface, self).__init__(parent)
        self.uiMainInterface = StartWindow()
        self.uiMainInterface.setupUi(self)
        init_db()

        self.uiMainInterface.PB_Arenda.clicked.connect(self.infoWindowView)
        self.uiMainInterface.PB_Add_Element.clicked.connect(self.addElementWindowView)
        self.uiMainInterface.PB_Info.clicked.connect(self.DataSetupView)
        self.uiMainInterface.PB_QR.clicked.connect(self.qrGeneratorView)

    def infoWindowView(self):
        self.infoWindow = InformationWindowController()
        self.infoWindow.show()

    def addElementWindowView(self):
        self.w = AddElementController()
        self.w.show()

    def DataSetupView(self):
        self.DataSetup = DataSetupController()
        self.DataSetup.show()

    def qrGeneratorView(self):
        self.qrGenerator = QrGeneratorController()
        self.qrGenerator.show()


if __name__ == '__main__':
    app = QApplication()
    window = Interface()
    window.show()
    sys.exit(app.exec())
