# -*- coding: utf-8 -*-
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(400, 548)
        Form.setStyleSheet(u"background-color: rgb(0, 0, 127);")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(40, 30, 171, 51))
        font = QFont()
        font.setFamily(u"\u5fae\u8f6f\u96c5\u9ed1")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet(u"border: 1px solid #ffffff;\n"
"color: rgb(255, 255, 255);")
        self.label.setAlignment(Qt.AlignCenter)
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(40, 120, 171, 51))
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"border: 1px solid #ffffff;\n"
"color: rgb(255, 255, 255);")
        self.label_2.setAlignment(Qt.AlignCenter)
        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(40, 210, 171, 51))
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(u"border: 1px solid #ffffff;\n"
"color: rgb(255, 255, 255);")
        self.label_3.setAlignment(Qt.AlignCenter)
        self.label_4 = QLabel(Form)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(40, 300, 171, 51))
        self.label_4.setFont(font)
        self.label_4.setStyleSheet(u"border: 1px solid #ffffff;\n"
"color: rgb(255, 255, 255);")
        self.label_4.setAlignment(Qt.AlignCenter)
        self.label_5 = QLabel(Form)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(40, 390, 171, 51))
        self.label_5.setFont(font)
        self.label_5.setStyleSheet(u"border: 1px solid #ffffff;\n"
"color: rgb(255, 255, 255);")
        self.label_5.setAlignment(Qt.AlignCenter)
        self.pushButton_1 = QPushButton(Form)
        self.pushButton_1.setObjectName(u"pushButton_1")
        self.pushButton_1.setGeometry(QRect(240, 30, 121, 51))
        self.pushButton_1.setFont(font)
        self.pushButton_1.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(26, 143, 125);\n"
"	border: 1px solid white;\n"
"	border-radius: 10px;\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: red;\n"
"}")
        self.pushButton_2 = QPushButton(Form)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(240, 120, 121, 51))
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(26, 143, 125);\n"
"	border: 1px solid white;\n"
"	border-radius: 10px;\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: red;\n"
"}")
        self.pushButton_3 = QPushButton(Form)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(240, 210, 121, 51))
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(26, 143, 125);\n"
"	border: 1px solid white;\n"
"	border-radius: 10px;\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: red;\n"
"}")
        self.pushButton_4 = QPushButton(Form)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(240, 300, 121, 51))
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(26, 143, 125);\n"
"	border: 1px solid white;\n"
"	border-radius: 10px;\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: red;\n"
"}")
        self.pushButton_5 = QPushButton(Form)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QRect(240, 390, 121, 51))
        self.pushButton_5.setFont(font)
        self.pushButton_5.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(26, 143, 125);\n"
"	border: 1px solid white;\n"
"	border-radius: 10px;\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: red;\n"
"}")
        self.line = QFrame(Form)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(40, 100, 321, 3))
        self.line.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.line_2 = QFrame(Form)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setGeometry(QRect(40, 190, 321, 3))
        self.line_2.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)
        self.line_3 = QFrame(Form)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setGeometry(QRect(40, 280, 321, 3))
        self.line_3.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)
        self.line_4 = QFrame(Form)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setGeometry(QRect(40, 370, 321, 3))
        self.line_4.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.line_4.setFrameShape(QFrame.HLine)
        self.line_4.setFrameShadow(QFrame.Sunken)
        self.line_5 = QFrame(Form)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setGeometry(QRect(40, 450, 321, 3))
        self.line_5.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.line_5.setFrameShape(QFrame.HLine)
        self.line_5.setFrameShadow(QFrame.Sunken)
        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(40, 470, 151, 61))
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(26, 143, 125);\n"
"	border: 1px solid white;\n"
"	border-radius: 10px;\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: red;\n"
"}")
        self.pushButton_6 = QPushButton(Form)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setGeometry(QRect(220, 470, 141, 61))
        self.pushButton_6.setFont(font)
        self.pushButton_6.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(26, 143, 125);\n"
"	border: 1px solid white;\n"
"	border-radius: 10px;\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: red;\n"
"}")

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\u5ba4\u5185\u73af\u5883\u68c0\u6d4b\u7cfb\u7edf-\u5ba4\u5185\u63a7\u5236", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u7a7a\u6c14\u51c0\u5316\u5668\u72b6\u6001\uff1a", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u7a97\u72b6\u6001\uff1a", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"\u52a0\u6e7f\u5668\u72b6\u6001\uff1a", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"\u7a7a\u8c03\u72b6\u6001\uff1a", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"\u98ce\u6247\u72b6\u6001\uff1a", None))
        self.pushButton_1.setText(QCoreApplication.translate("Form", u"\u5173", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"\u5173", None))
        self.pushButton_3.setText(QCoreApplication.translate("Form", u"\u5173", None))
        self.pushButton_4.setText(QCoreApplication.translate("Form", u"\u5173", None))
        self.pushButton_5.setText(QCoreApplication.translate("Form", u"\u5173", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"\u4e3b\u754c\u9762", None))
        self.pushButton_6.setText(QCoreApplication.translate("Form", u"\u73af\u5883\u8bb0\u5f55", None))
    # retranslateUi

