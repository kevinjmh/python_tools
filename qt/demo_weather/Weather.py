# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Weather.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QGroupBox,
    QLabel, QPushButton, QSizePolicy, QTextEdit,
    QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(400, 300)
        self.queryButton = QPushButton(Dialog)
        self.queryButton.setObjectName(u"queryButton")
        self.queryButton.setGeometry(QRect(100, 240, 75, 24))
        self.clearButton = QPushButton(Dialog)
        self.clearButton.setObjectName(u"clearButton")
        self.clearButton.setGeometry(QRect(210, 240, 75, 24))
        self.groupBox = QGroupBox(Dialog)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(10, 20, 371, 201))
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 30, 51, 16))
        self.comboBox = QComboBox(self.groupBox)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(100, 30, 68, 22))
        self.textEdit = QTextEdit(self.groupBox)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(30, 60, 311, 131))

        self.retranslateUi(Dialog)
        self.queryButton.clicked.connect(Dialog.queryWeather)
        self.clearButton.clicked.connect(Dialog.clearText)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.queryButton.setText(QCoreApplication.translate("Dialog", u"Query", None))
        self.clearButton.setText(QCoreApplication.translate("Dialog", u"Clear", None))
        self.groupBox.setTitle(QCoreApplication.translate("Dialog", u"city weather", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"City", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("Dialog", u"\u5317\u4eac", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("Dialog", u"\u4e0a\u6d77", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("Dialog", u"\u5929\u6d25", None))

    # retranslateUi

