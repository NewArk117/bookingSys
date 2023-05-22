#GUI Imports
from PyQt5.QtWidgets import QWidget, QPushButton, QGridLayout, QMessageBox
from PyQt5 import QtGui

#Import links to different scripts in Controller
import sys 
sys.path.append('./Controller')
from logOutController import logOutController

#Admin home page
class adminUI(QWidget):
    def __init__(self, stackedWidget):
        super().__init__()
        self.stackedWidget = stackedWidget
        
        # create the layout for main
        layoutMain = QGridLayout()
        
        #Buttons
        self.pushButton1= QPushButton("Manage Accounts")
        self.pushButton3= QPushButton("Logout")

        self.pushButton1.clicked.connect(self.callMAcc)
        self.pushButton3.clicked.connect(self.logOut)
        
        layoutMain.addWidget(self.pushButton1, 0, 1)
        layoutMain.addWidget(self.pushButton3, 2, 1)

        self.setLayout(layoutMain)
        
    def callMAcc(self):
        self.stackedWidget.setCurrentIndex(3)

    def callMProf(self):
        self.stackedWidget.setCurrentIndex(4)

    #User Story 2
    def logOut(self):
        reply = QMessageBox.question(self, 'Confirm logout',
                                    'Are you sure you want to logout?',
                                     QMessageBox.Yes | QMessageBox.No)
        
        if reply == QMessageBox.Yes:

            #Call the logout controlller
            logout = logOutController.loggingOut(self)

            if logout == True:
                self.stackedWidget.setCurrentIndex(0)