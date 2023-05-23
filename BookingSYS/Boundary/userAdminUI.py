#GUI imports
from PyQt5.QtWidgets import  QWidget, QLabel, QPushButton, QGridLayout, QListWidget, QLabel, QLineEdit, QMessageBox, QComboBox
import sqlite3
#Import links to different scripts in Controller
import sys 
sys.path.append('./Controller')
from viewProfController import viewProfileController
from viewAllProfController import viewAllProfileController
from editAccController import editAccountController
from editProfController import editProfileController
from viewAllAccController import viewAllAccountController
from viewAccController import viewAccountController
from searchAccController import searchAccountController
from searchProfController import searchProfileController
from suspendAccController import suspendAccountController
from suspendProfController import suspendProfileController

#Admin account main page GUI
class userAdminUI(QWidget):
    def __init__(self, stackedWidget):
        super().__init__()

        self.stackedWidget = stackedWidget
        
        #layout for manage accounts 
        layoutAcc = QGridLayout()

        #Buttons
        #Account
        self.labelStaff= QLabel("Accounts")
        self.labelCust= QLabel("Profiles")
        self.AccountBox = QListWidget()
        self.buttonCreateAcc= QPushButton("Create Account")
        self.buttonSuspendAcc = QPushButton("Suspend Account")
        self.buttonEditAcc = QPushButton("Edit Account")
        self.profBox = QListWidget()
        self.searchAccButton = QPushButton("Search Account")
        self.searchAccEdit = QLineEdit()
        self.viewAccButton = QPushButton("View Account")
        self.backButton = QPushButton("Back")
        
        self.backButton.clicked.connect(self.goBack)
        self.buttonCreateAcc.clicked.connect(self.goCreateAcc)
        self.buttonEditAcc.clicked.connect(self.editAcc)
        self.searchAccButton.clicked.connect(self.searchAcc)
        self.viewAccButton.clicked.connect(self.viewAcc)
        self.buttonSuspendAcc.clicked.connect(self.suspendAcc)

        layoutAcc.addWidget(self.labelStaff, 0, 0)
        layoutAcc.addWidget(self.AccountBox, 1, 0)
        layoutAcc.addWidget(self.labelCust, 2, 0)
        layoutAcc.addWidget(self.profBox, 3, 0)
        layoutAcc.addWidget(self.buttonCreateAcc, 0, 1)
        layoutAcc.addWidget(self.buttonSuspendAcc, 0 ,2)
        layoutAcc.addWidget(self.buttonEditAcc, 0, 3)
        layoutAcc.addWidget(self.searchAccEdit, 1, 1)
        layoutAcc.addWidget(self.searchAccButton, 1, 2)
        layoutAcc.addWidget(self.backButton, 5, 1)
        layoutAcc.addWidget(self.viewAccButton, 1, 3)

        #Profile
        self.buttonCreate2= QPushButton("Create Profile")
        self.buttonSuspend2 = QPushButton("Suspend Profile")
        self.buttonEdit2 = QPushButton("Edit Profile")
        self.buttonViewProfile = QPushButton("View Profile")
        self.searchProfButton = QPushButton("Search Profile")
        self.searchProfEdit = QLineEdit()

        self.buttonCreate2.clicked.connect(self.goCreateProf)
        self.buttonViewProfile.clicked.connect(self.viewProfile)
        self.buttonEdit2.clicked.connect(self.editProf)
        self.searchProfButton.clicked.connect(self.searchProf)
        self.buttonSuspend2.clicked.connect(self.suspendProf)

        layoutAcc.addWidget(self.buttonCreate2, 2 ,1)
        layoutAcc.addWidget(self.buttonSuspend2, 2 ,2)
        layoutAcc.addWidget(self.buttonEdit2, 2 ,3)
        layoutAcc.addWidget(self.searchProfButton, 3, 2)
        layoutAcc.addWidget(self.searchProfEdit, 3 , 1)
        layoutAcc.addWidget(self.buttonViewProfile, 3 ,3)
        self.setLayout(layoutAcc)

        self.stackedWidget.currentChanged.connect(self.viewAllAcc)
        self.stackedWidget.currentChanged.connect(self.viewAllProf)
        

    #User Story 7
    def searchAcc(self):
        item_name = self.searchAccEdit.text()
        list = searchAccountController.searchAccount(self, self.stackedWidget, item_name, self.AccountBox)

    #User Story 12
    def searchProf(self):
        item_name = self.searchProfEdit.text() 
        #call the search profile controller   
        list = searchProfileController.searchProfile(self, self.stackedWidget, item_name, self.profBox)

    #User Story 6
    def suspendAcc(self):
        selected_item = self.AccountBox.currentItem()
        if selected_item is not None:
            item_name = selected_item.text()

            #Call the suspend controller
            suspendAcc = suspendAccountController.suspendAccount(self, item_name)
            if suspendAcc == "changed":
                message_box = QMessageBox()
                message_box.setWindowTitle(item_name)
                message_box.setText(item_name + '  suspended')
                message_box.exec_()
    #User Story 11
    def suspendProf(self):
        selected_item = self.profBox.currentItem()
        if selected_item is not None:
            item_name = selected_item.text()
            suspendProf = suspendProfileController.suspendProfile(self, item_name)
            if suspendProf == "changed":
                message_box = QMessageBox()
                message_box.setWindowTitle(item_name)
                message_box.setText(item_name + ' is suspended')
                message_box.exec_()

    def goBack(self):
        self.stackedWidget.setCurrentIndex(2)

    def goCreateAcc(self):
        self.stackedWidget.setCurrentIndex(4)

    def goCreateProf(self):
        self.stackedWidget.setCurrentIndex(5)

    #User story 5
    def editAcc(self):
        selected_item = self.AccountBox.currentItem()

        # If an item is selected, display its name
        if selected_item is not None:
            item_name = selected_item.text()
            while True:
                message_box = QMessageBox()
                message_box.setWindowTitle(item_name)
                message_box.setText('Edit Account')

                layout = QGridLayout()
                label = QLabel("Password:")
                line_edit = QLineEdit()
                layout.addWidget(label,2,0)
                layout.addWidget(line_edit,2,1)

                suspendList = ["False","True"]
                suspend_label = QLabel('Account Lock:')
                suspend_cBox = QComboBox()
                suspend_cBox.addItems(suspendList) 
                layout.addWidget(suspend_label,3,0)
                layout.addWidget(suspend_cBox,3,1)

                # Create a widget to hold the layout and set it as the message box's body
                widget = QWidget()
                widget.setLayout(layout)
                message_box.layout().addWidget(widget)
                message_box.addButton(QMessageBox.Ok)

                result = message_box.exec_()
                if result == QMessageBox.Ok:
                    line = line_edit.text()
                    suspended =suspend_cBox.currentText()
                    #Call edit controller
                    edit = editAccountController.editAccount(self, item_name, line, suspended)
                    if edit:
                        success_message_box = QMessageBox()
                        success_message_box.setWindowTitle("Success")
                        success_message_box.setText("Pass!!!")
                        success_message_box.exec_()
                        break
                    else:
                        failure_message_box = QMessageBox()
                        failure_message_box.setWindowTitle("Edit Failed")
                        failure_message_box.setText("Empty Field!!!")
                        failure_message_box.exec_()
                else:
                    break       
                
    #User story 10
    def editProf(self):
        selected_item = self.profBox.currentItem()

        # If an item is selected, display its name
        if selected_item is not None:
            item_name = selected_item.text()
            while True:
                

                message_box = QMessageBox()
                message_box.setWindowTitle(item_name)
                message_box.setText('Edit Profile')

                layout = QGridLayout()
                
                label1 = QLabel("Name:")
                line_edit1 = QLineEdit()
                layout.addWidget(label1,1,0)
                layout.addWidget(line_edit1,1,1)      
                
                label2 = QLabel("Age:")
                line_edit2 = QLineEdit()
                layout.addWidget(label2,2,0)
                layout.addWidget(line_edit2,2,1)

                accTypeList = ['userAdmin', 'customer', 'cinemaManager', 'cinemaOwner']
                accType_label = QLabel('Account Type:')
                accType_cBox = QComboBox()
                accType_cBox.addItems(accTypeList) 
                layout.addWidget(accType_label,3,0)
                layout.addWidget(accType_cBox,3,1)

                suspendList = ["False","True"]
                suspend_label = QLabel('Profile Lock:')
                suspend_cBox = QComboBox()
                suspend_cBox.addItems(suspendList) 
                layout.addWidget(suspend_label,4,0)
                layout.addWidget(suspend_cBox,4,1)
                # Create a widget to hold the layout and set it as the message box's body
                widget = QWidget()
                widget.setLayout(layout)
                message_box.layout().addWidget(widget)
                message_box.addButton(QMessageBox.Ok)

                result = message_box.exec_()
                if result == QMessageBox.Ok:
                    name = line_edit1.text()
                    age = line_edit2.text()
                    accType =accType_cBox.currentText()
                    suspended =suspend_cBox.currentText()

                    #call the edit profile controller
                    edit = editProfileController.editProfile(self, item_name, name, age, accType,suspended)
                    if edit == "Success":
                        success_message_box = QMessageBox()
                        success_message_box.setWindowTitle("Success")
                        success_message_box.setText("Pass!!!")
                        success_message_box.exec_()
                        break
                    elif edit == "stringError":
                        failure_message_box = QMessageBox()
                        failure_message_box.setWindowTitle("Edit Failed")
                        failure_message_box.setText("Age has string")
                        failure_message_box.exec_()
                    elif edit == "integerError":
                        failure_message_box = QMessageBox()
                        failure_message_box.setWindowTitle("Edit Failed")
                        failure_message_box.setText("Name has integer")
                        failure_message_box.exec_()
                    else:
                        failure_message_box = QMessageBox()
                        failure_message_box.setWindowTitle("Edit Failed")
                        failure_message_box.setText("Empty Field!!!")
                        failure_message_box.exec_()
                else:
                    break       

    #User story 9
    def viewProfile(self):
        selected_item = self.profBox.currentItem()
        # If an item is selected, display its name
        if selected_item is not None:
            item_name = selected_item.text()

            #call the view controller 
            profileDetails = viewProfileController.viewProfile(self, item_name)
            if profileDetails == None:
                message_box1 = QMessageBox()
                message_box1.setText("Profile is Locked")
                message_box1.exec_()
            else:
                message_box = QMessageBox()
                message_box.setText("Account ID: " + str(profileDetails[0]) + "\n" + "Name: " + str(profileDetails[1]) 
                                    + "\n" + "Age: " + str(profileDetails[2]) + "\n" + "Account Type: " 
                                    + str(profileDetails[3]))
                message_box.setWindowTitle(str(profileDetails[0]))
                message_box.exec_()

    #User Story 4
    def viewAcc(self):
            selected_item = self.AccountBox.currentItem()
            # If an item is selected, display its name
            if selected_item is not None:
                item_name = selected_item.text()

                #Call the view account controller
                accountDetails = viewAccountController.viewAccount(self, item_name)
                accountDetails = list(accountDetails)
                if accountDetails[3] == True:
                    accountDetails[3] = "Not Locked"
                else:
                    accountDetails[3] = "Locked"
                accountDetails = tuple(accountDetails)
                message_box = QMessageBox()
                message_box.setText("Account ID: " + str(accountDetails[0]) + "\n" + "Password: " + str(accountDetails[1]) + "\n" + "Account Type: " + str(accountDetails[2] + "\n" + "Account: " + str(accountDetails[3])))
                message_box.setWindowTitle(str(accountDetails[0]))
                message_box.exec_()

    def viewAllAcc(self):
        viewAllAccountController.viewAllAccount(self,self.stackedWidget, self.AccountBox)

    def viewAllProf(self):
        viewAllProfileController.viewAllProfile(self,self.stackedWidget, self.profBox)