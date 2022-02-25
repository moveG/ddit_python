import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_class = uic.loadUiType("pyqt12.ui")[0]

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.pb1.clicked.connect(self.myClick)
        self.pb2.clicked.connect(self.myClick)
        self.pb3.clicked.connect(self.myClick)
        self.pb4.clicked.connect(self.myClick)
        
    def myClick(self) :
        num1 = float(self.le1.text())
        num2 = float(self.le2.text())
        result = 0
        math = self.sender().text()
        
        if math == "+":
            result = int(num1 + num2)
        elif math == "-":
            result = int(num1 - num2)
        elif math == "*":
            result = int(num1 * num2)
        else:
            result = num1 / num2
        
        self.le3.setText(str(result))
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()