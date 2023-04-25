import sys 
sys.path.append('./Controller')
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QStackedWidget, QGridLayout, QMessageBox, QListWidget
from PyQt5 import QtCore, QtGui, QtWidgets
from backButtonController import backButtonController

class manageAcc(QWidget):
    def __init__(self, stackedWidget):
        super().__init__()

        self.stackedWidget = stackedWidget
        

        self.setWindowTitle('Admin')
        font = QtGui.QFont()
        font.setPointSize(16)

        # layout for manage Accounts -----------------------------------
        layoutAcc = QGridLayout()

        #Buttons
        self.labelAcc= QLabel("In accounts")
        self.textBox1 = QListWidget()
        self.buttonCreate= QPushButton("Create Account")
        self.buttonDelete = QPushButton("Delete Account")
        self.buttonEdit = QPushButton("Edit Account")
        self.backButton = QPushButton("Back")
        self.buttonCreate.clicked.connect(self.createAccount)
        self.buttonDelete.clicked.connect(self.remove_line)
        self.buttonEdit.clicked.connect(self.editAccount)

        #self.pushButton1.clicked.connect(self.processHist)
        #self.pushButton2.clicked.connect(self.viewHist)
        self.backButton.clicked.connect(self.goBack)

        layoutAcc.addWidget(self.textBox1,1 ,0 ,4 ,1)
        layoutAcc.addWidget(self.labelAcc,0,0)
        layoutAcc.addWidget(self.buttonCreate, 1 ,1)
        layoutAcc.addWidget(self.buttonDelete, 1 ,2)
        layoutAcc.addWidget(self.buttonEdit, 2 ,1)
        layoutAcc.addWidget(self.backButton, 6 ,3)
        

        self.setLayout(layoutAcc)

    def goBack(self):
        backButtonController.backButtonC(self, self.stackedWidget)
    def createAccount(self):
        # create new window
        self.createAccountWindow = QWidget()
        self.createAccountWindow.setWindowTitle("Create Account")
        layout = QVBoxLayout()

        # Add label and input box
        nameLabel = QLabel("Username:")
        passwordLabel = QLabel("Password:")
        self.nameInput = QLineEdit()
        self.passwordInput = QLineEdit()
        self.passwordInput.setEchoMode(QLineEdit.Password)

        layout.addWidget(nameLabel)
        layout.addWidget(self.nameInput)
        layout.addWidget(passwordLabel)
        layout.addWidget(self.passwordInput)

        # add save button
        saveButton = QPushButton("Save")
        saveButton.clicked.connect(self.saveAccount)

        layout.addWidget(saveButton)
        self.createAccountWindow.setLayout(layout)

        # show new window
        self.createAccountWindow.show()

    def saveAccount(self):
        username = self.nameInput.text()
        password = self.passwordInput.text()
        if username == "" or password == "":
            QMessageBox.warning(self, "Warning", "Please enter username and password")
            return
        self.textBox1.addItem(username + " : " + password)
        QMessageBox.information(self.createAccountWindow, "Success", "Account created successfully.")
        self.createAccountWindow.close()

    def remove_line(self):
        row = self.textBox1.currentRow()
        current_item = self.textBox1.currentItem()
        if current_item is None:
            QMessageBox.warning(self, "Warning", "Please select the data to be removed")
            return
        item = self.textBox1.takeItem(row)
        del item

    def editAccount(self):
        current_item = self.textBox1.currentItem()
        if current_item is None:
            QMessageBox.warning(self, "Warning", "Please select the data to be edited")
            return
        new_text, content = QtWidgets.QInputDialog.getText(self, "Edit Account", "New Username:Password",
                                                           text=current_item.text())
        if content and new_text:
            current_item.setText(new_text)
