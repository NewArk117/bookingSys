import sys
import subprocess
from PyQt5 import QtGui
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QStackedWidget
sys.path.append('./Boundary')
from loginUI import loginUI
from adminUI import adminUI
from manageAcc import manageAcc
from manageProf import manageProf
from createAccUI import createAccUI
from createProfUI import createProfUI

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # set the window properties
        self.resize(800,600)
        self.setWindowTitle('Main Page')

        #stackedwidget to move from page to page
        self.stackedWidget = QStackedWidget()
        self.setCentralWidget(self.stackedWidget)

        #main page
        self.layoutMain = QVBoxLayout()
        button = QPushButton('Admin')
        button.clicked.connect(self.adminLog)

        self.layoutMain.addWidget(QLabel('WHO ARE YOU!'))
        self.layoutMain.addWidget(button)

        self.pageMain = QWidget()
        self.pageMain.setLayout(self.layoutMain)
        self.stackedWidget.addWidget(self.pageMain)


        #CREATE OBJECT OF THE UI HERE ======
        self.pageLogin = loginUI(self.stackedWidget) #1
        self.stackedWidget.addWidget(self.pageLogin)

        self.admin = adminUI(self.stackedWidget)#2
        self.stackedWidget.addWidget(self.admin)

        self.manageAcc = manageAcc(self.stackedWidget)#3
        self.stackedWidget.addWidget(self.manageAcc)

        self.manageProf = manageProf(self.stackedWidget)#4
        self.stackedWidget.addWidget(self.manageProf)

        self.createAccUI = createAccUI(self.stackedWidget)#5
        self.stackedWidget.addWidget(self.createAccUI)

        self.createProfUI = createProfUI(self.stackedWidget)#6
        self.stackedWidget.addWidget(self.createProfUI)


    def adminLog(self):
        self.stackedWidget.setCurrentIndex(1)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())