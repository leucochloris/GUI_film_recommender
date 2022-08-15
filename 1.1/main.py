import sys
import random
from design import *
from PyQt5 import QtCore, QtGui, QtWidgets
##from PyQt5 import Qt

class MyWin(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


        self.ui.pushButton.clicked.connect(self.message)

        self.a = [
            "Безумный Макс: Дорога ярости\n2015 г.\nIMDb: 8,1",
            "Малыш на драйве\n2017 г.\nIMDb: 7,7",
            "Мстители\n2012 г.\nIMDb: 8,1"
            ]

        self.b = [
            "Атака на Перл Харбор\n2011 г.\nIMDb: 6.8",
            "Ярость\n2014 г.\nIMDb: 7.6",
            "Спасти рядового Райана\n1998 г.\nIMDb: 8.6"
            ]

        self.c =  [
            "Зеленая миля\n1999 г.\nIMDb: 8.5",
            "Начало\n2010 г.\nIMDb: 8.8",
            "Престиж\n2006 г.\nIMDb: 8.5"
            ]
        self.index = self.ui.combo.currentIndex()

    def message(self):
        self.messageb = QtWidgets.QMessageBox ()
        self.messageb.setIcon (QtWidgets.QMessageBox.Information)
        self.messageb.setWindowTitle ("Рекомендую: ")

        if self.index == 0:
            self.messageb.setText (str (random.SystemRandom ().choice (self.a)))
        elif self.index == 1:
            self.messageb.setText (str (random.SystemRandom ().choice (self.b)))
        elif self.index == 2:
            self.messageb.setText (str (random.SystemRandom ().choice (self.c)))

        self.okButton = self.messageb.addButton ('Ок', QtWidgets.QMessageBox.AcceptRole)
        self.messageb.exec ()

    # Пока пустая функция которая выполняется при нажатии на кнопку  
    def MyFunction(self):
        pass



if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    myapp.show()
    sys.exit(app.exec_())
