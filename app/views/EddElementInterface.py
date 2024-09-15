# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Add_Elemet_New.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDateTimeEdit, QFrame,
    QLabel, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QStatusBar, QTextEdit, QVBoxLayout,
    QWidget)

class EddElementWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(563, 749)
        MainWindow.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(81, 0, 135, 255), stop:0.427447 rgba(41, 61, 132, 235), stop:1 rgba(155, 79, 165, 255));\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.Labe_Status = QLabel(self.centralwidget)
        self.Labe_Status.setObjectName(u"Labe_Status")
        self.Labe_Status.setGeometry(QRect(40, 260, 101, 23))
        font = QFont()
        font.setFamilies([u"LXGW WenKai TC"])
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        self.Labe_Status.setFont(font)
        self.Labe_Status.setStyleSheet(u"color: white;\n"
"font-weight: bold;\n"
"background-color: none;\n"
"border: none;\n"
"font: 14pt \"LXGW WenKai TC\";")
        self.Box_Status = QComboBox(self.centralwidget)
        self.Box_Status.setObjectName(u"Box_Status")
        self.Box_Status.setGeometry(QRect(150, 260, 371, 31))
        self.Box_Status.setStyleSheet(u"background-color: rgba(255, 255, 255, 30); \n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-radius: 7px;\n"
"\n"
"font-size: 16pt;\n"
"color: white;\n"
"\n"
"font: 14pt \"LXGW WenKai TC\";")
        self.Labe_Name_ = QLabel(self.centralwidget)
        self.Labe_Name_.setObjectName(u"Labe_Name_")
        self.Labe_Name_.setGeometry(QRect(40, 160, 141, 23))
        self.Labe_Name_.setFont(font)
        self.Labe_Name_.setStyleSheet(u"color: white;\n"
"font-weight: bold;\n"
"background-color: none;\n"
"border: none;\n"
"font: 14pt \"LXGW WenKai TC\";")
        self.Lable_Note_2 = QLabel(self.centralwidget)
        self.Lable_Note_2.setObjectName(u"Lable_Note_2")
        self.Lable_Note_2.setGeometry(QRect(40, 500, 116, 23))
        self.Lable_Note_2.setFont(font)
        self.Lable_Note_2.setStyleSheet(u"color: white;\n"
"font-weight: bold;\n"
"background-color: none;\n"
"border: none;\n"
"font: 14pt \"LXGW WenKai TC\";")
        self.Box_Project_Name = QComboBox(self.centralwidget)
        self.Box_Project_Name.setObjectName(u"Box_Project_Name")
        self.Box_Project_Name.setGeometry(QRect(120, 310, 401, 31))
        self.Box_Project_Name.setStyleSheet(u"background-color: rgba(255, 255, 255, 30); \n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-radius: 7px;\n"
"\n"
"font-size: 16pt;\n"
"color: white;\n"
"\n"
"font: 14pt \"LXGW WenKai TC\";")
        self.Text_FIO_2 = QTextEdit(self.centralwidget)
        self.Text_FIO_2.setObjectName(u"Text_FIO_2")
        self.Text_FIO_2.setGeometry(QRect(110, 420, 411, 41))
        self.Text_FIO_2.setFont(font)
        self.Text_FIO_2.setStyleSheet(u"background-color: rgba(255, 255, 255, 30); \n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-radius: 7px;\n"
"color: white;\n"
"font: 14pt \"LXGW WenKai TC\";")
        self.Box_Name_Subdivade = QComboBox(self.centralwidget)
        self.Box_Name_Subdivade.setObjectName(u"Box_Name_Subdivade")
        self.Box_Name_Subdivade.setGeometry(QRect(200, 370, 321, 31))
        self.Box_Name_Subdivade.setStyleSheet(u"background-color: rgba(255, 255, 255, 30); \n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-radius: 7px;\n"
"\n"
"font-size: 16pt;\n"
"color: white;\n"
"\n"
"font: 14pt \"LXGW WenKai TC\";")
        self.Lable_FIO_2 = QLabel(self.centralwidget)
        self.Lable_FIO_2.setObjectName(u"Lable_FIO_2")
        self.Lable_FIO_2.setGeometry(QRect(40, 420, 59, 23))
        self.Lable_FIO_2.setFont(font)
        self.Lable_FIO_2.setStyleSheet(u"color: white;\n"
"font-weight: bold;\n"
"background-color: none;\n"
"border: none;\n"
"font: 14pt \"LXGW WenKai TC\";")
        self.Labe_Count = QLabel(self.centralwidget)
        self.Labe_Count.setObjectName(u"Labe_Count")
        self.Labe_Count.setGeometry(QRect(40, 210, 111, 23))
        self.Labe_Count.setFont(font)
        self.Labe_Count.setStyleSheet(u"color: white;\n"
"font-weight: bold;\n"
"background-color: none;\n"
"border: none;\n"
"font: 14pt \"LXGW WenKai TC\";")
        self.Labe_Name_Project = QLabel(self.centralwidget)
        self.Labe_Name_Project.setObjectName(u"Labe_Name_Project")
        self.Labe_Name_Project.setGeometry(QRect(40, 310, 71, 23))
        self.Labe_Name_Project.setFont(font)
        self.Labe_Name_Project.setStyleSheet(u"color: white;\n"
"font-weight: bold;\n"
"background-color: none;\n"
"border: none;\n"
"font: 14pt \"LXGW WenKai TC\";")
        self.Labe_Name_Subdivade = QLabel(self.centralwidget)
        self.Labe_Name_Subdivade.setObjectName(u"Labe_Name_Subdivade")
        self.Labe_Name_Subdivade.setGeometry(QRect(40, 370, 151, 23))
        self.Labe_Name_Subdivade.setFont(font)
        self.Labe_Name_Subdivade.setStyleSheet(u"color: white;\n"
"font-weight: bold;\n"
"background-color: none;\n"
"border: none;\n"
"font: 14pt \"LXGW WenKai TC\";")
        self.Box_Type = QComboBox(self.centralwidget)
        self.Box_Type.setObjectName(u"Box_Type")
        self.Box_Type.setGeometry(QRect(90, 110, 431, 31))
        self.Box_Type.setStyleSheet(u"background-color: rgba(255, 255, 255, 30); \n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-radius: 7px;\n"
"\n"
"font-size: 16pt;\n"
"color: white;\n"
"\n"
"font: 14pt \"LXGW WenKai TC\";")
        self.Labe_Type = QLabel(self.centralwidget)
        self.Labe_Type.setObjectName(u"Labe_Type")
        self.Labe_Type.setGeometry(QRect(40, 110, 41, 23))
        self.Labe_Type.setFont(font)
        self.Labe_Type.setStyleSheet(u"color: white;\n"
"font-weight: bold;\n"
"background-color: none;\n"
"border: none;\n"
"font: 14pt \"LXGW WenKai TC\";")
        self.Text_Note_2 = QTextEdit(self.centralwidget)
        self.Text_Note_2.setObjectName(u"Text_Note_2")
        self.Text_Note_2.setGeometry(QRect(40, 530, 481, 81))
        self.Text_Note_2.setFont(font)
        self.Text_Note_2.setStyleSheet(u"background-color: rgba(255, 255, 255, 30); \n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-radius: 7px;\n"
"color: white;\n"
"font: 14pt \"LXGW WenKai TC\";")
        self.Text_Count = QTextEdit(self.centralwidget)
        self.Text_Count.setObjectName(u"Text_Count")
        self.Text_Count.setGeometry(QRect(160, 210, 361, 41))
        self.Text_Count.setFont(font)
        self.Text_Count.setAcceptDrops(True)
        self.Text_Count.setAutoFillBackground(True)
        self.Text_Count.setStyleSheet(u"background-color: rgba(255, 255, 255, 30); \n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-radius: 7px;\n"
"color: white;\n"
"font: 14pt \"LXGW WenKai TC\";")
        self.Label_Bace_Title_ADD_ELEMENT = QLabel(self.centralwidget)
        self.Label_Bace_Title_ADD_ELEMENT.setObjectName(u"Label_Bace_Title_ADD_ELEMENT")
        self.Label_Bace_Title_ADD_ELEMENT.setGeometry(QRect(130, 20, 321, 71))
        font1 = QFont()
        font1.setFamilies([u"LXGW WenKai TC"])
        font1.setPointSize(25)
        font1.setBold(False)
        font1.setItalic(False)
        self.Label_Bace_Title_ADD_ELEMENT.setFont(font1)
        self.Label_Bace_Title_ADD_ELEMENT.setStyleSheet(u"color: white;\n"
"font-weight: bold;\n"
"font: 25pt \"LXGW WenKai TC\";\n"
"background-color: none;\n"
"border: none;")
        self.PB_Add_ELEMENT_2 = QPushButton(self.centralwidget)
        self.PB_Add_ELEMENT_2.setObjectName(u"PB_Add_ELEMENT_2")
        self.PB_Add_ELEMENT_2.setGeometry(QRect(180, 630, 191, 61))
        self.PB_Add_ELEMENT_2.setFont(font)
        self.PB_Add_ELEMENT_2.setStyleSheet(u"background-color: rgba(255, 255, 255, 30); \n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-radius: 7px;\n"
"color: white;\n"
"font-weight: bold;\n"
"font: 14pt \"LXGW WenKai TC\";")
        self.Text_Name = QTextEdit(self.centralwidget)
        self.Text_Name.setObjectName(u"Text_Name")
        self.Text_Name.setGeometry(QRect(190, 160, 331, 41))
        self.Text_Name.setFont(font)
        self.Text_Name.setAcceptDrops(True)
        self.Text_Name.setStyleSheet(u"background-color: rgba(255, 255, 255, 30); \n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-radius: 7px;\n"
"color: white;\n"
"font: 14pt \"LXGW WenKai TC\";")
        self.dateTimeEdit = QDateTimeEdit(self.centralwidget)
        self.dateTimeEdit.setObjectName(u"dateTimeEdit")
        self.dateTimeEdit.setGeometry(QRect(100, 470, 421, 31))
        self.dateTimeEdit.setStyleSheet(u"background-color: rgba(255, 255, 255, 30); \n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-radius: 7px;\n"
"color: white;\n"
"font: 14pt \"LXGW WenKai TC\";")
        self.Lable_FIO_3 = QLabel(self.centralwidget)
        self.Lable_FIO_3.setObjectName(u"Lable_FIO_3")
        self.Lable_FIO_3.setGeometry(QRect(40, 470, 59, 23))
        self.Lable_FIO_3.setFont(font)
        self.Lable_FIO_3.setStyleSheet(u"color: white;\n"
"font-weight: bold;\n"
"background-color: none;\n"
"border: none;\n"
"font: 14pt \"LXGW WenKai TC\";")
        self.new_transaction = QFrame(self.centralwidget)
        self.new_transaction.setObjectName(u"new_transaction")
        self.new_transaction.setGeometry(QRect(10, 10, 541, 691))
        self.new_transaction.setStyleSheet(u"background-color: rgba(255, 255, 255, 30); \n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-radius: 7px;")
        self.new_transaction.setFrameShape(QFrame.NoFrame)
        self.new_transaction.setFrameShadow(QFrame.Raised)
        self.verticalLayout_21 = QVBoxLayout(self.new_transaction)
        self.verticalLayout_21.setSpacing(6)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(12, 12, 12, 12)
        MainWindow.setCentralWidget(self.centralwidget)
        self.new_transaction.raise_()
        self.Labe_Status.raise_()
        self.Box_Status.raise_()
        self.Labe_Name_.raise_()
        self.Lable_Note_2.raise_()
        self.Box_Project_Name.raise_()
        self.Text_FIO_2.raise_()
        self.Box_Name_Subdivade.raise_()
        self.Lable_FIO_2.raise_()
        self.Labe_Count.raise_()
        self.Labe_Name_Project.raise_()
        self.Labe_Name_Subdivade.raise_()
        self.Box_Type.raise_()
        self.Labe_Type.raise_()
        self.Text_Note_2.raise_()
        self.Text_Count.raise_()
        self.Label_Bace_Title_ADD_ELEMENT.raise_()
        self.PB_Add_ELEMENT_2.raise_()
        self.Text_Name.raise_()
        self.dateTimeEdit.raise_()
        self.Lable_FIO_3.raise_()
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 563, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.Labe_Status.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0441\u0442\u043e\u044f\u043d\u0438\u0435:", None))
        self.Labe_Name_.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0438\u043c\u0435\u043d\u043e\u0432\u0430\u043d\u0438\u0435:", None))
        self.Lable_Note_2.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0438\u043c\u0435\u0447\u0430\u043d\u0438\u0435:", None))
        self.Lable_FIO_2.setText(QCoreApplication.translate("MainWindow", u"\u0424.\u0418.\u041e:", None))
        self.Labe_Count.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e:", None))
        self.Labe_Name_Project.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u043e\u0435\u043a\u0442:", None))
        self.Labe_Name_Subdivade.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0434\u0440\u0430\u0437\u0434\u0435\u043b\u0435\u043d\u0438\u0435:", None))
        self.Labe_Type.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0438\u043f:", None))
        self.Label_Bace_Title_ADD_ELEMENT.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u042d\u043b\u0435\u043c\u0435\u043d\u0442", None))
        self.PB_Add_ELEMENT_2.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.Lable_FIO_3.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0430\u0442\u0430:", None))
    # retranslateUi

