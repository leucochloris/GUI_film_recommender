import sys
from random   import choice
from PyQt5    import QtCore, QtGui, QtWidgets
from designUi import Ui_MainWindow

class MyWin(QtWidgets.QMainWindow):
    def __init__(self, myList, parent=None):
        QtWidgets.QWidget.__init__(self, parent)

        self.myList = myList

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.label_3 = QtWidgets.QLabel()

        grid = QtWidgets.QGridLayout(self.ui.centralwidget)
        grid.addWidget(self.ui.label,      0, 0) 
        grid.addWidget(self.ui.label_2,    1, 0)
        grid.addWidget(self.ui.comboBox,   2, 0) 
        grid.addWidget(self.label_3,       3, 0)
        grid.addWidget(self.ui.pushButton, 4, 0)         

        # Здесь прописываем событие нажатия на кнопку        
        self.ui.pushButton.clicked.connect(self.MyFunction)

        self.comboIndex = 0
        self.ui.comboBox.activated[int].connect(self.onActivatedText)

    @QtCore.pyqtSlot(int) 
    def onActivatedText(self, index):
        self.comboIndex = index     

    def MyFunction(self):
        self.label_3.setText(choice(self.myList[self.comboIndex]))


myList = [
    ['Безумный Макс: Дорога ярости\n2015 г.\nIMDb: 8,1',
    'Малыш на драйве\n2017 г.\nIMDb: 7,7',
    'Мстители\n2012 г.\nIMDb: 8,1'],
    ['Атака на Перл Харбор\n2011 г.\nIMDb: 6.8',
    'Ярость\n2014 г.\nIMDb: 7.6',
    'Спасти рядового Райана\n1998 г.\nIMDb: 8.6'],
    ['Зеленая миля\n1999 г.\nIMDb: 8.5',
    'Начало\n2010 г.\nIMDb: 8.8',
    'Престиж\n2006 г.\nIMDb: 8.5']
]

if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin(myList)
    myapp.show()
    sys.exit(app.exec_())
