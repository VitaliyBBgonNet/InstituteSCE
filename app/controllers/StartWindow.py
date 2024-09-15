from PySide6.QtWidgets import QApplication, QMainWindow, QWidget
from app.views.MainIterface import Ui_MainWindow
from InformationWindow import InformationWindow
import sys

class Interface(QMainWindow):
    def __init__(self, parent=None):
        super(Interface, self).__init__(parent)
        self.uiMainInterface = Ui_MainWindow()
        self.uiMainInterface.setupUi(self)

        self.uiMainInterface.PB_Arenda.clicked.connect(self.infoWindow)

    def infoWindow(self):
        self.infoWindow = InformationWindow()
        self.infoWindow.show()

if __name__ == '__main__':
    app = QApplication()
    window = Interface()
    window.show()
    sys.exit(app.exec())