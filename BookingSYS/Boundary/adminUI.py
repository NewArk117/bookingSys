import sys 
sys.path.append('./Controller')
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QStackedWidget, QGridLayout, QMessageBox, QListWidget
from PyQt5 import QtCore, QtGui, QtWidgets
from manageAccController import manageAccController
from manageProfController import manageProfController
from logOutController import logOutController

class adminUI(QWidget):
    def __init__(self, stackedWidget):
        super().__init__()

        self.stackedWidget = stackedWidget

        self.setWindowTitle('Admin')
        font = QtGui.QFont()
        font.setPointSize(16)
        

        # create the layout for main -----------------------------------
        layoutMain = QGridLayout()
        #Buttons
        self.pushButton1= QPushButton("Manage Accounts")
        self.pushButton2= QPushButton("Manage Profiles")
        self.pushButton3= QPushButton("Logout")

        self.pushButton1.clicked.connect(self.callMAcc)
        self.pushButton2.clicked.connect(self.callMProf)
        self.pushButton3.clicked.connect(self.logOut)
        
        layoutMain.addWidget(self.pushButton1, 0, 1)
        layoutMain.addWidget(self.pushButton2, 1, 1)
        layoutMain.addWidget(self.pushButton3, 2, 1)

        #-----------------------------------------------------------------
        self.setLayout(layoutMain)
        
    def callMAcc(self):
        manageAccController.manAcc(self, self.stackedWidget)

    def callMProf(self):
        manageProfController.manProf(self, self.stackedWidget)

    def logOut(self):
        logOutController.loggingOut(self, self.stackedWidget)