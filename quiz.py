from PyQt4.QtScript import __init__

__author__ = 'Christian'

import sys
from PyQt4 import QtGui, QtCore

class controller(QtGui.QWidget):

    def setScore(self):
        self.team.setScore(self.scoreInput.toPlainText())

    def __init__(self, number, team):
        super(controller, self).__init__()
        self.team = team
        title = ("controller %s")%(number)
        self.setWindowTitle(str(title))
        self.setFixedSize(120,200)
        self.move(number*150, 200)
        self.increaseButton = QtGui.QPushButton('+', self)
        self.increaseButton.setGeometry(10, 10, 100, 50)
        QtCore.QObject.connect(self.increaseButton, QtCore.SIGNAL("clicked()"), self.team.increaseScore)
        self.decreaseButton = QtGui.QPushButton('-', self)
        self.decreaseButton.setGeometry(10, 70, 100, 50)
        QtCore.QObject.connect(self.decreaseButton, QtCore.SIGNAL("clicked()"), self.team.decreaseScore)
        self.scoreInput = QtGui.QTextEdit('0', self)
        self.scoreInput.setGeometry(10, 130, 100, 25)
        self.scoreButton = QtGui.QPushButton('Set score', self)
        self.scoreButton.setGeometry(10, 165, 100, 30)
        QtCore.QObject.connect(self.scoreButton, QtCore.SIGNAL("clicked()"), self.setScore)
        self.show()



class team(QtGui.QWidget):
    def __init__(self, number):
        super(team, self).__init__()
        points = 0
        title = ("team %s")%(number)
        self.setWindowTitle(str(title))
        self.setFixedSize(130,90)
        self.move(number*150, 100)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setStyleSheet("background-color: black")
        self.pointLabel = QtGui.QLabel('0', self)
        self.pointLabel.setAlignment(QtCore.Qt.AlignRight)
        self.pointLabel.setFixedSize(130, 90)
        self.pointLabel.setStyleSheet("QLabel { color : white; font-size : 70px;}")
        self.show()

    def setScore(self, score):
        self.pointLabel.setText(str(score))

    def getScore(self):
        return int(self.pointLabel.text())

    def increaseScore(self):
        self.setScore(self.getScore()+2)

    def decreaseScore(self):
        self.setScore(self.getScore()-1)

    def mousePressEvent(self, event):
        self.offset = event.pos()

    def mouseMoveEvent(self, event):
        x=event.globalX()
        y=event.globalY()
        x_w = self.offset.x()
        y_w = self.offset.y()
        self.move(x-x_w, y-y_w)


teams=4

controllers = []
app = QtGui.QApplication(sys.argv)
for i in range(1, teams+1):
    controllers.append(controller(i, team(i)))

sys.exit(app.exec_())



