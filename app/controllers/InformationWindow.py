import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget,QTableWidget, QMessageBox, QMessageBox
from app.views.InformationInterface import Ui_MainWindow
from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QFileDialog

class InformationWindow(QMainWindow):
    def __init__(self, parent=None):
        super(InformationWindow, self).__init__(parent)
        self.UiInformationInterface = Ui_MainWindow()
        self.UiInformationInterface.setupUi(self)