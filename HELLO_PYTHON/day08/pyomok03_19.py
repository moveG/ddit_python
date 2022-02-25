import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from qtpy import QtGui, QtCore, QtWidgets
from PyQt5.QtGui import QIcon
from _ast import If
from conda.common._logic import FALSE

form_class = uic.loadUiType("pyomok03_19.ui")[0]

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.arr2d = [
            [0, 0, 0, 0, 0,  0, 0, 0, 0, 0,  0, 0, 0, 0, 0,  0, 0, 0, 0],
            [0, 0, 0, 0, 0,  0, 0, 0, 0, 0,  0, 0, 0, 0, 0,  0, 0, 0, 0],
            [0, 0, 0, 0, 0,  0, 0, 0, 0, 0,  0, 0, 0, 0, 0,  0, 0, 0, 0],
            [0, 0, 0, 0, 0,  0, 0, 0, 0, 0,  0, 0, 0, 0, 0,  0, 0, 0, 0],
            [0, 0, 0, 0, 0,  0, 0, 0, 0, 0,  0, 0, 0, 0, 0,  0, 0, 0, 0],

            [0, 0, 0, 0, 0,  0, 0, 0, 0, 0,  0, 0, 0, 0, 0,  0, 0, 0, 0],
            [0, 0, 0, 0, 0,  0, 0, 0, 0, 0,  0, 0, 0, 0, 0,  0, 0, 0, 0],
            [0, 0, 0, 0, 0,  0, 0, 0, 0, 0,  0, 0, 0, 0, 0,  0, 0, 0, 0],
            [0, 0, 0, 0, 0,  0, 0, 0, 0, 0,  0, 0, 0, 0, 0,  0, 0, 0, 0],
            [0, 0, 0, 0, 0,  0, 0, 0, 0, 0,  0, 0, 0, 0, 0,  0, 0, 0, 0],

            [0, 0, 0, 0, 0,  0, 0, 0, 0, 0,  0, 0, 0, 0, 0,  0, 0, 0, 0],
            [0, 0, 0, 0, 0,  0, 0, 0, 0, 0,  0, 0, 0, 0, 0,  0, 0, 0, 0],
            [0, 0, 0, 0, 0,  0, 0, 0, 0, 0,  0, 0, 0, 0, 0,  0, 0, 0, 0],
            [0, 0, 0, 0, 0,  0, 0, 0, 0, 0,  0, 0, 0, 0, 0,  0, 0, 0, 0],
            [0, 0, 0, 0, 0,  0, 0, 0, 0, 0,  0, 0, 0, 0, 0,  0, 0, 0, 0],       

            [0, 0, 0, 0, 0,  0, 0, 0, 0, 0,  0, 0, 0, 0, 0,  0, 0, 0, 0],
            [0, 0, 0, 0, 0,  0, 0, 0, 0, 0,  0, 0, 0, 0, 0,  0, 0, 0, 0],
            [0, 0, 0, 0, 0,  0, 0, 0, 0, 0,  0, 0, 0, 0, 0,  0, 0, 0, 0],
            [0, 0, 0, 0, 0,  0, 0, 0, 0, 0,  0, 0, 0, 0, 0,  0, 0, 0, 0] 
        ]
        
        self.pb2d = []
        self.flag_bw = True
        self.flag_ing = True
        
        for i in range(len(self.arr2d)):
            line = []
            
            for j in range(len(self.arr2d)):
                pb_one = QPushButton("", self)
                pb_one.setIcon(QtGui.QIcon("0.png"))
                pb_one.setIconSize(QtCore.QSize(40, 40))
                pb_one.setGeometry((QtCore.QRect(j*40, i*40, 40, 40)))
                pb_one.setToolTip("{},{}".format(i, j))
                pb_one.clicked.connect(self.myClick)
                line.append(pb_one)
            self.pb2d.append(line)
        
        self.myRender()
        
        self.pb_reset.clicked.connect(self.myReset)
        
    def myRender(self):
        for i in range(len(self.arr2d)):
            for j in range(len(self.arr2d)):
                if self.arr2d[i][j] == 0:
                    self.pb2d[i][j].setIcon(QtGui.QIcon("0.png"))
                if self.arr2d[i][j] == 1:
                    self.pb2d[i][j].setIcon(QtGui.QIcon("1.png"))
                if self.arr2d[i][j] == 2:
                    self.pb2d[i][j].setIcon(QtGui.QIcon("2.png"))
    
    def myClick(self):
        if not self.flag_ing:
            return

        str_ij = self.sender().toolTip().split(",")
        i = int(str_ij[0])
        j = int(str_ij[1])
        
        if self.arr2d[i][j] > 0:
            return
        
        stone = -1

        if self.flag_bw:
            self.arr2d[i][j] = 1
            stone = 1
        else:
            self.arr2d[i][j] = 2
            stone = 2
        
        up = self.checkUP(i, j, stone)
        dw = self.checkDW(i, j, stone)
        le = self.checkLE(i, j, stone)
        ri = self.checkRI(i, j, stone)
        
        ul = self.checkUL(i, j, stone)
        ur = self.checkUR(i, j, stone)
        dl = self.checkDL(i, j, stone)
        dr = self.checkDR(i, j, stone)
        
        d1 = up + dw + 1
        d2 = le + ri + 1
        d3 = ur + dl + 1
        d4 = ul + dr + 1

        self.myRender()
        
        if d1 == 5 or d2 == 5 or d3 == 5 or d4 == 5:
            if self.flag_bw:
                QtWidgets.QMessageBox.about(self, "오목", "흑돌의 승리")
            else:
                QtWidgets.QMessageBox.about(self, "오목", "백돌의 승리")
            self.flag_ing = False
                
        self.flag_bw = not self.flag_bw
        
    def myReset(self):
        for i in range(len(self.arr2d)):
            for j in range(len(self.arr2d)):
                self.arr2d[i][j] = 0
        self.myRender()

        self.flag_bw = True
        self.flag_ing = True

    def checkUP(self, i , j , stone):
        cnt = 0
        
        try:
            while True:
                i -= 1
                
                if i < 0:
                    return cnt
                if j < 0:
                    return cnt 
                
                if self.arr2d[i][j] == stone:
                    cnt += 1
                else:    
                    return cnt
        except:
            return cnt
    
    def checkDW(self, i , j , stone):
        cnt = 0
        
        try:
            while True:
                i += 1
                
                if i < 0:
                    return cnt
                if j < 0:
                    return cnt 
                
                if self.arr2d[i][j] == stone:
                    cnt += 1
                else:    
                    return cnt
        except:
            return cnt
        
    def checkLE(self, i , j , stone):
        cnt = 0
        
        try:
            while True:
                j -= 1
                
                if i < 0:
                    return cnt
                if j < 0:
                    return cnt 
                
                if self.arr2d[i][j] == stone:
                    cnt += 1
                else:    
                    return cnt
        except:
            return cnt
    
    def checkRI(self, i , j , stone):
        cnt = 0
        
        try:
            while True:
                j += 1
                
                if i < 0:
                    return cnt
                if j < 0:
                    return cnt 
                
                if self.arr2d[i][j] == stone:
                    cnt += 1
                else:    
                    return cnt
        except:
            return cnt
    
    def checkUL(self, i , j , stone):
        cnt = 0
        
        try:
            while True:
                i -= 1
                j -= 1
                
                if i < 0:
                    return cnt
                if j < 0:
                    return cnt 
                
                if self.arr2d[i][j] == stone:
                    cnt += 1
                else:    
                    return cnt
        except:
            return cnt
    
    def checkUR(self, i , j , stone):
        cnt = 0
        
        try:
            while True:
                i -= 1
                j += 1
                
                if i < 0:
                    return cnt
                if j < 0:
                    return cnt 
                
                if self.arr2d[i][j] == stone:
                    cnt += 1
                else:    
                    return cnt
        except:
            return cnt
    
    def checkDL(self, i , j , stone):
        cnt = 0
        
        try:
            while True:
                i += 1
                j -= 1
                
                if i < 0:
                    return cnt
                if j < 0:
                    return cnt 
                
                if self.arr2d[i][j] == stone:
                    cnt += 1
                else:    
                    return cnt
        except:
            return cnt
    
    def checkDR(self, i , j , stone):
        cnt = 0
        
        try:
            while True:
                i += 1
                j += 1
                
                if i < 0:
                    return cnt
                if j < 0:
                    return cnt 
                
                if self.arr2d[i][j] == stone:
                    cnt += 1
                else:    
                    return cnt
        except:
            return cnt
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()