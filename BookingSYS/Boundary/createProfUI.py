import sys 
sys.path.append('./Controller')
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QStackedWidget, QGridLayout, QMessageBox, QListWidget
from PyQt5 import QtCore, QtGui, QtWidgets
from createProfController import createProfController

#wigdet index 5
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
        self.profileName_label = QLabel('Profile Name:')
        self.profileName_edit = QLineEdit()
        self.systemR_label = QLabel('System rights:')
        self.systemR_edit = QLineEdit()
        

        self.createButton = QPushButton('Create')
        self.backButton = QPushButton ('Back')
        
        self.backButton.clicked.connect(self.goBack)
        self.createButton.clicked.connect(self.createProfile)

        layout.addWidget(self.profileName_label,1, 1)
        layout.addWidget(self.profileName_edit,1,2)
        layout.addWidget(self.systemR_label,2,1)
        layout.addWidget(self.systemR_edit,2,2)
        layout.addWidget(self.createButton,8 ,1)
        layout.addWidget(self.backButton, 8, 3)
        
        self.setLayout(layout)

    def goBack(self):
        self.stackedWidget.setCurrentIndex(4)

    #call this function to go to the entity, entity should have the SQL statements to create the account. parse the variables into the function
    def createProfile(self):
        profilename = self.profileName_edit.text()
        systemR = self.systemR_edit.text()

        createProfController.createProf(self,self.stackedWidget,profilename, systemR)