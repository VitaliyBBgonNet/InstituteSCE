import sys
import datetime

from PySide6.QtWidgets import QApplication, QMainWindow

from app.views.EddElementInterface import EddElementWindow

class AddElementService(QMainWindow):
    def __init__(self, parent=None):
        super(AddElementService, self).__init__(parent)
        self.ui = EddElementWindow()
        self.ui.setupUi(self)
