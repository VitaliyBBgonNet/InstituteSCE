import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget,QTableWidget, QMessageBox, QMessageBox
from app.views.Information import Information
from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QFileDialog

class InformationWindowController(QMainWindow):
    def __init__(self, parent=None):
        super(InformationWindowController, self).__init__(parent)
        self.UiInformationInterface = Information()
        self.UiInformationInterface.setupUi(self)