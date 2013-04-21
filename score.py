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
        # i = settingScreens[0]
        # i.close()

    def closeEvent(self, e):
        self.team.close()
        e.accept()




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


class settings(QtGui.QDialog):


    def __init__(self):
        super(settings, self).__init__()
        title = "settings"
        self.setWindowTitle(str(title))
        self.resize(190,200)
        #self.setFixedSize(200,200)

        self.layout = QtGui.QGridLayout(self)

        # number of teams
        self.setTeams = QtGui.QLineEdit('2')
        self.setTeams.setValidator(QtGui.QIntValidator())
        self.layout.addWidget(QtGui.QLabel('Number of teams:'), 0, 0)
        self.layout.addWidget(self.setTeams, 0, 1)

        # positive score
        self.setPositive = QtGui.QLineEdit('1', self)
        self.setPositive.setValidator(QtGui.QIntValidator())
        self.layout.addWidget(QtGui.QLabel('Positive score:'), 1, 0)
        self.layout.addWidget(self.setPositive, 1, 1)
    
        # negative score
        self.setNegative = QtGui.QLineEdit('1', self)
        self.setNegative.setValidator(QtGui.QIntValidator())
        self.layout.addWidget(QtGui.QLabel('Negative score:'), 2, 0)
        self.layout.addWidget(self.setNegative, 2, 1)

        # font size
        self.setFont = QtGui.QLineEdit('70', self)
        self.setFont.setValidator(QtGui.QIntValidator())
        self.layout.addWidget(QtGui.QLabel('Font size:'), 3, 0)
        self.layout.addWidget(self.setFont)

        # ok button
        self.okButton = QtGui.QPushButton('OK')
        self.okButton.clicked.connect(self.makeControllers)
        self.layout.addWidget(self.okButton, 4, 1)

        self.layout.addWidget(QtGui.QLabel('Videokomiteen<br>2013'),4,0)

        self.setLayout(self.layout)
        #self.show()



    def makeControllers(self):
        teams = int(self.setTeams.text())
        positive = int(self.setPositive.text())
        negative = int(self.setNegative.text())
        font = self.setFont.text()
        for i in range(1, teams+1):
            controllers.append(controller(i, team(i, positive, negative, font)))
        self.accept()




app = QtGui.QApplication(sys.argv)
settingScreens = []
controllers = []
#settingScreens.append(settings())
#settingScreens[-1].exec_()

s = settings()
s.show()

sys.exit(app.exec_())





