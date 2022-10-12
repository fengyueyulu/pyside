# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'home3System.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(422, 544)
        Form.setStyleSheet(u"background-color: rgb(0, 0, 127);")
        self.home3_label = QLabel(Form)
        self.home3_label.setObjectName(u"home3_label")
        self.home3_label.setGeometry(QRect(10, 10, 371, 51))
        font = QFont()
        font.setFamily(u"\u5fae\u8f6f\u96c5\u9ed1")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.home3_label.setFont(font)
        self.home3_label.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.home3_label.setAlignment(Qt.AlignCenter)
        self.home3_label_2 = QLabel(Form)
        self.home3_label_2.setObjectName(u"home3_label_2")
        self.home3_label_2.setGeometry(QRect(70, 90, 72, 30))
        font1 = QFont()
        font1.setFamily(u"\u5fae\u8f6f\u96c5\u9ed1")
        font1.setPointSize(14)
        font1.setBold(True)
        font1.setWeight(75)
        self.home3_label_2.setFont(font1)
        self.home3_label_2.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.home3_label_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.home3_label_3 = QLabel(Form)
        self.home3_label_3.setObjectName(u"home3_label_3")
        self.home3_label_3.setGeometry(QRect(70, 170, 72, 30))
        self.home3_label_3.setFont(font1)
        self.home3_label_3.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.home3_label_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.home3_label_4 = QLabel(Form)
        self.home3_label_4.setObjectName(u"home3_label_4")
        self.home3_label_4.setGeometry(QRect(70, 250, 72, 30))
        self.home3_label_4.setFont(font1)
        self.home3_label_4.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.home3_label_4.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.temprature_lcd = QLCDNumber(Form)
        self.temprature_lcd.setObjectName(u"temprature_lcd")
        self.temprature_lcd.setGeometry(QRect(150, 80, 121, 51))
        self.temprature_lcd.setStyleSheet(u"border: 1px solid white;\n"
"color: rgb(255, 255, 255);")
        self.humidity_lcd = QLCDNumber(Form)
        self.humidity_lcd.setObjectName(u"humidity_lcd")
        self.humidity_lcd.setGeometry(QRect(150, 160, 121, 51))
        self.humidity_lcd.setStyleSheet(u"border: 1px solid white;\n"
"color: rgb(255, 255, 255);")
        self.ch4_lcd = QLCDNumber(Form)
        self.ch4_lcd.setObjectName(u"ch4_lcd")
        self.ch4_lcd.setGeometry(QRect(150, 240, 121, 51))
        self.ch4_lcd.setStyleSheet(u"border: 1px solid white;\n"
"color: rgb(255, 255, 255);")
        self.home3_label_5 = QLabel(Form)
        self.home3_label_5.setObjectName(u"home3_label_5")
        self.home3_label_5.setGeometry(QRect(280, 100, 71, 30))
        font2 = QFont()
        font2.setFamily(u"\u5fae\u8f6f\u96c5\u9ed1")
        font2.setPointSize(12)
        font2.setBold(True)
        font2.setWeight(75)
        self.home3_label_5.setFont(font2)
        self.home3_label_5.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.home3_label_5.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.home3_label_6 = QLabel(Form)
        self.home3_label_6.setObjectName(u"home3_label_6")
        self.home3_label_6.setGeometry(QRect(280, 180, 71, 30))
        self.home3_label_6.setFont(font2)
        self.home3_label_6.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.home3_label_6.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.home3_label_7 = QLabel(Form)
        self.home3_label_7.setObjectName(u"home3_label_7")
        self.home3_label_7.setGeometry(QRect(280, 260, 71, 30))
        self.home3_label_7.setFont(font2)
        self.home3_label_7.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.home3_label_7.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.home_btn = QPushButton(Form)
        self.home_btn.setObjectName(u"home_btn")
        self.home_btn.setGeometry(QRect(10, 490, 121, 41))
        self.home_btn.setFont(font1)
        self.home_btn.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(26, 143, 125);\n"
"	border: 1px solid white;\n"
"	border-radius: 10px;\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: red;\n"
"}")
        self.home3_line_3 = QFrame(Form)
        self.home3_line_3.setObjectName(u"home3_line_3")
        self.home3_line_3.setGeometry(QRect(150, 220, 118, 3))
        self.home3_line_3.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.home3_line_3.setFrameShape(QFrame.HLine)
        self.home3_line_3.setFrameShadow(QFrame.Sunken)
        self.home3_line_4 = QFrame(Form)
        self.home3_line_4.setObjectName(u"home3_line_4")
        self.home3_line_4.setGeometry(QRect(150, 140, 118, 3))
        self.home3_line_4.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.home3_line_4.setFrameShape(QFrame.HLine)
        self.home3_line_4.setFrameShadow(QFrame.Sunken)
        self.home3_line = QFrame(Form)
        self.home3_line.setObjectName(u"home3_line")
        self.home3_line.setGeometry(QRect(5, 70, 410, 3))
        self.home3_line.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.home3_line.setFrameShape(QFrame.HLine)
        self.home3_line.setFrameShadow(QFrame.Sunken)
        self.jump_btn = QPushButton(Form)
        self.jump_btn.setObjectName(u"jump_btn")
        self.jump_btn.setGeometry(QRect(150, 490, 121, 41))
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
        self.jump_btn_2 = QPushButton(Form)
        self.jump_btn_2.setObjectName(u"jump_btn_2")
        self.jump_btn_2.setGeometry(QRect(290, 490, 121, 41))
        self.jump_btn_2.setFont(font1)
        self.jump_btn_2.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(26, 143, 125);\n"
