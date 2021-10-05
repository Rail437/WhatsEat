# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\DesktopProgram\sample_program\sample.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
import json
import sys

from PyQt5 import QtCore, QtGui, QtWidgets

import DesktopProgram.img.menu_images_rc
from DesktopProgram.sample_program.test_frime import Ui_Form


class Ui_WhatsEat(object):
    def setupUi(self, WhatsEat):
        WhatsEat.setObjectName("WhatsEat")
        WhatsEat.resize(1024, 768)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(WhatsEat.sizePolicy().hasHeightForWidth())
        WhatsEat.setSizePolicy(sizePolicy)
        WhatsEat.setMinimumSize(QtCore.QSize(1024, 768))
        WhatsEat.setMaximumSize(QtCore.QSize(1024, 768))
        WhatsEat.setStyleSheet("background-color: rgb(44, 44, 44);")
        self.centralwidget = QtWidgets.QWidget(WhatsEat)
        self.centralwidget.setMinimumSize(QtCore.QSize(1024, 768))
        self.centralwidget.setMaximumSize(QtCore.QSize(1024, 768))
        self.centralwidget.setObjectName("centralwidget")
        self.menu_bar = QtWidgets.QWidget(self.centralwidget)
        self.menu_bar.setGeometry(QtCore.QRect(0, 0, 60, 200))
        self.menu_bar.setStyleSheet("background-color: rgb(56, 56, 56);\n"
                                    "border-bottom-right-radius: 10px;")
        self.menu_bar.setObjectName("menu_bar")
        # self.menu_bar.mousePressEvent(QtGui.QMouseEvent())
        self.menu_search = QtWidgets.QPushButton(self.menu_bar)
        self.menu_search.setGeometry(QtCore.QRect(5, 11, 50, 50))
        self.menu_search.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/menu/menu_search.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.menu_search.setIcon(icon)
        self.menu_search.setIconSize(QtCore.QSize(50, 50))
        self.menu_search.setCheckable(False)
        self.menu_search.setObjectName("menu_search")
        self.menu_login = QtWidgets.QPushButton(self.menu_bar)
        self.menu_login.setGeometry(QtCore.QRect(5, 76, 50, 50))
        self.menu_login.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/menu/menu_profile.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.menu_login.setIcon(icon1)
        self.menu_login.setIconSize(QtCore.QSize(50, 50))
        self.menu_login.setObjectName("menu_login")
        self.menu_help = QtWidgets.QPushButton(self.menu_bar)
        self.menu_help.setGeometry(QtCore.QRect(5, 141, 50, 50))
        self.menu_help.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/menu/menu_help.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.menu_help.setIcon(icon2)
        self.menu_help.setIconSize(QtCore.QSize(50, 50))
        self.menu_help.setObjectName("menu_help")
        self.header = QtWidgets.QWidget(self.centralwidget)
        self.header.setGeometry(QtCore.QRect(94, 36, 868, 89))
        self.header.setObjectName("header")
        self.header_name = QtWidgets.QLabel(self.header)
        self.header_name.setGeometry(QtCore.QRect(10, 0, 811, 35))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(24)
        self.header_name.setFont(font)
        self.header_name.setStyleSheet("color: rgb(255, 255, 255);")
        self.header_name.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.header_name.setObjectName("header_name")
        self.header_name.setText("Подобрать блюдо на ужин")
        self.line = QtWidgets.QLabel(self.header)
        self.line.setGeometry(QtCore.QRect(8, 44, 858, 10))
        self.line.setStyleSheet("background-color: rgb(231, 180, 0);")
        self.line.setText("")
        self.line.setObjectName("line")
        self.catalog = QtWidgets.QLabel(self.header)
        self.catalog.setGeometry(QtCore.QRect(10, 62, 171, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.catalog.setFont(font)
        self.catalog.setStyleSheet("color: rgb(255, 255, 255);")
        self.catalog.setObjectName("catalog")
        self.catalog.setText("Книга рецептов")
        self.content_area = QtWidgets.QWidget(self.centralwidget)
        self.content_area.setGeometry(QtCore.QRect(99, 141, 868, 583))
        self.content_area.setStyleSheet("")
        self.content_area.setObjectName("content_area")
        WhatsEat.setCentralWidget(self.centralwidget)
        WhatsEat.setWindowTitle("WhatsEat")
        QtCore.QMetaObject.connectSlotsByName(WhatsEat)
        self.recipe = Ui_Form()


