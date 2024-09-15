from PySide6.QtWidgets import QApplication, QMainWindow, QWidget
from app.views.MainIterface import Ui_MainWindow
from InformationController import InformationWindow
from AddElementController import AddElementController
from DataSetupController import DataSetupController
import sys

class Interface(QMainWindow):
    def __init__(self, parent=None):
        super(Interface, self).__init__(parent)
        self.uiMainInterface = Ui_MainWindow()
        self.uiMainInterface.setupUi(self)

        self.uiMainInterface.PB_Arenda.clicked.connect(self.infoWindowView)
        self.uiMainInterface.PB_Add_Element.clicked.connect(self.addElementWindowView)
        self.uiMainInterface.PB_Info.clicked.connect(self.DataSetupView)

    def infoWindowView(self):
        self.infoWindow = InformationWindow()
        self.infoWindow.show()

    def addElementWindowView(self):
        self.w = AddElementController()
        self.w.show()

    def DataSetupView(self):
        self.DataSetup = DataSetupController()
        self.DataSetup.show()

if __name__ == '__main__':
    app = QApplication()
    window = Interface()
    window.show()
    sys.exit(app.exec())