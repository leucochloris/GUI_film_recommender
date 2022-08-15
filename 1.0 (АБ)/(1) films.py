
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'films.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(320, 240)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.combo = QtWidgets.QComboBox(self.centralwidget)
        self.combo.setObjectName("combo")
        self.combo.addItem("")
        self.combo.addItem("")
        self.combo.addItem("")
        self.gridLayout.addWidget(self.combo, 2, 0, 1, 1)
        self.ok = QtWidgets.QPushButton(self.centralwidget)
        self.ok.setObjectName("ok")
        self.gridLayout.addWidget(self.ok, 3, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.combo.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Помочь выбрать фильм?"))
        self.label_2.setText(_translate("MainWindow", "Выберите жанр:"))
        self.combo.setItemText(0, _translate("MainWindow", "Боевик"))
        self.combo.setItemText(1, _translate("MainWindow", "Военный"))
        self.combo.setItemText(2, _translate("MainWindow", "Детектив"))
        self.ok.setText(_translate("MainWindow", "Подобрать фильм!"))
