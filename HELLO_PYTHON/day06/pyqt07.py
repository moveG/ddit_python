import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
import random

form_class = uic.loadUiType("pyqt07.ui")[0]

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.pb.clicked.connect(self.myClick)
        self.le.returnPressed.connect(self.myClick)
        
    def myClick(self) :
        dan = self.le.text()
        idan = int(dan)
        gugudan = ""
        gugudan += "{} * {} = {}\n".format(idan, 1, idan * 1)
        gugudan += "{} * {} = {}\n".format(idan, 2, idan * 2)
        gugudan += "{} * {} = {}\n".format(idan, 3, idan * 3)
        gugudan += "{} * {} = {}\n".format(idan, 4, idan * 4)
        gugudan += "{} * {} = {}\n".format(idan, 5, idan * 5)
        gugudan += "{} * {} = {}\n".format(idan, 6, idan * 6)
        gugudan += "{} * {} = {}\n".format(idan, 7, idan * 7)
        gugudan += "{} * {} = {}\n".format(idan, 8, idan * 8)
        gugudan += "{} * {} = {}\n".format(idan, 9, idan * 9)
        
        self.te.setText(gugudan)
            
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()