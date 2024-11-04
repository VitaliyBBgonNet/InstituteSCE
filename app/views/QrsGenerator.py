# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'QrGeneratorUI.ui'
##
## Created by: Qt User Interface Compiler version 6.7.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QHeaderView,
    QLabel, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QStatusBar, QTableWidget, QTableWidgetItem,
    QTextEdit, QVBoxLayout, QWidget)

class QrGenerator(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1319, 812)
        MainWindow.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(81, 0, 135, 255), stop:0.427447 rgba(41, 61, 132, 235), stop:1 rgba(155, 79, 165, 255));\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(940, 130, 51, 16))
        font = QFont()
        font.setFamilies([u"LXGW WenKai TC"])
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"color: white;\n"
"font-weight: bold;\n"
"background-color: none;\n"
"border: none;\n"
"font: 14pt \"LXGW WenKai TC\";")
        self.PbGenerateQR = QPushButton(self.centralwidget)
        self.PbGenerateQR.setObjectName(u"PbGenerateQR")
        self.PbGenerateQR.setGeometry(QRect(940, 490, 361, 51))
        self.PbGenerateQR.setStyleSheet(u"background-color: rgba(255, 255, 255, 30); \n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-radius: 7px;\n"
"color: white;\n"
"font-weight: bold;\n"
"font: 14pt \"LXGW WenKai TC\";")
        self.PbSearch = QPushButton(self.centralwidget)
        self.PbSearch.setObjectName(u"PbSearch")
        self.PbSearch.setGeometry(QRect(940, 330, 361, 51))
        self.PbSearch.setStyleSheet(u"background-color: rgba(255, 255, 255, 30); \n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-radius: 7px;\n"
"color: white;\n"
"font-weight: bold;\n"
"font: 14pt \"LXGW WenKai TC\";")
        self.BoxType = QComboBox(self.centralwidget)
        self.BoxType.setObjectName(u"BoxType")
        self.BoxType.setGeometry(QRect(990, 120, 311, 31))
        self.BoxType.setStyleSheet(u"background-color: rgba(255, 255, 255, 30); \n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-radius: 7px;\n"
"\n"
"font-size: 16pt;\n"
"color: white;\n"
"\n"
"font: 14pt \"LXGW WenKai TC\";")
        self.PbClearFilter = QPushButton(self.centralwidget)
        self.PbClearFilter.setObjectName(u"PbClearFilter")
        self.PbClearFilter.setGeometry(QRect(940, 390, 361, 41))
        self.PbClearFilter.setStyleSheet(u"background-color: rgba(255, 255, 255, 30); \n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-radius: 7px;\n"
"color: white;\n"
"font-weight: bold;\n"
"font: 14pt \"LXGW WenKai TC\";")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(940, 440, 51, 31))
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(u"color: white;\n"
"font-weight: bold;\n"
"background-color: none;\n"
"border: none;\n"
"font: 14pt \"LXGW WenKai TC\";")
        self.textName = QTextEdit(self.centralwidget)
        self.textName.setObjectName(u"textName")
        self.textName.setGeometry(QRect(990, 70, 311, 41))
        self.textName.setStyleSheet(u"background-color: rgba(255, 255, 255, 30); \n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-radius: 7px;\n"
"color: white;\n"
"font: 14pt \"LXGW WenKai TC\";")
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(940, 80, 51, 16))
        self.label_4.setFont(font)
        self.label_4.setStyleSheet(u"color: white;\n"
"font-weight: bold;\n"
"background-color: none;\n"
"border: none;\n"
"font: 14pt \"LXGW WenKai TC\";")
        self.textWayForSave = QTextEdit(self.centralwidget)
        self.textWayForSave.setObjectName(u"textWayForSave")
        self.textWayForSave.setGeometry(QRect(1000, 440, 251, 41))
        self.textWayForSave.setStyleSheet(u"background-color: rgba(255, 255, 255, 30); \n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-radius: 7px;\n"
"color: white;\n"
"font: 14pt \"LXGW WenKai TC\";")
        self.PbTakeWay = QPushButton(self.centralwidget)
        self.PbTakeWay.setObjectName(u"PbTakeWay")
        self.PbTakeWay.setGeometry(QRect(1260, 440, 41, 41))
        self.PbTakeWay.setStyleSheet(u"background-color: rgba(255, 255, 255, 30); \n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-radius: 7px;\n"
"color: white;\n"
"font-weight: bold;\n"
"font: 14pt \"LXGW WenKai TC\";")
        self.tableListDetails = QTableWidget(self.centralwidget)
        self.tableListDetails.setObjectName(u"tableListDetails")
        self.tableListDetails.setGeometry(QRect(40, 70, 871, 641))
        self.tableListDetails.setStyleSheet(u"QTableView {\n"
"background-color: rgba(255, 255, 255, 30); \n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-radius: 10px;\n"
"color: white;\n"
"font: 14pt \"LXGW WenKai TC\";\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"background-color: rgba(53, 53, 53,100);\n"
"color: white;\n"
"border: none;\n"
"height: 50px;\n"
"font-size: 16pt;\n"
"font: 14pt \"LXGW WenKai TC\";\n"
"}\n"
"\n"
"QTableView::item {\n"
"    border-style: none;\n"
"    border-bottom: 1px solid rgba(255,255,255,50);\n"
"    padding-left: auto;\n"
"    padding-right: auto;\n"
"font: 14pt \"LXGW WenKai TC\";\n"
"}\n"
"\n"
"QTableView::item:selected{\n"
"	border: none;\n"
"	color: rgb(255, 255, 255);\n"
"    background-color: rgba(255, 255, 255, 50);\n"
"font: 14pt \"LXGW WenKai TC\";\n"
"}\n"
"\n"
"QCheckBox {\n"
"background-color: rgba(255, 255, 255, 0);\n"
"border: 1px solid rgba(255, 255, 255, 0);\n"
"border-radius: 5px;\n"
"color: white;\n"
"font: 14pt \"LXGW WenKai TC\";\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"background-color"
                        ": rgba(255, 255, 255, 100);\n"
"border: 1px solid rgba(255, 255, 255, 100);\n"
"font: 14pt \"LXGW WenKai TC\";\n"
"}")
        self.tableListDetails.setShowGrid(False)
        self.tableListDetails.horizontalHeader().setCascadingSectionResizes(True)
        self.tableListDetails.horizontalHeader().setMinimumSectionSize(120)
        self.tableListDetails.horizontalHeader().setDefaultSectionSize(150)
        self.tableListDetails.horizontalHeader().setHighlightSections(True)
        self.tableListDetails.horizontalHeader().setProperty(u"showSortIndicator", False)
        self.tableListDetails.horizontalHeader().setStretchLastSection(False)
        self.tableListDetails.verticalHeader().setProperty(u"showSortIndicator", False)
        self.new_transaction = QFrame(self.centralwidget)
        self.new_transaction.setObjectName(u"new_transaction")
        self.new_transaction.setGeometry(QRect(10, 10, 1301, 751))
        self.new_transaction.setStyleSheet(u"background-color: rgba(255, 255, 255, 30); \n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-radius: 7px;")
        self.new_transaction.setFrameShape(QFrame.NoFrame)
        self.new_transaction.setFrameShadow(QFrame.Raised)
        self.verticalLayout_21 = QVBoxLayout(self.new_transaction)
        self.verticalLayout_21.setSpacing(6)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(12, 12, 12, 12)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(420, 0, 241, 71))
        self.label.setStyleSheet(u"color: white;\n"
"font-weight: bold;\n"
"background-color: none;\n"
"border: none;\n"
"font: 25pt \"LXGW WenKai TC\";")
        self.textFIO = QTextEdit(self.centralwidget)
        self.textFIO.setObjectName(u"textFIO")
        self.textFIO.setGeometry(QRect(1010, 280, 291, 41))
        self.textFIO.setStyleSheet(u"background-color: rgba(255, 255, 255, 30); \n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-radius: 7px;\n"
"color: white;\n"
"font: 14pt \"LXGW WenKai TC\";")
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(940, 290, 61, 16))
        self.label_5.setFont(font)
        self.label_5.setStyleSheet(u"color: white;\n"
"font-weight: bold;\n"
"background-color: none;\n"
"border: none;\n"
"font: 14pt \"LXGW WenKai TC\";")
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(940, 160, 61, 31))
        self.label_6.setFont(font)
        self.label_6.setStyleSheet(u"color: white;\n"
"font-weight: bold;\n"
"background-color: none;\n"
"border: none;\n"
"font: 14pt \"LXGW WenKai TC\";")
        self.BoxProject = QComboBox(self.centralwidget)
        self.BoxProject.setObjectName(u"BoxProject")
        self.BoxProject.setGeometry(QRect(1010, 160, 291, 31))
        self.BoxProject.setStyleSheet(u"background-color: rgba(255, 255, 255, 30); \n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-radius: 7px;\n"
"\n"
"font-size: 16pt;\n"
"color: white;\n"
"\n"
"font: 14pt \"LXGW WenKai TC\";")
        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(940, 200, 111, 31))
        self.label_7.setFont(font)
        self.label_7.setStyleSheet(u"color: white;\n"
"font-weight: bold;\n"
"background-color: none;\n"
"border: none;\n"
"font: 14pt \"LXGW WenKai TC\";")
        self.BoxStatus = QComboBox(self.centralwidget)
        self.BoxStatus.setObjectName(u"BoxStatus")
        self.BoxStatus.setGeometry(QRect(1050, 200, 251, 31))
        self.BoxStatus.setStyleSheet(u"background-color: rgba(255, 255, 255, 30); \n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-radius: 7px;\n"
"\n"
"font-size: 16pt;\n"
"color: white;\n"
"\n"
"font: 14pt \"LXGW WenKai TC\";")
        self.label_8 = QLabel(self.centralwidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(940, 240, 151, 31))
        self.label_8.setFont(font)
        self.label_8.setStyleSheet(u"color: white;\n"
"font-weight: bold;\n"
"background-color: none;\n"
"border: none;\n"
"font: 14pt \"LXGW WenKai TC\";")
        self.BoxDepartment = QComboBox(self.centralwidget)
        self.BoxDepartment.setObjectName(u"BoxDepartment")
        self.BoxDepartment.setGeometry(QRect(1060, 240, 241, 31))
        self.BoxDepartment.setStyleSheet(u"background-color: rgba(255, 255, 255, 30); \n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-radius: 7px;\n"
"\n"
"font-size: 16pt;\n"
"color: white;\n"
"\n"
"font: 14pt \"LXGW WenKai TC\";")
        MainWindow.setCentralWidget(self.centralwidget)
        self.new_transaction.raise_()
        self.label_2.raise_()
        self.PbGenerateQR.raise_()
        self.PbSearch.raise_()
        self.BoxType.raise_()
        self.PbClearFilter.raise_()
        self.label_3.raise_()
        self.textName.raise_()
        self.label_4.raise_()
        self.textWayForSave.raise_()
        self.PbTakeWay.raise_()
        self.tableListDetails.raise_()
        self.label.raise_()
        self.textFIO.raise_()
        self.label_5.raise_()
        self.label_6.raise_()
        self.BoxProject.raise_()
        self.label_7.raise_()
        self.BoxStatus.raise_()
        self.label_8.raise_()
        self.BoxDepartment.raise_()
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1319, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"QR_Generator", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0438\u043f:", None))
        self.PbGenerateQR.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0437\u0434\u0430\u0442\u044c QR", None))
        self.PbSearch.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0438\u0441\u043a", None))
        self.PbClearFilter.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0447\u0438\u0441\u0442\u0438\u0442\u044c", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0443\u0442\u044c:", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u0418\u043c\u044f:", None))
        self.PbTakeWay.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u0413\u0435\u043d\u0435\u0440\u0430\u0446\u0438\u044f QR", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u0424.\u0418.\u041e.", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u043e\u0435\u043a:", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0441\u0442\u043e\u044f\u043d\u0438\u0435:", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0434\u0440\u0430\u0437\u0434\u0435\u043b.:", None))
    # retranslateUi

