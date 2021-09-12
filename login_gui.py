from PyQt5 import QtWidgets
from PyQt5.uic import loadUiType
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from os import path
from sys import argv
from sqlite3 import connect

db = connect("login.db")

cr = db.cursor()
cr.execute("select * from login")
data = cr.fetchone()
usr = data[0]
passw = data[1]

FORM_CLASS,_=loadUiType(path.join(path.dirname(__file__),"login.ui"))

class LoadingScreen(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(0,0,1280,720)
        self.setFixedSize(1280,720)
        # self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.CustomizeWindowHint)

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



class mainapp(QMainWindow,FORM_CLASS):
    def __init__(self, parent=None):
        super(mainapp,self).__init__(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.login_button.clicked.connect(self.login)
        

    def login(self):
        self.loading_screen = LoadingScreen()
        self.show()
        username = self.username_input.text()
        password = self.password_input.text()
        if username == usr and password == passw :
            print("logged in succesfully")
        else:
            print("wrong credentials")

if __name__ == "__main__":
    app = QApplication(argv)
    MainWindow = QtWidgets.QMainWindow()
    window = mainapp()
    window.show()
    app.exec()