"	border: 1px solid white;\n"
"	border-radius: 10px;\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: red;\n"
"}")
        self.home3_line_2 = QFrame(Form)
        self.home3_line_2.setObjectName(u"home3_line_2")
        self.home3_line_2.setGeometry(QRect(5, 470, 410, 3))
        self.home3_line_2.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.home3_line_2.setFrameShape(QFrame.HLine)
        self.home3_line_2.setFrameShadow(QFrame.Sunken)
        self.home3_label_8 = QLabel(Form)
        self.home3_label_8.setObjectName(u"home3_label_8")
        self.home3_label_8.setGeometry(QRect(70, 340, 72, 30))
        self.home3_label_8.setFont(font1)
        self.home3_label_8.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.home3_label_8.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.ch4_lcd_2 = QLCDNumber(Form)
        self.ch4_lcd_2.setObjectName(u"ch4_lcd_2")
        self.ch4_lcd_2.setGeometry(QRect(150, 320, 121, 51))
        self.ch4_lcd_2.setStyleSheet(u"border: 1px solid white;\n"
"color: rgb(255, 255, 255);")
        self.home3_line_5 = QFrame(Form)
        self.home3_line_5.setObjectName(u"home3_line_5")
        self.home3_line_5.setGeometry(QRect(150, 300, 118, 3))
        self.home3_line_5.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.home3_line_5.setFrameShape(QFrame.HLine)
        self.home3_line_5.setFrameShadow(QFrame.Sunken)
        self.ch4_lcd_3 = QLCDNumber(Form)
        self.ch4_lcd_3.setObjectName(u"ch4_lcd_3")
        self.ch4_lcd_3.setGeometry(QRect(150, 400, 121, 51))
        self.ch4_lcd_3.setStyleSheet(u"border: 1px solid white;\n"
"color: rgb(255, 255, 255);")
        self.home3_label_9 = QLabel(Form)
        self.home3_label_9.setObjectName(u"home3_label_9")
        self.home3_label_9.setGeometry(QRect(70, 410, 72, 30))
        self.home3_label_9.setFont(font1)
        self.home3_label_9.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.home3_label_9.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.home3_line_6 = QFrame(Form)
        self.home3_line_6.setObjectName(u"home3_line_6")
        self.home3_line_6.setGeometry(QRect(150, 380, 118, 3))
        self.home3_line_6.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.home3_line_6.setFrameShape(QFrame.HLine)
        self.home3_line_6.setFrameShadow(QFrame.Sunken)
        self.home3_label_10 = QLabel(Form)
        self.home3_label_10.setObjectName(u"home3_label_10")
        self.home3_label_10.setGeometry(QRect(280, 340, 71, 30))
        self.home3_label_10.setFont(font2)
        self.home3_label_10.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.home3_label_10.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.home3_label_11 = QLabel(Form)
        self.home3_label_11.setObjectName(u"home3_label_11")
        self.home3_label_11.setGeometry(QRect(280, 420, 71, 30))
        self.home3_label_11.setFont(font2)
        self.home3_label_11.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.home3_label_11.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\u5ba4\u5185\u73af\u5883\u76d1\u6d4b\u7cfb\u7edf", None))
        self.home3_label.setText(QCoreApplication.translate("Form", u"\u5ba4\u5185\u73af\u5883\u76d1\u6d4b\u7cfb\u7edf", None))
        self.home3_label_2.setText(QCoreApplication.translate("Form", u"\u6e29\u5ea6\uff1a", None))
        self.home3_label_3.setText(QCoreApplication.translate("Form", u"\u6e7f\u5ea6\uff1a", None))
        self.home3_label_4.setText(QCoreApplication.translate("Form", u"\u7532\u70f7\uff1a", None))
        self.home3_label_5.setText(QCoreApplication.translate("Form", u"\u2103", None))
        self.home3_label_6.setText(QCoreApplication.translate("Form", u"%RH", None))
        self.home3_label_7.setText(QCoreApplication.translate("Form", u"m\u00b3/g", None))
        self.home_btn.setText(QCoreApplication.translate("Form", u"\u4e3b\u754c\u9762", None))
        self.jump_btn.setText(QCoreApplication.translate("Form", u"\u73af\u5883\u8bb0\u5f55", None))
        self.jump_btn_2.setText(QCoreApplication.translate("Form", u"\u5ba4\u5185\u63a7\u5236", None))
        self.home3_label_8.setText(QCoreApplication.translate("Form", u"PM2.5", None))
        self.home3_label_9.setText(QCoreApplication.translate("Form", u"\u7532\u70f7\uff1a", None))
        self.home3_label_10.setText(QCoreApplication.translate("Form", u"\u00b5m", None))
        self.home3_label_11.setText(QCoreApplication.translate("Form", u"m\u00b3/g", None))
    # retranslateUi

