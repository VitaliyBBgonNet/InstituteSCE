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
        MainWindow.resize(1532, 812)
        MainWindow.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(81, 0, 135, 255), stop:0.427447 rgba(41, 61, 132, 235), stop:1 rgba(155, 79, 165, 255));\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(1210, 120, 51, 16))
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
        self.PB_GenerateQR_2 = QPushButton(self.centralwidget)
        self.PB_GenerateQR_2.setObjectName(u"PB_GenerateQR_2")
        self.PB_GenerateQR_2.setGeometry(QRect(1210, 380, 301, 51))
        self.PB_GenerateQR_2.setStyleSheet(u"background-color: rgba(255, 255, 255, 30); \n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-radius: 7px;\n"
"color: white;\n"
"font-weight: bold;\n"
"font: 14pt \"LXGW WenKai TC\";")
        self.PB_GenerateQR = QPushButton(self.centralwidget)
        self.PB_GenerateQR.setObjectName(u"PB_GenerateQR")
        self.PB_GenerateQR.setGeometry(QRect(1210, 220, 301, 51))
        self.PB_GenerateQR.setStyleSheet(u"background-color: rgba(255, 255, 255, 30); \n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-radius: 7px;\n"
"color: white;\n"
"font-weight: bold;\n"
"font: 14pt \"LXGW WenKai TC\";")
        self.comboBox = QComboBox(self.centralwidget)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(1250, 120, 261, 31))
        self.comboBox.setStyleSheet(u"background-color: rgba(255, 255, 255, 30); \n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-radius: 7px;\n"
"\n"
"font-size: 16pt;\n"
"color: white;\n"
"\n"
"font: 14pt \"LXGW WenKai TC\";")
        self.PB_GenerateQR_3 = QPushButton(self.centralwidget)
        self.PB_GenerateQR_3.setObjectName(u"PB_GenerateQR_3")
        self.PB_GenerateQR_3.setGeometry(QRect(1210, 280, 301, 41))
        self.PB_GenerateQR_3.setStyleSheet(u"background-color: rgba(255, 255, 255, 30); \n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-radius: 7px;\n"
"color: white;\n"
"font-weight: bold;\n"
"font: 14pt \"LXGW WenKai TC\";")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(1210, 330, 51, 31))
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(u"color: white;\n"
"font-weight: bold;\n"
"background-color: none;\n"
"border: none;\n"
"font: 14pt \"LXGW WenKai TC\";")
        self.textEdit = QTextEdit(self.centralwidget)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(1260, 70, 251, 41))
        self.textEdit.setStyleSheet(u"background-color: rgba(255, 255, 255, 30); \n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-radius: 7px;\n"
"color: white;\n"
"font: 14pt \"LXGW WenKai TC\";")
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(1210, 70, 51, 16))
        self.label_4.setFont(font)
        self.label_4.setStyleSheet(u"color: white;\n"
"font-weight: bold;\n"
"background-color: none;\n"
"border: none;\n"
"font: 14pt \"LXGW WenKai TC\";")
        self.textEdit_2 = QTextEdit(self.centralwidget)
        self.textEdit_2.setObjectName(u"textEdit_2")
        self.textEdit_2.setGeometry(QRect(1260, 330, 201, 41))
        self.textEdit_2.setStyleSheet(u"background-color: rgba(255, 255, 255, 30); \n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-radius: 7px;\n"
"color: white;\n"
"font: 14pt \"LXGW WenKai TC\";")
        self.PB_GenerateQR_4 = QPushButton(self.centralwidget)
        self.PB_GenerateQR_4.setObjectName(u"PB_GenerateQR_4")
        self.PB_GenerateQR_4.setGeometry(QRect(1470, 330, 41, 41))
        self.PB_GenerateQR_4.setStyleSheet(u"background-color: rgba(255, 255, 255, 30); \n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-radius: 7px;\n"
"color: white;\n"
"font-weight: bold;\n"
"font: 14pt \"LXGW WenKai TC\";")
        self.tableWidget = QTableWidget(self.centralwidget)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(20, 70, 1181, 641))
        self.tableWidget.setStyleSheet(u"QTableView {\n"
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
        self.tableWidget.setShowGrid(False)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(120)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(150)
        self.tableWidget.horizontalHeader().setHighlightSections(True)
        self.tableWidget.horizontalHeader().setProperty("showSortIndicator", False)
        self.tableWidget.horizontalHeader().setStretchLastSection(False)
        self.tableWidget.verticalHeader().setProperty("showSortIndicator", False)
        self.new_transaction = QFrame(self.centralwidget)
        self.new_transaction.setObjectName(u"new_transaction")
        self.new_transaction.setGeometry(QRect(10, 10, 1511, 751))
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
        self.label.setGeometry(QRect(530, 0, 241, 71))
        self.label.setStyleSheet(u"color: white;\n"
"font-weight: bold;\n"
"background-color: none;\n"
"border: none;\n"
"font: 25pt \"LXGW WenKai TC\";")
        self.textEdit_3 = QTextEdit(self.centralwidget)
        self.textEdit_3.setObjectName(u"textEdit_3")
        self.textEdit_3.setGeometry(QRect(1280, 170, 231, 41))
        self.textEdit_3.setStyleSheet(u"background-color: rgba(255, 255, 255, 30); \n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-radius: 7px;\n"
"color: white;\n"
"font: 14pt \"LXGW WenKai TC\";")
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(1210, 180, 61, 16))
        self.label_5.setFont(font)
        self.label_5.setStyleSheet(u"color: white;\n"
"font-weight: bold;\n"
"background-color: none;\n"
"border: none;\n"
"font: 14pt \"LXGW WenKai TC\";")
        MainWindow.setCentralWidget(self.centralwidget)
        self.new_transaction.raise_()
        self.label_2.raise_()
        self.PB_GenerateQR_2.raise_()
        self.PB_GenerateQR.raise_()
        self.comboBox.raise_()
        self.PB_GenerateQR_3.raise_()
        self.label_3.raise_()
        self.textEdit.raise_()
        self.label_4.raise_()
        self.textEdit_2.raise_()
        self.PB_GenerateQR_4.raise_()
        self.tableWidget.raise_()
        self.label.raise_()
        self.textEdit_3.raise_()
        self.label_5.raise_()
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1532, 21))
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
        self.PB_GenerateQR_2.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0437\u0434\u0430\u0442\u044c QR", None))
        self.PB_GenerateQR.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0438\u0441\u043a", None))
        self.PB_GenerateQR_3.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0447\u0438\u0441\u0442\u0438\u0442\u044c", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0443\u0442\u044c:", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u0418\u043c\u044f:", None))
        self.PB_GenerateQR_4.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u0413\u0435\u043d\u0435\u0440\u0430\u0446\u0438\u044f QR", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u0424.\u0418.\u041e.", None))
    # retranslateUi

