#GUI imports
from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton,QGridLayout, QComboBox, QMessageBox
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
        self.accTypeList = ['userAdmin', 'customer', 'cinemaManager', 'cinemaOwner']

        #Buttons
        self.userID_label = QLabel('Account ID:')
        self.userID_edit = QLineEdit()
        self.password_label = QLabel('New password:')
        self.password_edit = QLineEdit()
        self.accType_label = QLabel('Account Type:')
        self.accType_cBox = QComboBox()
        self.accType_cBox.addItems(self.accTypeList)
        

        self.createButton = QPushButton('Create')
        self.backButton = QPushButton ('Back')
        
        self.backButton.clicked.connect(self.goBack)
        self.createButton.clicked.connect(self.createAccount)

        layout.addWidget(self.password_label, 6,1)
        layout.addWidget(self.password_edit,6,2)
        layout.addWidget(self.userID_label,5,1)
        layout.addWidget(self.userID_edit,5,2)
        layout.addWidget(self.accType_label,7,1)
        layout.addWidget(self.accType_cBox,7,2)
        layout.addWidget(self.createButton,8 ,1)
        layout.addWidget(self.backButton, 8, 3)
        
        self.setLayout(layout)

    def goBack(self):
        self.stackedWidget.setCurrentIndex(3)
        

    def createAccount(self):
        password = self.password_edit.text()
        userID = self.userID_edit.text()
        accType = self.accType_cBox.currentText()
        widget1 = QWidget()
        
        #Call the controller
        newAcc = createAccController.createAcc(self, userID, password, accType)
        
        emptyError = "A column is empty please fill up all the details"
        IDError = "ID already in used"
        success = "Account Created"
        Error = "Error"
        if newAcc == 'Success':
            QMessageBox.information(widget1, "Done!", success)
            self.stackedWidget.setCurrentIndex(3)
        elif newAcc == 'IDError':
            QMessageBox.information(widget1, Error, IDError)
        else:
             QMessageBox.warning(widget1, Error, emptyError)

        self.password_edit.clear()
        self.userID_edit.clear()
    