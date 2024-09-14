from PySide6.QtWidgets import QApplication, QMainWindow, QWidget
from app.views.MainIterface import Ui_MainWindow
import sys

class Interface(QMainWindow):
    def __init__(self, parent=None):
        super(Interface, self).__init__(parent)
        self.ui_Interface = Ui_MainWindow()
        self.ui_Interface.setupUi(self)


if __name__ == '__main__':
    app = QApplication()
    window = Interface()
    window.show()
    sys.exit(app.exec())
