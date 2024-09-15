import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QTableWidget, QMessageBox, QTableWidgetItem
from PySide6.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QCheckBox, QVBoxLayout, QWidget
from app.views.QrGenerator import QrGenerator
from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QFileDialog

class QrGeneratorController(QMainWindow):
    def __init__(self, parent=None):
        super(QrGeneratorController, self).__init__(parent)
        self.qrInterface = QrGenerator()
        self.qrInterface.setupUi(self)
