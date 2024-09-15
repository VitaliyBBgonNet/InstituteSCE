
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QFrame,
    QLabel, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QStatusBar, QTextEdit, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(575, 789)
        MainWindow.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(81, 0, 135, 255), stop:0.427447 rgba(41, 61, 132, 235), stop:1 rgba(155, 79, 165, 255));\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(200, 20, 221, 51))
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamilies([u"LXGW WenKai TC"])
        font.setPointSize(25)
        font.setBold(False)
        font.setItalic(False)
        self.label.setFont(font)
        self.label.setStyleSheet(u"color: white;\n"
"font-weight: bold;\n"
"font: 25pt \"LXGW WenKai TC\";\n"
"background-color: none;\n"
"border: none;")
        self.text_id_object = QTextEdit(self.centralwidget)
        self.text_id_object.setObjectName(u"text_id_object")
        self.text_id_object.setGeometry(QRect(80, 110, 351, 41))
        font1 = QFont()
        font1.setFamilies([u"LXGW WenKai TC"])
        font1.setPointSize(14)
        font1.setBold(False)
        font1.setItalic(False)
        self.text_id_object.setFont(font1)
        self.text_id_object.setAcceptDrops(True)
        self.text_id_object.setStyleSheet(u"background-color: rgba(255, 255, 255, 30); \n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-radius: 7px;\n"
"color: white;\n"
"font: 14pt \"LXGW WenKai TC\";")
        self.Labe_Name_2 = QLabel(self.centralwidget)
        self.Labe_Name_2.setObjectName(u"Labe_Name_2")
        self.Labe_Name_2.setGeometry(QRect(40, 110, 41, 31))
        font2 = QFont()
        font2.setFamilies([u"LXGW WenKai TC"])
        font2.setPointSize(14)
        font2.setBold(False)
        self.Labe_Name_2.setFont(font2)
        self.Labe_Name_2.setStyleSheet(u"color: white;\n"
"font-weight: bold;\n"
"background-color: none;\n"
"border: none;\n"
"font: 14pt \"LXGW WenKai TC\";")
        self.Labe_Name_3 = QLabel(self.centralwidget)
        self.Labe_Name_3.setObjectName(u"Labe_Name_3")
        self.Labe_Name_3.setGeometry(QRect(40, 160, 141, 23))
        self.Labe_Name_3.setFont(font2)
        self.Labe_Name_3.setStyleSheet(u"color: white;\n"
"font-weight: bold;\n"
"background-color: none;\n"
"border: none;\n"
"font: 14pt \"LXGW WenKai TC\";\n"
"")
        self.text_name_object = QTextEdit(self.centralwidget)
        self.text_name_object.setObjectName(u"text_name_object")
        self.text_name_object.setGeometry(QRect(190, 160, 351, 41))
        self.text_name_object.setFont(font1)
        self.text_name_object.setAcceptDrops(True)
        self.text_name_object.setStyleSheet(u"background-color: rgba(255, 255, 255, 30); \n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-radius: 7px;\n"
"color: white;\n"
"font: 14pt \"LXGW WenKai TC\";")
        self.Labe_Name_4 = QLabel(self.centralwidget)
        self.Labe_Name_4.setObjectName(u"Labe_Name_4")
        self.Labe_Name_4.setGeometry(QRect(40, 210, 41, 23))
        self.Labe_Name_4.setFont(font1)
        self.Labe_Name_4.setStyleSheet(u"color: white;\n"
"font-weight: bold;\n"
"background-color: none;\n"
"border: none;\n"
"font: 14pt \"LXGW WenKai TC\";")
        self.Box_object_type = QComboBox(self.centralwidget)
        self.Box_object_type.setObjectName(u"Box_object_type")
        self.Box_object_type.setGeometry(QRect(100, 210, 441, 31))
        self.Box_object_type.setStyleSheet(u"background-color: rgba(255, 255, 255, 30); \n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-radius: 7px;\n"
"\n"
"font-size: 16pt;\n"
"color: white;\n"
"\n"
"font: 14pt \"LXGW WenKai TC\";")
        self.Box_object_State = QComboBox(self.centralwidget)
        self.Box_object_State.setObjectName(u"Box_object_State")
        self.Box_object_State.setGeometry(QRect(150, 260, 391, 31))
        self.Box_object_State.setStyleSheet(u"background-color: rgba(255, 255, 255, 30); \n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-radius: 7px;\n"
"color: white;\n"
"font: 14pt \"LXGW WenKai TC\";")
        self.Labe_Name_5 = QLabel(self.centralwidget)
        self.Labe_Name_5.setObjectName(u"Labe_Name_5")
        self.Labe_Name_5.setGeometry(QRect(40, 260, 101, 23))
        self.Labe_Name_5.setFont(font1)
        self.Labe_Name_5.setStyleSheet(u"color: white;\n"
"font-weight: bold;\n"
"background-color: none;\n"
"border: none;\n"
"font: 14pt \"LXGW WenKai TC\";")
        self.Labe_Name_6 = QLabel(self.centralwidget)
        self.Labe_Name_6.setObjectName(u"Labe_Name_6")
        self.Labe_Name_6.setGeometry(QRect(40, 310, 71, 23))
        self.Labe_Name_6.setFont(font1)
        self.Labe_Name_6.setStyleSheet(u"color: white;\n"
"font-weight: bold;\n"
"background-color: none;\n"
"border: none;\n"
"font: 14pt \"LXGW WenKai TC\";")
        self.Box_object_project = QComboBox(self.centralwidget)
        self.Box_object_project.setObjectName(u"Box_object_project")
        self.Box_object_project.setGeometry(QRect(120, 300, 421, 31))
        self.Box_object_project.setStyleSheet(u"background-color: rgba(255, 255, 255, 30); \n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-radius: 7px;\n"
"color: white;\n"
"font: 14pt \"LXGW WenKai TC\";")
        self.Labe_Name_7 = QLabel(self.centralwidget)
        self.Labe_Name_7.setObjectName(u"Labe_Name_7")
        self.Labe_Name_7.setGeometry(QRect(40, 350, 151, 23))
        self.Labe_Name_7.setFont(font1)
        self.Labe_Name_7.setStyleSheet(u"color: white;\n"
"font-weight: bold;\n"
"background-color: none;\n"
"border: none;\n"
"font: 14pt \"LXGW WenKai TC\";")
        self.Box_object_subdive = QComboBox(self.centralwidget)
        self.Box_object_subdive.setObjectName(u"Box_object_subdive")
        self.Box_object_subdive.setGeometry(QRect(200, 350, 341, 31))
        self.Box_object_subdive.setStyleSheet(u"background-color: rgba(255, 255, 255, 30); \n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-radius: 7px;\n"
"color: white;\n"
"font: 14pt \"LXGW WenKai TC\";")
        self.Labe_Name_8 = QLabel(self.centralwidget)
        self.Labe_Name_8.setObjectName(u"Labe_Name_8")
        self.Labe_Name_8.setGeometry(QRect(40, 400, 61, 23))
        self.Labe_Name_8.setFont(font1)
        self.Labe_Name_8.setStyleSheet(u"color: white;\n"
"font-weight: bold;\n"
"background-color: none;\n"
"border: none;\n"
"font: 14pt \"LXGW WenKai TC\";")
        self.Labe_Name_9 = QLabel(self.centralwidget)
        self.Labe_Name_9.setObjectName(u"Labe_Name_9")
        self.Labe_Name_9.setGeometry(QRect(40, 450, 51, 23))
        self.Labe_Name_9.setFont(font1)
        self.Labe_Name_9.setStyleSheet(u"color: white;\n"
"font-weight: bold;\n"
"background-color: none;\n"
"border: none;\n"
"font: 14pt \"LXGW WenKai TC\";")
        self.dateEdit_time = QDateEdit(self.centralwidget)
        self.dateEdit_time.setObjectName(u"dateEdit_time")
        self.dateEdit_time.setGeometry(QRect(120, 450, 421, 31))
        self.dateEdit_time.setStyleSheet(u"background-color: rgba(255, 255, 255, 30); \n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-radius: 7px;\n"
"color: white;\n"
"font: 14pt \"LXGW WenKai TC\";")
        self.Labe_Name_10 = QLabel(self.centralwidget)
        self.Labe_Name_10.setObjectName(u"Labe_Name_10")
        self.Labe_Name_10.setGeometry(QRect(40, 500, 121, 23))
        self.Labe_Name_10.setFont(font1)
        self.Labe_Name_10.setStyleSheet(u"color: white;\n"
"font-weight: bold;\n"
"background-color: none;\n"
"border: none;\n"
"font: 14pt \"LXGW WenKai TC\";")
        self.Text_Name_3 = QTextEdit(self.centralwidget)
        self.Text_Name_3.setObjectName(u"Text_Name_3")
        self.Text_Name_3.setGeometry(QRect(40, 540, 501, 81))
        self.Text_Name_3.setFont(font1)
        self.Text_Name_3.setAcceptDrops(True)
        self.Text_Name_3.setStyleSheet(u"background-color: rgba(255, 255, 255, 30); \n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-radius: 7px;\n"
"color: white;\n"
"font: 14pt \"LXGW WenKai TC\";")
        self.PB_Add_ELEMENT_2 = QPushButton(self.centralwidget)
        self.PB_Add_ELEMENT_2.setObjectName(u"PB_Add_ELEMENT_2")
        self.PB_Add_ELEMENT_2.setGeometry(QRect(190, 640, 241, 61))
        self.PB_Add_ELEMENT_2.setFont(font1)
        self.PB_Add_ELEMENT_2.setStyleSheet(u"background-color: rgba(255, 255, 255, 30); \n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-radius: 7px;\n"
"color: white;\n"
"font-weight: bold;\n"
"font: 14pt \"LXGW WenKai TC\";")
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(440, 110, 51, 41))
        self.pushButton.setStyleSheet(u"background-color: rgba(255, 255, 255, 30); \n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-radius: 7px;\n"
"color: white;\n"
"font-weight: bold;\n"
"font: 10pt \"LXGW WenKai TC\";")
        self.Box_object_fio = QTextEdit(self.centralwidget)
        self.Box_object_fio.setObjectName(u"Box_object_fio")
        self.Box_object_fio.setGeometry(QRect(120, 400, 421, 41))
        self.Box_object_fio.setFont(font1)
        self.Box_object_fio.setAcceptDrops(True)
        self.Box_object_fio.setStyleSheet(u"background-color: rgba(255, 255, 255, 30); \n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-radius: 7px;\n"
"color: white;\n"
"font: 14pt \"LXGW WenKai TC\";")
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(500, 110, 51, 41))
        self.pushButton_2.setStyleSheet(u"background-color: rgba(255, 255, 255, 30); \n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-radius: 7px;\n"
"color: white;\n"
"font-weight: bold;\n"
"font: 10pt \"LXGW WenKai TC\";")
        self.new_transaction = QFrame(self.centralwidget)
        self.new_transaction.setObjectName(u"new_transaction")
        self.new_transaction.setGeometry(QRect(20, 10, 541, 731))
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
        self.text_id_object.raise_()
        self.Labe_Name_2.raise_()
        self.Labe_Name_3.raise_()
        self.text_name_object.raise_()
        self.Labe_Name_4.raise_()
        self.Box_object_type.raise_()
        self.Box_object_State.raise_()
        self.Labe_Name_5.raise_()
        self.Labe_Name_6.raise_()
        self.Box_object_project.raise_()
        self.Labe_Name_7.raise_()
        self.Box_object_subdive.raise_()
        self.Labe_Name_8.raise_()
        self.Labe_Name_9.raise_()
        self.dateEdit_time.raise_()
        self.Labe_Name_10.raise_()
        self.Text_Name_3.raise_()
        self.PB_Add_ELEMENT_2.raise_()
        self.pushButton.raise_()
        self.Box_object_fio.raise_()
        self.pushButton_2.raise_()
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 575, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u0418\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044f", None))
        self.Labe_Name_2.setText(QCoreApplication.translate("MainWindow", u"ID:", None))
        self.Labe_Name_3.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0438\u043c\u0435\u043d\u043e\u0432\u0430\u043d\u0438\u0435:", None))
        self.Labe_Name_4.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0438\u043f:", None))
        self.Labe_Name_5.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0441\u0442\u043e\u044f\u043d\u0438\u0435:", None))
        self.Labe_Name_6.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u043e\u0435\u043a\u0442:", None))
        self.Labe_Name_7.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0434\u0440\u0430\u0437\u0434\u0435\u043b\u0435\u043d\u0438\u0435:", None))
        self.Labe_Name_8.setText(QCoreApplication.translate("MainWindow", u"\u0424.\u0418.\u041e.", None))
        self.Labe_Name_9.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0430\u0442\u0430:", None))
        self.Labe_Name_10.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0438\u043c\u0435\u0447\u0430\u043d\u0438\u0435:", None))
        self.PB_Add_ELEMENT_2.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0434\u0442\u0432\u0435\u0440\u0434\u0438\u0442\u044c \u0438\u0437\u043c\u0435\u043d\u0435\u043d\u0438\u044f ", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0438\u0441\u043a", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043a\u0430\u043d\u0435\u0440", None))
    # retranslateUi

