#Import to use SQL database
import sqlite3

#GUI imports
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import  QWidget, QLabel, QPushButton, QGridLayout, QListWidget, QListWidgetItem

#Import links to different scripts in Controller
import sys 
sys.path.append('./Controller')
from viewProfController import viewProfileController
from editAccController import editAccountController
from editProfController import editProfileController
from viewAccController import viewAccountController

#Admin account main page GUI
class manageAcc(QWidget):
    def __init__(self, stackedWidget):
        super().__init__()

        self.stackedWidget = stackedWidget
        
        #layout for manage accounts 
        layoutAcc = QGridLayout()

        #Buttons
        #Account
        self.labelStaff= QLabel("Staff Accounts")
        self.labelCust= QLabel("Customer Accounts")
        self.staffBox = QListWidget()
        self.buttonCreateAcc= QPushButton("Create Account")
        self.buttonDeleteAcc = QPushButton("Delete Account")
        self.buttonEditAcc = QPushButton("Edit Account")
        self.custBox = QListWidget()
        self.backButton = QPushButton("Back")

        self.backButton.clicked.connect(self.goBack)
        self.buttonCreateAcc.clicked.connect(self.goCreateAcc)
        self.buttonEditAcc.clicked.connect(self.editAcc)
        

        layoutAcc.addWidget(self.labelStaff, 0, 0)
        layoutAcc.addWidget(self.staffBox, 1, 0)
        layoutAcc.addWidget(self.labelCust, 2, 0)
        layoutAcc.addWidget(self.custBox, 3, 0)
        layoutAcc.addWidget(self.buttonCreateAcc, 0, 1)
        layoutAcc.addWidget(self.buttonDeleteAcc, 0 ,2)
        layoutAcc.addWidget(self.buttonEditAcc, 0, 3)
        layoutAcc.addWidget(self.backButton, 5, 1)
        

        #Profile
        self.buttonCreate2= QPushButton("Create Profile")
        self.buttonDelete2 = QPushButton("Delete Profile")
        self.buttonEdit2 = QPushButton("Edit Profile")
        self.buttonViewProfile = QPushButton("View Profile")

        self.buttonCreate2.clicked.connect(self.goCreateProf)
        self.buttonViewProfile.clicked.connect(self.perform_action)
        self.buttonEdit2.clicked.connect(self.editProf)
        layoutAcc.addWidget(self.buttonCreate2, 3 ,1)
        layoutAcc.addWidget(self.buttonDelete2, 3 ,2)
        layoutAcc.addWidget(self.buttonEdit2, 3 ,3)
        layoutAcc.addWidget(self.buttonViewProfile, 4 ,1)
        self.setLayout(layoutAcc)


    
        #QTimer to periodically refresh the list widget
        self.timer1 = QTimer()
        self.timer1.timeout.connect(self.refreshStaffAcc)
        self.timer1.start(5000) # refresh every 5 second

        #QTimer to periodically refresh the list widget
        self.timer2 = QTimer()
        self.timer2.timeout.connect(self.refreshCustAcc)
        self.timer2.start(5000) # refresh every 5 second


    def deleteAcc(self):
        backButtonController.backButtonC(self, self.stackedWidget)

    def goBack(self):
        self.stackedWidget.setCurrentIndex(2)

    def goCreateAcc(self):
        self.stackedWidget.setCurrentIndex(4)

    def goCreateProf(self):
        self.stackedWidget.setCurrentIndex(5)

    def editAcc(self):
        selected_item = self.staffBox.currentItem()
        selected_item2 = self.custBox.currentItem()

        # If an item is selected, display its name
        if selected_item is not None:
            item_name = selected_item.text()
            editAccountController.editAccount(self, self.stackedWidget, item_name)

        elif selected_item2 is not None:
            item_name2 = selected_item2.text()
            editAccountController.editAccount(self, self.stackedWidget, item_name2)

    def editProf(self):
        selected_item = self.staffBox.currentItem()
        selected_item2 = self.custBox.currentItem()

        # If an item is selected, display its name
        if selected_item is not None:
            item_name = selected_item.text()
            editProfileController.editProfile(self, self.stackedWidget, item_name)

        elif selected_item2 is not None:
            item_name2 = selected_item2.text()
            editProfileController.editProfile(self, self.stackedWidget, item_name2)

    def refreshStaffAcc(self):
        # connect to the database
        conn = sqlite3.connect('SilverVillageUserAcc.db')

        # execute a query to retrieve data from the database
        cursor = conn.execute("SELECT * FROM account WHERE permission = 'sysAdmin' OR permission = 'staff' or permission = 'cinemaOwner' or permission = 'cinemaManager'")

        # clear the list widget
        self.staffBox.clear()

        # populate the list widget with data from the query
        for row in cursor:
            item = QListWidgetItem(str(row[0]))
            self.staffBox.addItem(item)

        # close the database connection
        conn.close()
        
    def refreshCustAcc(self):
        # connect to the database
        conn = sqlite3.connect('SilverVillageUserAcc.db')

        # execute a query to retrieve data from the database
        cursor = conn.execute("SELECT * FROM account WHERE permission = 'customer'")

        # clear the list widget
        self.custBox.clear()

        # populate the list widget with data from the query
        for row in cursor:
            item = QListWidgetItem(str(row[0]))
            self.custBox.addItem(item)

        # close the database connection
        conn.close()

    def perform_action(self):
        selected_item = self.staffBox.currentItem()
        selected_item2 = self.custBox.currentItem()

        # If an item is selected, display its name
        if selected_item is not None:
            item_name = selected_item.text()
            viewProfileController.viewProfile(self, self.stackedWidget, item_name)

        elif selected_item2 is not None:
            item_name2 = selected_item2.text()
            viewProfileController.viewProfile(self, self.stackedWidget, item_name2)

    def viewAcc(self):
        viewAccountController.viewAccount(self,self.stackedWidget)