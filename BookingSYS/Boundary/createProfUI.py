#GUI imports
import sqlite3
from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QGridLayout, QComboBox, QMessageBox
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
        conn = sqlite3.connect('SilverVillageUserAcc.db')
        cursor = conn.cursor()
        cursor.execute("SELECT userID FROM account")
        
        rows = cursor.fetchall()
        self.userIDList = []
        for row in rows:
            self.userIDList.append(row[0])

        self.userID_label = QLabel('Account ID:')
        self.userID_cBox = QComboBox()
        self.userID_cBox.addItems(self.userIDList)

        self.name_label = QLabel('Name:')
        self.name_edit = QLineEdit()

        self.DOB_label = QLabel("Age:")
        self.DOB_edit = QLineEdit()

        self.accTypeList = ['userAdmin', 'customer', 'cinemaManager', 'cinemaOwner']
        self.accType_label = QLabel('Account Type:')
        self.accType_cBox = QComboBox()
        self.accType_cBox.addItems(self.accTypeList)
        
        layout.addWidget(self.userID_label,1, 1)
        layout.addWidget(self.userID_cBox,1,2)

        layout.addWidget(self.name_label,2,1)
        layout.addWidget(self.name_edit,2,2)

        layout.addWidget(self.DOB_label,3,1)
        layout.addWidget(self.DOB_edit,3,2)

        layout.addWidget(self.accType_label,4,1)
        layout.addWidget(self.accType_cBox,4,2)

        self.createButton = QPushButton('Create')
        self.backButton = QPushButton ('Back')
        
        self.backButton.clicked.connect(self.goBack)
        self.createButton.clicked.connect(self.createProfile)

        layout.addWidget(self.createButton,8 ,1)
        layout.addWidget(self.backButton, 8, 3)
        
        self.setLayout(layout)

    def goBack(self):
        self.stackedWidget.setCurrentIndex(3)

    #User story 8
    def createProfile(self):
        userID = self.userID_cBox.currentText()
        name = self.name_edit.text()
        age = self.DOB_edit.text()
        accType = self.accType_cBox.currentText()
        widget1 = QWidget()

        #Call the create profile controller controller
        newProf = createProfController.createProf(self,userID, name, age, accType)

        success = "Profile Created"
        Error = "Error"
        integerError = "There is integer in the name!"
        stringError = "Contain String in age"
        emptyError = "There is empty column"
        if newProf == 'Success':
            QMessageBox.information(widget1, "Done!", success)
            self.stackedWidget.setCurrentIndex(3)
        elif newProf == "stringError":
            QMessageBox.information(widget1, Error, stringError)
        elif newProf == "emptyError":
            QMessageBox.information(widget1, Error, emptyError)
        else:
             QMessageBox.information(widget1, Error, integerError)

        self.name_edit.clear()
        self.DOB_edit.clear()
