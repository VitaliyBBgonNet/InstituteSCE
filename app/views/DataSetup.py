# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Data_Setup.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QLabel,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QTextEdit, QVBoxLayout, QWidget)

class DataSetup(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(758, 417)
        MainWindow.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(81, 0, 135, 255), stop:0.427447 rgba(41, 61, 132, 235), stop:1 rgba(155, 79, 165, 255));\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 70, 53, 32))
        font = QFont()
        font.setFamilies([u"LXGW WenKai TC"])
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        self.label.setFont(font)
        self.label.setStyleSheet(u"color: white;\n"
"font-weight: bold;\n"
"background-color: none;\n"
"border: none;\n"
"font: 18pt \"LXGW WenKai TC\";")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(30, 147, 144, 32))
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"color: white;\n"
"font-weight: bold;\n"
"background-color: none;\n"
"border: none;\n"
"font: 18pt \"LXGW WenKai TC\";")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(30, 230, 95, 32))
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(u"color: white;\n"
"font-weight: bold;\n"
"background-color: none;\n"
"border: none;\n"
"font: 18pt \"LXGW WenKai TC\";")
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(30, 307, 203, 32))
        self.label_4.setFont(font)
        self.label_4.setStyleSheet(u"color: white;\n"
"font-weight: bold;\n"
"background-color: none;\n"
"border: none;\n"
"font:18pt \"LXGW WenKai TC\";")
        self.Text_Type = QTextEdit(self.centralwidget)
        self.Text_Type.setObjectName(u"Text_Type")
        self.Text_Type.setGeometry(QRect(90, 70, 201, 41))
        font1 = QFont()
        font1.setFamilies([u"LXGW WenKai TC"])
        font1.setPointSize(14)
        font1.setBold(False)
        font1.setItalic(False)
        self.Text_Type.setFont(font1)
        self.Text_Type.setStyleSheet(u"background-color: rgba(255, 255, 255, 30); \n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-radius: 7px;\n"
"color: white;\n"
"font: 14pt \"LXGW WenKai TC\";")
        self.Text_State = QTextEdit(self.centralwidget)
        self.Text_State.setObjectName(u"Text_State")
        self.Text_State.setGeometry(QRect(180, 150, 151, 41))
        self.Text_State.setFont(font1)
        self.Text_State.setStyleSheet(u"background-color: rgba(255, 255, 255, 30); \n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-radius: 7px;\n"
"color: white;\n"
"font: 14pt \"LXGW WenKai TC\";")
        self.PB_Add_Type = QPushButton(self.centralwidget)
        self.PB_Add_Type.setObjectName(u"PB_Add_Type")
        self.PB_Add_Type.setGeometry(QRect(530, 70, 91, 41))
        self.PB_Add_Type.setStyleSheet(u"background-color: rgba(255, 255, 255, 30); \n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-radius: 7px;\n"
"color: white;\n"
"font-weight: bold;\n"
"font: 10pt \"LXGW WenKai TC\";")
        self.PB_Dell_Type = QPushButton(self.centralwidget)
        self.PB_Dell_Type.setObjectName(u"PB_Dell_Type")
        self.PB_Dell_Type.setGeometry(QRect(640, 70, 91, 41))
        self.PB_Dell_Type.setStyleSheet(u"background-color: rgba(255, 255, 255, 30); \n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-radius: 7px;\n"
"color: white;\n"
"font-weight: bold;\n"
"font: 10pt \"LXGW WenKai TC\";")
        self.Text_Project = QTextEdit(self.centralwidget)
        self.Text_Project.setObjectName(u"Text_Project")
        self.Text_Project.setGeometry(QRect(140, 230, 191, 41))
        self.Text_Project.setFont(font1)
        self.Text_Project.setStyleSheet(u"background-color: rgba(255, 255, 255, 30); \n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-radius: 7px;\n"
"color: white;\n"
"font: 14pt \"LXGW WenKai TC\";")
        self.Text_Subdive = QTextEdit(self.centralwidget)
        self.Text_Subdive.setObjectName(u"Text_Subdive")
        self.Text_Subdive.setGeometry(QRect(240, 310, 151, 41))
        self.Text_Subdive.setFont(font1)
        self.Text_Subdive.setStyleSheet(u"background-color: rgba(255, 255, 255, 30); \n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-radius: 7px;\n"
"color: white;\n"
"font: 14pt \"LXGW WenKai TC\";")
        self.PB_Add_State = QPushButton(self.centralwidget)
        self.PB_Add_State.setObjectName(u"PB_Add_State")
        self.PB_Add_State.setGeometry(QRect(530, 150, 91, 41))
        self.PB_Add_State.setStyleSheet(u"background-color: rgba(255, 255, 255, 30); \n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-radius: 7px;\n"
"color: white;\n"
"font-weight: bold;\n"
"font: 10pt \"LXGW WenKai TC\";")
        self.PB_Dell_State = QPushButton(self.centralwidget)
        self.PB_Dell_State.setObjectName(u"PB_Dell_State")
        self.PB_Dell_State.setGeometry(QRect(640, 150, 91, 41))
        self.PB_Dell_State.setStyleSheet(u"background-color: rgba(255, 255, 255, 30); \n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-radius: 7px;\n"
"color: white;\n"
"font-weight: bold;\n"
"font: 10pt \"LXGW WenKai TC\";")
        self.PB_Dell_Project = QPushButton(self.centralwidget)
        self.PB_Dell_Project.setObjectName(u"PB_Dell_Project")
        self.PB_Dell_Project.setGeometry(QRect(640, 230, 91, 41))
        self.PB_Dell_Project.setStyleSheet(u"background-color: rgba(255, 255, 255, 30); \n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-radius: 7px;\n"
"color: white;\n"
"font-weight: bold;\n"
"font: 10pt \"LXGW WenKai TC\";")
        self.PB_Add_Project = QPushButton(self.centralwidget)
        self.PB_Add_Project.setObjectName(u"PB_Add_Project")
        self.PB_Add_Project.setGeometry(QRect(530, 230, 91, 41))
        self.PB_Add_Project.setStyleSheet(u"background-color: rgba(255, 255, 255, 30); \n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-radius: 7px;\n"
"color: white;\n"
"font-weight: bold;\n"
"font: 10pt \"LXGW WenKai TC\";")
        self.PB_Add_Sabdvide = QPushButton(self.centralwidget)
        self.PB_Add_Sabdvide.setObjectName(u"PB_Add_Sabdvide")
        self.PB_Add_Sabdvide.setGeometry(QRect(530, 310, 91, 41))
        self.PB_Add_Sabdvide.setStyleSheet(u"background-color: rgba(255, 255, 255, 30); \n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-radius: 7px;\n"
"color: white;\n"
"font-weight: bold;\n"
"font: 10pt \"LXGW WenKai TC\";")
        self.PB_Dell_Sabdvide = QPushButton(self.centralwidget)
        self.PB_Dell_Sabdvide.setObjectName(u"PB_Dell_Sabdvide")
        self.PB_Dell_Sabdvide.setGeometry(QRect(640, 310, 91, 41))
        self.PB_Dell_Sabdvide.setStyleSheet(u"background-color: rgba(255, 255, 255, 30); \n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-radius: 7px;\n"
"color: white;\n"
"font-weight: bold;\n"
"font: 10pt \"LXGW WenKai TC\";")
        self.Box_Type = QComboBox(self.centralwidget)
        self.Box_Type.setObjectName(u"Box_Type")
        self.Box_Type.setGeometry(QRect(300, 70, 221, 41))
        self.Box_Type.setStyleSheet(u"background-color: rgba(255, 255, 255, 30); \n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-radius: 7px;\n"
"\n"
"font-size: 16pt;\n"
"color: white;\n"
"\n"
"font: 14pt \"LXGW WenKai TC\";")
        self.Box_State = QComboBox(self.centralwidget)
        self.Box_State.setObjectName(u"Box_State")
        self.Box_State.setGeometry(QRect(340, 150, 181, 41))
        self.Box_State.setStyleSheet(u"background-color: rgba(255, 255, 255, 30); \n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-radius: 7px;\n"
"\n"
"font-size: 16pt;\n"
"color: white;\n"
"\n"
"font: 14pt \"LXGW WenKai TC\";")
        self.Box_Project = QComboBox(self.centralwidget)
        self.Box_Project.setObjectName(u"Box_Project")
        self.Box_Project.setGeometry(QRect(340, 230, 181, 41))
        self.Box_Project.setStyleSheet(u"background-color: rgba(255, 255, 255, 30); \n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-radius: 7px;\n"
"\n"
"font-size: 16pt;\n"
"color: white;\n"
"\n"
"font: 14pt \"LXGW WenKai TC\";")
        self.Box_Subdive = QComboBox(self.centralwidget)
        self.Box_Subdive.setObjectName(u"Box_Subdive")
        self.Box_Subdive.setGeometry(QRect(400, 310, 121, 41))
        self.Box_Subdive.setStyleSheet(u"background-color: rgba(255, 255, 255, 30); \n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-radius: 7px;\n"
"\n"
"font-size: 16pt;\n"
"color: white;\n"
"\n"
"font: 14pt \"LXGW WenKai TC\";")
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(210, 10, 351, 31))
        font2 = QFont()
        font2.setFamilies([u"LXGW WenKai TC"])
        font2.setPointSize(25)
        font2.setBold(False)
        font2.setItalic(False)
        self.label_5.setFont(font2)
        self.label_5.setStyleSheet(u"color: white;\n"
"font-weight: bold;\n"
"background-color: none;\n"
"border: none;\n"
"font: 25pt \"LXGW WenKai TC\";")
        self.new_transaction = QFrame(self.centralwidget)
        self.new_transaction.setObjectName(u"new_transaction")
        self.new_transaction.setGeometry(QRect(20, 10, 731, 361))
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
        self.label.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.Text_Type.raise_()
        self.Text_State.raise_()
        self.PB_Add_Type.raise_()
        self.PB_Dell_Type.raise_()
        self.Text_Project.raise_()
        self.Text_Subdive.raise_()
        self.PB_Add_State.raise_()
        self.PB_Dell_State.raise_()
        self.PB_Dell_Project.raise_()
        self.PB_Add_Project.raise_()
        self.PB_Add_Sabdvide.raise_()
        self.PB_Dell_Sabdvide.raise_()
        self.Box_Type.raise_()
        self.Box_State.raise_()
        self.Box_Project.raise_()
        self.Box_Subdive.raise_()
        self.label_5.raise_()
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 758, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Database_Setup", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0438\u043f:", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0441\u0442\u043e\u044f\u043d\u0438\u0435:", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u043e\u0435\u043a\u0442:", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0434\u0440\u0430\u0437\u0434\u0435\u043b\u0435\u043d\u0438\u0435:", None))
        self.PB_Add_Type.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.PB_Dell_Type.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
        self.PB_Add_State.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.PB_Dell_State.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
        self.PB_Dell_Project.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
        self.PB_Add_Project.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.PB_Add_Sabdvide.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.PB_Dell_Sabdvide.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0435\u0434\u0430\u043a\u0442\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u0435 \u0431\u0430\u0437\u044b \u0434\u0430\u043d\u043d\u044b\u0445", None))
    # retranslateUi

