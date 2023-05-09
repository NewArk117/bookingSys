#GUI imports
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QGridLayout

#Import links to different scripts in Controller
import sys 
sys.path.append('./Controller')
from loginController import loginController

#Admin Login 
class loginUI(QWidget):
    def __init__(self, stackedWidget):
        super().__init__()
        self.stackedWidget = stackedWidget

       #Create the login form
        self.username_label = QLabel('Username:')
        self.username_edit = QLineEdit()
        self.password_label = QLabel('Password:')
        self.password_edit = QLineEdit()
        self.password_edit.setEchoMode(QLineEdit.Password)
        self.login_button = QPushButton('Login')
        self.backButton = QPushButton ('Back')

        #Create the layout
        layoutLogin = QGridLayout()
        layoutLogin.addWidget(self.username_label, 1, 0)
        layoutLogin.addWidget(self.username_edit, 1, 1)
        layoutLogin.addWidget(self.password_label, 1, 2)
        layoutLogin.addWidget(self.password_edit,1 ,3)
        layoutLogin.addWidget(self.login_button, 1, 4)
        layoutLogin.addWidget(self.backButton, 6 ,3)

        self.login_button.clicked.connect(self.login)
        self.backButton.clicked.connect(self.goBack)
        self.login_button.setShortcut(Qt.Key_Return)

        #Set the layout for the window to the stackedWidget
        self.setLayout(layoutLogin)


        
    #Get the username and password
    def login(self):
        username = self.username_edit.text()
        password = self.password_edit.text()

        #Calls the loginController
        loginController.checkLogin(self, self.stackedWidget, username, password)

        self.username_edit.clear()
        self.password_edit.clear()

    #Go back to main page
    def goBack(self):
            self.stackedWidget.setCurrentIndex(0)