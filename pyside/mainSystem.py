# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainSystem.ui'
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
        self.search_btn = QPushButton(Form)
        self.search_btn.setObjectName(u"search_btn")
        self.search_btn.setGeometry(QRect(20, 380, 161, 51))
        font1 = QFont()
        font1.setFamily(u"\u5fae\u8f6f\u96c5\u9ed1")
        font1.setPointSize(14)
        font1.setBold(True)
        font1.setWeight(75)
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
        self.home1_btn = QPushButton(Form)
        self.home1_btn.setObjectName(u"home1_btn")
        self.home1_btn.setGeometry(QRect(120, 100, 161, 51))
        self.home1_btn.setFont(font1)
        self.home1_btn.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(26, 143, 125);\n"
"	border: 1px solid white;\n"
"	border-radius: 10px;\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: red;\n"
"}")
        self.line_6 = QFrame(Form)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setGeometry(QRect(140, 170, 118, 3))
        self.line_6.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.line_6.setFrameShape(QFrame.HLine)
        self.line_6.setFrameShadow(QFrame.Sunken)
        self.home2_btn = QPushButton(Form)
        self.home2_btn.setObjectName(u"home2_btn")
        self.home2_btn.setGeometry(QRect(120, 190, 161, 51))
        self.home2_btn.setFont(font1)
        self.home2_btn.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(26, 143, 125);\n"
"	border: 1px solid white;\n"
"	border-radius: 10px;\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: red;\n"
"}")
        self.line_7 = QFrame(Form)
        self.line_7.setObjectName(u"line_7")
        self.line_7.setGeometry(QRect(140, 260, 118, 3))
        self.line_7.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.line_7.setFrameShape(QFrame.HLine)
        self.line_7.setFrameShadow(QFrame.Sunken)
        self.home3_btn_2 = QPushButton(Form)
        self.home3_btn_2.setObjectName(u"home3_btn_2")
        self.home3_btn_2.setGeometry(QRect(120, 285, 161, 51))
        self.home3_btn_2.setFont(font1)
        self.home3_btn_2.setStyleSheet(u"QPushButton {\n"
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
        self.search_btn.setText(QCoreApplication.translate("Form", u"\u73af\u5883\u8bb0\u5f55", None))
        self.jump_btn.setText(QCoreApplication.translate("Form", u"\u5ba4\u5185\u63a7\u5236", None))
        self.home1_btn.setText(QCoreApplication.translate("Form", u"\u623f\u95f4\u4e00", None))
        self.home2_btn.setText(QCoreApplication.translate("Form", u"\u623f\u95f4\u4e00", None))
        self.home3_btn_2.setText(QCoreApplication.translate("Form", u"\u5ba2\u5385", None))
    # retranslateUi

