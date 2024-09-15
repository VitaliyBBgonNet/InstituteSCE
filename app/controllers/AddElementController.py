from PySide6.QtWidgets import QApplication, QMainWindow

from app.views.AddElementInterface import AddElementWindow

class AddElementController(QMainWindow):
    def __init__(self, parent=None):
        super(AddElementController, self).__init__(parent)
        self.ui = AddElementWindow()
        self.ui.setupUi(self)
