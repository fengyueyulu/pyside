# -*- coding: utf-8 -*-
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(390, 455)
        Form.setStyleSheet(u"background-color: rgb(0, 0, 127);")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 10, 371, 51))
        font = QFont()
        font.setFamily(u"\u5fae\u8f6f\u96c5\u9ed1")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label.setAlignment(Qt.AlignCenter)
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(50, 110, 72, 30))
        font1 = QFont()
        font1.setFamily(u"\u5fae\u8f6f\u96c5\u9ed1")
        font1.setPointSize(14)
        font1.setBold(True)
        font1.setWeight(75)
        self.label_2.setFont(font1)
        self.label_2.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(50, 200, 72, 30))
        self.label_3.setFont(font1)
        self.label_3.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_4 = QLabel(Form)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(50, 290, 72, 30))
        self.label_4.setFont(font1)
        self.label_4.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_4.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.temprature_lcd = QLCDNumber(Form)
        self.temprature_lcd.setObjectName(u"temprature_lcd")
        self.temprature_lcd.setGeometry(QRect(130, 90, 121, 71))
        self.temprature_lcd.setStyleSheet(u"border: 1px solid white;\n"
"color: rgb(255, 255, 255);")
        self.humidity_lcd = QLCDNumber(Form)
        self.humidity_lcd.setObjectName(u"humidity_lcd")
        self.humidity_lcd.setGeometry(QRect(130, 180, 121, 71))
        self.humidity_lcd.setStyleSheet(u"border: 1px solid white;\n"
"color: rgb(255, 255, 255);")
        self.ch4_lcd = QLCDNumber(Form)
        self.ch4_lcd.setObjectName(u"ch4_lcd")
        self.ch4_lcd.setGeometry(QRect(130, 270, 121, 71))
        self.ch4_lcd.setStyleSheet(u"border: 1px solid white;\n"
"color: rgb(255, 255, 255);")
        self.label_5 = QLabel(Form)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(260, 110, 71, 30))
        font2 = QFont()
        font2.setFamily(u"\u5fae\u8f6f\u96c5\u9ed1")
        font2.setPointSize(12)
        font2.setBold(True)
        font2.setWeight(75)
        self.label_5.setFont(font2)
        self.label_5.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_5.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_6 = QLabel(Form)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(260, 200, 71, 30))
        self.label_6.setFont(font2)
        self.label_6.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_6.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_7 = QLabel(Form)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(260, 290, 71, 30))
        self.label_7.setFont(font2)
        self.label_7.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_7.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.search_btn = QPushButton(Form)
        self.search_btn.setObjectName(u"search_btn")
        self.search_btn.setGeometry(QRect(20, 380, 161, 51))
        self.search_btn.setFont(font1)
        self.search_btn.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(26, 143, 125);\n"
"	border: 1px solid white;\n"
"	border-radius: 10px;\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: red;\n"
"}")
        self.line_2 = QFrame(Form)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setGeometry(QRect(10, 360, 371, 3))
        self.line_2.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)
        self.line_3 = QFrame(Form)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setGeometry(QRect(130, 260, 118, 3))
        self.line_3.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)
        self.line_4 = QFrame(Form)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setGeometry(QRect(130, 170, 118, 3))
        self.line_4.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.line_4.setFrameShape(QFrame.HLine)
        self.line_4.setFrameShadow(QFrame.Sunken)
        self.line = QFrame(Form)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(5, 70, 381, 3))
        self.line.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.jump_btn = QPushButton(Form)
        self.jump_btn.setObjectName(u"jump_btn")
        self.jump_btn.setGeometry(QRect(210, 380, 161, 51))
        self.jump_btn.setFont(font1)
        self.jump_btn.setStyleSheet(u"QPushButton {\n"
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
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\u5ba4\u5185\u73af\u5883\u76d1\u6d4b\u7cfb\u7edf", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u5ba4\u5185\u73af\u5883\u76d1\u6d4b\u7cfb\u7edf", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u6e29\u5ea6\uff1a", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"\u6e7f\u5ea6\uff1a", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"\u7532\u70f7\uff1a", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"\u2103", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"%RH", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"m\u00b3/g", None))
        self.search_btn.setText(QCoreApplication.translate("Form", u"\u73af\u5883\u8bb0\u5f55", None))
        self.jump_btn.setText(QCoreApplication.translate("Form", u"\u5ba4\u5185\u63a7\u5236", None))
    # retranslateUi

