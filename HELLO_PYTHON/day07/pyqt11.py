import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
import random
from qtpy import QtWidgets

form_class = uic.loadUiType("pyqt11.ui")[0]

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()

        self.arr3 = []
        self.setArr3()
        self.count = 0
        print(self.arr3)
        
        self.setupUi(self)
        self.pb.clicked.connect(self.myClick)
        self.le.returnPressed.connect(self.myClick)
        
    def setArr3(self):
        arr9 = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        
        while True:
            rnd = int(random.random() * len(arr9))
            if arr9[rnd] > "0":
                self.arr3.append(arr9[rnd])
                arr9[rnd] = "-1"
            if len(self.arr3) >= 3:
                break
        
    def myClick(self) :
        self.count += 1
        
        str_old = self.te.toPlainText()
        
        str3 = self.le.text()
        i_s = self.getS(str3)
        i_b = self.getB(str3)
        
        str_new = "{}S, {}B...{}\n".format(i_s, i_b, str3)
        
        self.le.setText("")
        self.te.setText(str_new + str_old)
        
        if i_s == 3:
            QtWidgets.QMessageBox.about(self, "BASEBALL", "{}회 만의 승리".format(self.count))
                
    def getB(self, str3):
        cnt = 0
        
        if self.arr3[0] == str3[1:2] or self.arr3[0] == str3[2:3]:
            cnt += 1
        if self.arr3[1] == str3[0:1] or self.arr3[1] == str3[2:3]:
            cnt += 1
        if self.arr3[2] == str3[0:1] or self.arr3[2] == str3[1:2]:
            cnt += 1
       
        return cnt

    def getS(self, str3):
        cnt = 0
        
        if self.arr3[0] == str3[0:1]:
            cnt += 1
        if self.arr3[1] == str3[1:2]:
            cnt += 1
        if self.arr3[2] == str3[2:3]:
            cnt += 1
       
        return cnt
       
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()