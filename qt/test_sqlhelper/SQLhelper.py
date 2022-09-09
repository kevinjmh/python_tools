# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'SQLhelper.ui'
##
## Created by: Qt User Interface Compiler version 6.3.0
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
from PySide6.QtWidgets import (QApplication, QComboBox, QLabel, QLineEdit,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QTabWidget, QTextBrowser, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(887, 391)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.textBrowser = QTextBrowser(self.centralwidget)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setGeometry(QRect(10, 250, 791, 101))
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(0, 0, 891, 211))
        self.phoneTab = QWidget()
        self.phoneTab.setObjectName(u"phoneTab")
        self.lineEdit = QLineEdit(self.phoneTab)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(70, 20, 113, 20))
        self.label = QLabel(self.phoneTab)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 20, 61, 16))
        self.pushButton = QPushButton(self.phoneTab)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(460, 80, 111, 24))
        self.comboBox = QComboBox(self.phoneTab)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(50, 80, 311, 22))
        self.tabWidget.addTab(self.phoneTab, "")
        self.dimTab = QWidget()
        self.dimTab.setObjectName(u"dimTab")
        self.tabWidget.addTab(self.dimTab, "")
        self.AssetTab = QWidget()
        self.AssetTab.setObjectName(u"AssetTab")
        self.tabWidget.addTab(self.AssetTab, "")
        self.copy = QPushButton(self.centralwidget)
        self.copy.setObjectName(u"copy")
        self.copy.setGeometry(QRect(320, 220, 75, 24))
        self.clear = QPushButton(self.centralwidget)
        self.clear.setObjectName(u"clear")
        self.clear.setGeometry(QRect(420, 220, 75, 24))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 887, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.pushButton.clicked.connect(MainWindow.genSQL)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Phone", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Get ", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"tb_hcy_number_segment", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"satisfaction_blacklist", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"TotalSpace", None))

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.phoneTab), QCoreApplication.translate("MainWindow", u"User", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.dimTab), QCoreApplication.translate("MainWindow", u"Dim", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.AssetTab), QCoreApplication.translate("MainWindow", u"Asset", None))
        self.copy.setText(QCoreApplication.translate("MainWindow", u"Copy", None))
        self.clear.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
    # retranslateUi

