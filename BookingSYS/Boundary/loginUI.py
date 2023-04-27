import sys 
sys.path.append('./Controller')
#sys.path.append('C:/Users/USER/Desktop/BookingSys/bookingSys/BookingSYS/Controller')
from adminLoginController import adminLoginController
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QStackedWidget, QGridLayout


class loginUI(QWidget):
    def __init__(self, stackedWidget):
        super().__init__()

        self.stackedWidget = stackedWidget
    
        self.setWindowTitle('Login')

       # create the login form
        self.username_label = QLabel('Username:')
        self.username_edit = QLineEdit()
        self.password_label = QLabel('Password:')
        self.password_edit = QLineEdit()
        self.password_edit.setEchoMode(QLineEdit.Password)
        self.login_button = QPushButton('Login')

        # create the layout
        layoutLogin = QGridLayout()
        layoutLogin.addWidget(self.username_label, 1, 0)
        layoutLogin.addWidget(self.username_edit, 1, 1)
        layoutLogin.addWidget(self.password_label, 1, 2)
        layoutLogin.addWidget(self.password_edit,1 ,3)
        layoutLogin.addWidget(self.login_button, 1, 4)


        self.login_button.clicked.connect(self.login)
        self.login_button.setShortcut(Qt.Key_Return)

        # set the layout for the window to the stackedWidget
        self.setLayout(layoutLogin)


        # get the username and password
        


    def login(self):
        username = self.username_edit.text()
        password = self.password_edit.text()
        #print("This is the username" + username)
        #print("This is the pw" + password)
        adminLoginController.addStaff(self, self.stackedWidget, username, password)
        self.username_edit.clear()
        self.password_edit.clear()
