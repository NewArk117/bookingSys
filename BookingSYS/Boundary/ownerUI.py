#GUI imports
from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton,QVBoxLayout, QListWidget, QAbstractItemView, QDialog, QMessageBox, QHBoxLayout, QDateEdit, QComboBox
from PyQt5 import QtGui
from PyQt5.QtCore import QStringListModel, Qt, QTimer, QDate
import sqlite3
#Import links to different scripts in Controller
import sys 
import calendar
import datetime
sys.path.append('./Controller')
sys.path.append('./Entity')
from logOutController import logOutController
from ownerController import viewHourlyTicController,viewHourlyRevController, viewDailyTicController,viewDailyRevController, viewWeeklyTicController, viewWeeklyRevController

#Create new account GUI
class ownerUI(QWidget):
    def __init__(self, stackedWidget):
        super().__init__()

        self.stackedWidget = stackedWidget
        
        self.setWindowTitle('Owner')
        font = QtGui.QFont()
        font.setPointSize(15)

        # layout for manage Accounts -----------------------------------
        layout = QVBoxLayout()

        freqList = ["Hourly", "Daily", "Weekly"]

        self.label1 = QLabel("Generate report")
        self.label1.setFixedSize(150,150)
        self.label1.adjustSize()
        self.label1.setFont(font)

        self.label2 =QLabel()
        self.label2.setFixedSize(150,60)
        self.label2.adjustSize()
        
        layout1 = QHBoxLayout()
        self.ticketLabel = QLabel("Number of Tickets Sold:")
        self.ticHourly = QPushButton("Hourly")
        self.ticDaily = QPushButton("Daily")
        self.ticWeekly = QPushButton("Weekly")
        layout1.addWidget(self.ticketLabel)
        layout1.addWidget(self.ticHourly)
        layout1.addWidget(self.ticDaily)
        layout1.addWidget(self.ticWeekly)

        layout2= QHBoxLayout()
        self.revenueLabel = QLabel("Revenue:")
        self.revHourly = QPushButton("Hourly")
        self.revDaily = QPushButton("Daily")
        self.revWeekly = QPushButton("Weekly")
        layout2.addWidget(self.revenueLabel)
        layout2.addWidget(self.revHourly)
        layout2.addWidget(self.revDaily)
        layout2.addWidget(self.revWeekly)

        self.labelempty = QLabel()
        self.logOutButton = QPushButton("Logout")

        layout.addWidget(self.label1)
        layout.addLayout(layout1)
        layout.addLayout(layout2)
        #layout.addWidget(self.labelempty)
        layout.addWidget(self.logOutButton)

        self.logOutButton.clicked.connect(self.logOut)
        self.ticHourly.clicked.connect(self.viewHourlyTic)
        self.ticDaily.clicked.connect(self.viewDailyTic)
        self.ticWeekly.clicked.connect(self.viewWeeklyTic)
        self.revHourly.clicked.connect(self.viewHourlyRev)
        self.revDaily.clicked.connect(self.viewDailyRev)
        self.revWeekly.clicked.connect(self.viewWeeklyRev)

        self.setLayout(layout)

    def viewHourlyTic(self):
        self.text = ""
        self.itemname = ""
        print("Hourly")
        self.text, self.itemname = viewHourlyTicController.viewHourlyTicC(self)

        msgBox = QMessageBox()
        msgBox.setText(self.text)
        msgBox.setWindowTitle(self.itemname)
        msgBox.exec_()

    def viewDailyTic(self):
        self.text = ""
        self.itemname = ""
        print("Daily")
        self.text, self.itemname = viewDailyTicController.viewDailyTicC(self)

        msgBox = QMessageBox()
        msgBox.setText(self.text)
        msgBox.setWindowTitle(self.itemname)
        msgBox.exec_()

    def viewWeeklyTic(self):
        self.text = ""
        self.itemname = ""
        print("Weekly")
        self.text, self.itemname = viewWeeklyTicController.viewWeeklyTicC(self)

        msgBox = QMessageBox()
        msgBox.setText(self.text)
        msgBox.setWindowTitle(self.itemname)
        msgBox.exec_()

    

    def viewHourlyRev(self):
        self.text = ""
        self.itemname = ""
        print("Hourly")
        self.text, self.itemname = viewHourlyRevController.viewHourlyRevC(self)

        msgBox = QMessageBox()
        msgBox.setText(self.text)
        msgBox.setWindowTitle(self.itemname)
        msgBox.exec_()

    def viewDailyRev(self):
        self.text = ""
        self.itemname = ""
        print("Daily")
        self.text, self.itemname = viewDailyRevController.viewDailyRevC(self)

        msgBox = QMessageBox()
        msgBox.setText(self.text)
        msgBox.setWindowTitle(self.itemname)
        msgBox.exec_()

    def viewWeeklyRev(self):
        self.text = ""
        self.itemname = ""
        print("Weekly")
        self.text, self.itemname = viewWeeklyRevController.viewWeeklyRevC(self)

        msgBox = QMessageBox()
        msgBox.setText(self.text)
        msgBox.setWindowTitle(self.itemname)
        msgBox.exec_()

    def logOut(self):
        logout = logOutController.loggingOut(self)
        if logout == True:
            self.stackedWidget.setCurrentIndex(0)