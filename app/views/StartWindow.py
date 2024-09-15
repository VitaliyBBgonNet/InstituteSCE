from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QVBoxLayout, QWidget)

class StartWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(500, 401)
        MainWindow.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(81, 0, 135, 255), stop:0.427447 rgba(41, 61, 132, 235), stop:1 rgba(155, 79, 165, 255));\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(40, 20, 431, 31))
        font = QFont()
        font.setFamilies([u"LXGW WenKai TC"])
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        self.label.setFont(font)
        self.label.setStyleSheet(u"color: white;\n"
"font-weight: bold;\n"
"font: 20pt \"LXGW WenKai TC\";\n"
"background-color: none;\n"
"border: none;")
        self.PB_Add_Element = QPushButton(self.centralwidget)
        self.PB_Add_Element.setObjectName(u"PB_Add_Element")
        self.PB_Add_Element.setGeometry(QRect(50, 210, 401, 61))
        self.PB_Add_Element.setStyleSheet(u"background-color: rgba(255, 255, 255, 30); \n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-radius: 7px;\n"
"color: white;\n"
"font-weight: bold;\n"
"font: 14pt \"LXGW WenKai TC\";")
        self.PB_Info = QPushButton(self.centralwidget)
        self.PB_Info.setObjectName(u"PB_Info")
        self.PB_Info.setGeometry(QRect(50, 70, 401, 61))
        self.PB_Info.setStyleSheet(u"background-color: rgba(255, 255, 255, 30); \n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-radius: 7px;\n"
"color: white;\n"
"font-weight: bold;\n"
"font: 14pt \"LXGW WenKai TC\";")
        self.PB_Arenda = QPushButton(self.centralwidget)
        self.PB_Arenda.setObjectName(u"PB_Arenda")
        self.PB_Arenda.setGeometry(QRect(50, 140, 401, 61))
        self.PB_Arenda.setStyleSheet(u"background-color: rgba(255, 255, 255, 30); \n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-radius: 7px;\n"
"color: white;\n"
"font-weight: bold;\n"
"font: 14pt \"LXGW WenKai TC\";")
        self.PB_QR = QPushButton(self.centralwidget)
        self.PB_QR.setObjectName(u"PB_QR")
        self.PB_QR.setGeometry(QRect(50, 280, 401, 61))
        self.PB_QR.setStyleSheet(u"background-color: rgba(255, 255, 255, 30); \n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-radius: 7px;\n"
"color: white;\n"
"font-weight: bold;\n"
"font: 14pt \"LXGW WenKai TC\";")
        self.new_transaction = QFrame(self.centralwidget)
        self.new_transaction.setObjectName(u"new_transaction")
        self.new_transaction.setGeometry(QRect(20, 10, 461, 341))
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
        self.PB_Add_Element.raise_()
        self.PB_Info.raise_()
        self.PB_Arenda.raise_()
        self.PB_QR.raise_()
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 500, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u043e\u0435\u043a\u0442\u043d\u0430\u044f \u0434\u0435\u044f\u0442\u0435\u043b\u044c\u043d\u043e\u0441\u0442\u044c \u0418\u0420\u0422\u0421\u0423", None))
        self.PB_Add_Element.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u042d\u043b\u0435\u043c\u0435\u043d\u0442", None))
        self.PB_Info.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0435\u0434\u0430\u043a\u0442\u0438\u0440\u043e\u0432\u0430\u0442\u044c \u0411\u0414", None))
        self.PB_Arenda.setText(QCoreApplication.translate("MainWindow", u"\u0418\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044f", None))
        self.PB_QR.setText(QCoreApplication.translate("MainWindow", u"QR", None))
    # retranslateUi

