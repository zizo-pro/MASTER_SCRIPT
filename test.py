from PyQt5 import QtWidgets
from PyQt5.uic import loadUiType
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from os import path
from sys import argv



class LoadingScreen(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(0,0,1280,720)
        self.setFixedSize(1280,720)
        self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.CustomizeWindowHint)

        self.label_animation = QLabel(self)
        self.movie = QMovie("i.gif")

        timer = QTimer(self)
        self.startAnimation()
        timer.singleShot(11000,self.stopAnimation)

        self.show()

    def startAnimation(self):
        self.movie.start()

    def stopAnimation(self):
        self.movie.stop()
        self.close()

class appdemo(QWidget):
    def __init__(self):
        super().__init__()
        label = QLabel('<font size=12> this is main app window </font>',self)
        label.setGeometry(150,150,300,50)
        self.loading_screen = LoadingScreen()
        self.show()

app = QApplication(argv)
demo = appdemo()
app.exit(app.exec_())