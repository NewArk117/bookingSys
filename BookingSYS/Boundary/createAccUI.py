import sys 
sys.path.append('./Controller')
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QStackedWidget, QGridLayout, QMessageBox, QListWidget
from PyQt5 import QtCore, QtGui, QtWidgets
from createAccController import createAccController

#wigdet index 5
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
        self.fname_label = QLabel('First Name:')
        self.fname_edit = QLineEdit()
        self.lname_label = QLabel('Last Name:')
        self.lname_edit = QLineEdit()
        self.age_label = QLabel('Age:')
        self.age_edit = QLineEdit()
        self.username_label = QLabel('New username:')
        self.username_edit = QLineEdit()
        self.password_label = QLabel('New password:')
        self.password_edit = QLineEdit()
        self.accType_label = QLabel('Account type:')
        self.accType_edit = QLineEdit()

        self.createButton = QPushButton('Create')
        self.backButton = QPushButton ('Back')
        
        self.backButton.clicked.connect(self.goBack)
        self.createButton.clicked.connect(self.createAccount)

        layout.addWidget(self.fname_label,1, 1)
        layout.addWidget(self.fname_edit,1,2)
        layout.addWidget(self.lname_label,2,1)
        layout.addWidget(self.lname_edit,2,2)
        layout.addWidget(self.age_label,3,1)
        layout.addWidget(self.age_edit,3,2)
        layout.addWidget(self.username_label,4,1)
        layout.addWidget(self.username_edit,4,2)
        layout.addWidget(self.password_label,5,1)
        layout.addWidget(self.password_edit,5,2)
        layout.addWidget(self.accType_label,6,1)
        layout.addWidget(self.accType_edit,6,2)
        layout.addWidget(self.createButton,8 ,1)
        layout.addWidget(self.backButton, 8, 3)
        
        self.setLayout(layout)

    def goBack(self):
        self.stackedWidget.setCurrentIndex(3)

    #call this function to go to the entity, entity should have the SQL statements to create the account. parse the variables into the function
    def createAccount(self):
        fname = self.fname_edit.text()
        lname = self.lname_edit.text()
        age = self.age_edit.text()
        username = self.username_edit.text()
        password = self.password_edit.text()
        accType = self.accType_edit.text()

        createAccController.createAcc(self,self.stackedWidget,fname, lname, age, username, password, accType)