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
        i = settingScreens[0]
        i.close()




class team(QtGui.QWidget):
    increase = int
    decrease = int

    def __init__(self, number, increase, decrease, size):
        super(team, self).__init__()
        self.increase = increase
        self.decrease = decrease
        title = ("team %s")%(number)
        self.setWindowTitle(str(title))
        self.setFixedSize(int(size)*1.90, int(size)*1.30)
        self.move(number*150, 100)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setStyleSheet("background-color: black")
        self.pointLabel = QtGui.QLabel('0', self)
        self.pointLabel.setAlignment(QtCore.Qt.AlignRight)
        self.pointLabel.setFixedSize(int(size)*1.90, int(size)*1.30)
        self.pointLabel.setStyleSheet("QLabel { color : white; font-size : "+size+"px;}")
        self.show()

    def setScore(self, score):
        self.pointLabel.setText(str(score))

    def getScore(self):
        return int(self.pointLabel.text())

    def increaseScore(self):
        self.setScore(self.getScore()+self.increase)

    def decreaseScore(self):
        self.setScore(self.getScore()-self.decrease)

    def mousePressEvent(self, event):
        self.offset = event.pos()

    def mouseMoveEvent(self, event):
        x=event.globalX()
        y=event.globalY()
        x_w = self.offset.x()
        y_w = self.offset.y()
        self.move(x-x_w, y-y_w)


class settings(QtGui.QWidget):


    def __init__(self):
        super(settings, self).__init__()
        title = "settings"
        self.setWindowTitle(str(title))
        self.setFixedSize(200,200)
        self.setTeamsLabel = QtGui.QLabel('Number of teams:', self)
        self.setTeamsLabel.setAlignment(QtCore.Qt.AlignLeft)
        self.setTeamsLabel.setGeometry(10, 16, 90, 15) #left, top, width, height
        self.setTeams = QtGui.QTextEdit('2', self)
        self.setTeams.setGeometry(160, 10, 30, 24)
        self.setPositiveLabel = QtGui.QLabel('Positive score:', self)
        self.setPositiveLabel.setAlignment(QtCore.Qt.AlignLeft)
        self.setPositiveLabel.setGeometry(10, 46, 90, 15)
        self.setPositive = QtGui.QTextEdit('1', self)
        self.setPositive.setGeometry(160, 40, 30, 24)
        self.setNegativeLabel = QtGui.QLabel('Negative score:', self)
        self.setNegativeLabel.setAlignment(QtCore.Qt.AlignLeft)
        self.setNegativeLabel.setGeometry(10, 76, 90, 15)
        self.setNegative = QtGui.QTextEdit('1', self)
        self.setNegative.setGeometry(160, 70, 30, 24)
        self.setFontLabel = QtGui.QLabel('Font size:', self)
        self.setFontLabel.setAlignment(QtCore.Qt.AlignLeft)
        self.setFontLabel.setGeometry(10, 106, 90, 15)
        self.setFont = QtGui.QTextEdit('70', self)
        self.setFont.setGeometry(160, 100, 30, 24)
        self.setOKButton = QtGui.QPushButton('OK', self)
        self.setOKButton.setGeometry(140, 160, 50, 30)
        QtCore.QObject.connect(self.setOKButton, QtCore.SIGNAL("clicked()"), self.makeControllers)
        self.yearLabel = QtGui.QLabel('2013', self)
        self.yearLabel.setAlignment(QtCore.Qt.AlignLeft)
        self.yearLabel.setGeometry(10, 160, 30, 15)
        self.nameLabel = QtGui.QLabel('Videokomiteen', self)
        self.nameLabel.setAlignment(QtCore.Qt.AlignLeft)
        self.nameLabel.setGeometry(10, 175, 90, 15)
        self.show()



    def makeControllers(self):
        teams = int(self.setTeams.toPlainText())
        positive = int(self.setPositive.toPlainText())
        negative = int(self.setNegative.toPlainText())
        font = self.setFont.toPlainText()
        for i in range(1, teams+1):
            controllers.append(controller(i, team(i, positive, negative, font)))




app = QtGui.QApplication(sys.argv)
settingScreens = []
controllers = []
settingScreens.append(settings())
sys.exit(app.exec_())





