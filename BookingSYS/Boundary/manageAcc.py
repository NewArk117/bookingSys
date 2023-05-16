#GUI imports
from PyQt5.QtWidgets import  QWidget, QLabel, QPushButton, QGridLayout, QListWidget, QLabel, QLineEdit

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

#Admin account main page GUI
class manageAcc(QWidget):
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
        self.buttonDeleteAcc = QPushButton("Delete Account")
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
        

        layoutAcc.addWidget(self.labelStaff, 0, 0)
        layoutAcc.addWidget(self.AccountBox, 1, 0)
        layoutAcc.addWidget(self.labelCust, 2, 0)
        layoutAcc.addWidget(self.profBox, 3, 0)
        layoutAcc.addWidget(self.buttonCreateAcc, 0, 1)
        layoutAcc.addWidget(self.buttonDeleteAcc, 0 ,2)
        layoutAcc.addWidget(self.buttonEditAcc, 0, 3)
        layoutAcc.addWidget(self.searchAccEdit, 1, 1)
        layoutAcc.addWidget(self.searchAccButton, 1, 2)
        layoutAcc.addWidget(self.backButton, 5, 1)
        layoutAcc.addWidget(self.viewAccButton, 1, 3)

        #Profile
        self.buttonCreate2= QPushButton("Create Profile")
        self.buttonDelete2 = QPushButton("Delete Profile")
        self.buttonEdit2 = QPushButton("Edit Profile")
        self.buttonViewProfile = QPushButton("View Profile")
        self.searchProfButton = QPushButton("Search Profile")
        self.searchProfEdit = QLineEdit()

        self.buttonCreate2.clicked.connect(self.goCreateProf)
        self.buttonViewProfile.clicked.connect(self.viewProfile)
        self.buttonEdit2.clicked.connect(self.editProf)
        
        layoutAcc.addWidget(self.buttonCreate2, 2 ,1)
        layoutAcc.addWidget(self.buttonDelete2, 2 ,2)
        layoutAcc.addWidget(self.buttonEdit2, 2 ,3)
        layoutAcc.addWidget(self.searchProfButton, 3, 2)
        layoutAcc.addWidget(self.searchProfEdit, 3 , 1)
        layoutAcc.addWidget(self.buttonViewProfile, 3 ,3)
        self.setLayout(layoutAcc)


        self.stackedWidget.currentChanged.connect(self.viewAllAcc)
        self.stackedWidget.currentChanged.connect(self.viewAllProf)

    def searchAcc(self):
        item_name = self.searchAccEdit.text()
        searchAccountController.searchAccount(self, self.stackedWidget, item_name, self.AccountBox)

    def deleteAcc(self):
        backButtonController.backButtonC(self, self.stackedWidget)

    def goBack(self):
        self.stackedWidget.setCurrentIndex(2)

    def goCreateAcc(self):
        self.stackedWidget.setCurrentIndex(4)

    def goCreateProf(self):
        self.stackedWidget.setCurrentIndex(5)

    def editAcc(self):
        selected_item = self.AccountBox.currentItem()

        # If an item is selected, display its name
        if selected_item is not None:
            item_name = selected_item.text()
            editAccountController.editAccount(self, self.stackedWidget, item_name)
            
    def editProf(self):
        selected_item = self.profBox.currentItem()

        # If an item is selected, display its name
        if selected_item is not None:
            item_name = selected_item.text()
            editProfileController.editProfile(self, self.stackedWidget, item_name)


    def viewProfile(self):
        selected_item = self.profBox.currentItem()
        # If an item is selected, display its name
        if selected_item is not None:
            item_name = selected_item.text()
            viewProfileController.viewProfile(self, self.stackedWidget, item_name)

    def viewAcc(self):
            selected_item = self.AccountBox.currentItem()
            # If an item is selected, display its name
            if selected_item is not None:
                item_name = selected_item.text()
                viewAccountController.viewAccount(self, self.stackedWidget, item_name)

    def viewAllAcc(self):
        viewAllAccountController.viewAllAccount(self,self.stackedWidget, self.AccountBox)

    def viewAllProf(self):
        viewAllProfileController.viewAllProfile(self,self.stackedWidget, self.profBox)