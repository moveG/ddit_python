import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from qtpy import QtWidgets

form_class = uic.loadUiType("pyqt09.ui")[0]

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.pb.clicked.connect(self.myClick)
        self.le3.returnPressed.connect(self.myClick)
        
    def myClick(self) :
        num1 = int(self.le1.text())
        num2 = int(self.le2.text())
        num3 = int(self.le3.text())
        result = 0
        
        for i in range(num1, num2 + 1):
            if i % num3 == 0:
                result += i
        
        self.le4.setText(str(result))
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()