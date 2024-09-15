from PySide6.QtWidgets import QApplication, QMainWindow

from app.views.AddElement import AddElement

class AddElementController(QMainWindow):
    def __init__(self, parent=None):
        super(AddElementController, self).__init__(parent)
        self.addAddElementInterface = AddElement()
        self.addAddElementInterface.setupUi(self)
