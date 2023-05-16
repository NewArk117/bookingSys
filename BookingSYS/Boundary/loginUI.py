#GUI imports
import sqlite3

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QGridLayout, QMessageBox, QDialog, QFormLayout

#Import links to different scripts in Controller
import sys
sys.path.append('./Controller')
from loginController import loginController
from userRegController import userRegController

#Admin Login

class loginUI(QWidget):
    def __init__(self, stackedWidget):
        super().__init__()
        self.stackedWidget = stackedWidget
        self.userRegController = userRegController()

        # Create the login form
        self.username_label = QLabel('Username:')
        self.username_edit = QLineEdit()
        self.password_label = QLabel('Password:')
        self.password_edit = QLineEdit()
        self.password_edit.setEchoMode(QLineEdit.Password)
        self.login_button = QPushButton('Login')
        self.register_button = QPushButton('Register')  # Added register button
        self.backButton = QPushButton('Back')

        # Create the layout
        layoutLogin = QGridLayout()
        layoutLogin.addWidget(self.username_label, 1, 0)
        layoutLogin.addWidget(self.username_edit, 1, 1)
        layoutLogin.addWidget(self.password_label, 1, 2)
        layoutLogin.addWidget(self.password_edit, 1, 3)
        layoutLogin.addWidget(self.login_button, 1, 4)
        layoutLogin.addWidget(self.register_button, 2, 4)  # Added register button to the layout
        layoutLogin.addWidget(self.backButton, 6, 3)

        self.login_button.clicked.connect(self.login)
        self.register_button.clicked.connect(self.register)  # Connect register button to a function
        self.backButton.clicked.connect(self.goBack)
        self.login_button.setShortcut(Qt.Key_Return)

        # Set the layout for the window to the stackedWidget
        self.setLayout(layoutLogin)

    def register(self):
        # Handle register button click event
        register_dialog = QDialog(self)
        register_dialog.setWindowTitle('Register')
        register_dialog.setModal(True)

        # Create form widgets
        id_label = QLabel('UserID:')
        id_edit = QLineEdit()
        username_label = QLabel('Username:')
        username_edit = QLineEdit()
        password_label = QLabel('Password:')
        password_edit = QLineEdit()
        password_edit.setEchoMode(QLineEdit.Password)
        confirm_password_label = QLabel('Confirm Password:')
        confirm_password_edit = QLineEdit()
        confirm_password_edit.setEchoMode(QLineEdit.Password)
        register_button = QPushButton('Register')

        # Create the layout for the register dialog
        layout = QFormLayout()
        layout.addRow(id_label, id_edit)
        layout.addRow(username_label, username_edit)
        layout.addRow(password_label, password_edit)
        layout.addRow(confirm_password_label, confirm_password_edit)
        layout.addRow(register_button)

        # Set the layout for the register dialog
        register_dialog.setLayout(layout)

        # Connect register button to a function
        register_button.clicked.connect(
            lambda: self.process_registration(register_dialog, id_edit.text(), username_edit.text(),
                                              password_edit.text(),
                                              confirm_password_edit.text()))

        # Show the register dialog
        register_dialog.exec_()

    def process_registration(self, dialog, id, username, password, confirm_password):
        self.userRegController.process_registration(dialog, id, username, password, confirm_password)

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


