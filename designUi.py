
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 220)                        # 400
        MainWindow.setMinimumSize(QtCore.QSize(400, 220))  # 400
        MainWindow.setMaximumSize(QtCore.QSize(400, 220))  # 400
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Icons8-Ios7-Cinema-Documentary.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAccessibleName("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 151, 21))
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(10, 140, 121, 31))
        self.pushButton.setObjectName("pushButton")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 50, 111, 21))
        self.label_2.setObjectName("label_2")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(10, 80, 121, 22))
        self.comboBox.setMaxVisibleItems(8)
        self.comboBox.setFrame(True)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Know You Better"))
        self.label.setText(_translate("MainWindow", "Помочь Вам выбрать фильм?!"))
        self.pushButton.setText(_translate("MainWindow", "Нажмите на меня"))
        self.label_2.setText(_translate("MainWindow", "Выберите жанр"))
        self.comboBox.setCurrentText(_translate("MainWindow", "Боевик"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Боевик"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Военный"))
        self.comboBox.setItemText(2, _translate("MainWindow", "Детектив"))
