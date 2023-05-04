#GUI imports
from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QGridLayout
from PyQt5 import QtGui

#Import links to different scripts in Controller
import sys 
sys.path.append('./Controller')
from createProfController import createProfController

#Create new account GUI
class createProfUI(QWidget):
    def __init__(self, stackedWidget):
        super().__init__()

        self.stackedWidget = stackedWidget
        
        self.setWindowTitle('Admin')
        font = QtGui.QFont()
        font.setPointSize(16)

        # layout for manage Accounts -----------------------------------
        layout = QGridLayout()

        #Buttons
        self.userID_label = QLabel('Account ID:')
        self.userID_edit = QLineEdit()

        self.name_label = QLabel('Name:')
        self.name_edit = QLineEdit()

        self.DOB_label = QLabel('DOB(DDMMYYYY):')
        self.DOB_edit = QLineEdit()

        self.accType_label = QLabel('Account Type:')
        self.accType_edit = QLineEdit()
        
        layout.addWidget(self.userID_label,1, 1)
        layout.addWidget(self.userID_edit,1,2)

        layout.addWidget(self.name_label,2,1)
        layout.addWidget(self.name_edit,2,2)

        layout.addWidget(self.DOB_label,3,1)
        layout.addWidget(self.DOB_edit,3,2)

        layout.addWidget(self.accType_label,4,1)
        layout.addWidget(self.accType_edit,4,2)

        self.createButton = QPushButton('Create')
        self.backButton = QPushButton ('Back')
        
        self.backButton.clicked.connect(self.goBack)
        self.createButton.clicked.connect(self.createProfile)

        layout.addWidget(self.createButton,8 ,1)
        layout.addWidget(self.backButton, 8, 3)
        
        self.setLayout(layout)

    def goBack(self):
        self.stackedWidget.setCurrentIndex(4)

    #call this function to go to the entity, entity should have the SQL statements to create the account. parse the variables into the function
    def createProfile(self):
        userID = self.userID_edit.text()
        name = self.name_edit.text()
        DOB = self.DOB_edit.text()
        accType = self.accType_edit.text()
        createProfController.createProf(self,self.stackedWidget,userID, name, DOB, accType)