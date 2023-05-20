#GUI imports
from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton,QGridLayout
from PyQt5 import QtGui

#Import links to different scripts in Controller
import sys 
sys.path.append('./Controller')
from createAccController import createAccController


#Create new account GUI
class createAccUI(QWidget):
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
        self.username_label = QLabel('New username:')
        self.username_edit = QLineEdit()
        self.password_label = QLabel('New password:')
        self.password_edit = QLineEdit()
        self.accType_label = QLabel('Account Type:')
        self.accType_edit = QLineEdit()
        

        self.createButton = QPushButton('Create')
        self.backButton = QPushButton ('Back')
        
        self.backButton.clicked.connect(self.goBack)
        self.createButton.clicked.connect(self.createAccount)

        layout.addWidget(self.username_label,4,1)
        layout.addWidget(self.username_edit,4,2)
        layout.addWidget(self.password_label,5,1)
        layout.addWidget(self.password_edit,5,2)
        layout.addWidget(self.userID_label,6,1)
        layout.addWidget(self.userID_edit,6,2)
        layout.addWidget(self.accType_label,7,1)
        layout.addWidget(self.accType_edit,7,2)
        layout.addWidget(self.createButton,8 ,1)
        layout.addWidget(self.backButton, 8, 3)
        
        self.setLayout(layout)

    def goBack(self):
        self.stackedWidget.setCurrentIndex(3)
        

    def createAccount(self):
        username = self.username_edit.text()
        password = self.password_edit.text()
        userID = self.userID_edit.text()
        accType = self.accType_edit.text()
        createAccController.createAcc(self,self.stackedWidget, userID, username, password, accType)
        
        self.username_edit.clear()
        self.password_edit.clear()
        self.userID_edit.clear()
        self.accType_edit.clear()