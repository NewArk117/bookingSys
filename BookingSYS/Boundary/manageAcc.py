import sys 
sys.path.append('./Controller')
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QStackedWidget, QGridLayout, QMessageBox, QListWidget
from PyQt5 import QtCore, QtGui, QtWidgets
from backButtonController import backButtonController
from createAccController import createAccController

#widget index 3
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

        #self.pushButton1.clicked.connect(self.processHist)
        #self.pushButton2.clicked.connect(self.viewHist)
        self.backButton.clicked.connect(self.goBack)
        self.buttonCreate.clicked.connect(self.goCreateAcc)

        layoutAcc.addWidget(self.textBox1,1 ,0 ,4 ,1)
        layoutAcc.addWidget(self.labelAcc,0,0)
        layoutAcc.addWidget(self.buttonCreate, 1 ,1)
        layoutAcc.addWidget(self.buttonDelete, 1 ,2)
        layoutAcc.addWidget(self.buttonEdit, 2 ,1)
        layoutAcc.addWidget(self.backButton, 6 ,3)
        

        self.setLayout(layoutAcc)

    def goBack(self):
        backButtonController.backButtonC(self, self.stackedWidget)

    def goCreateAcc(self):
        self.stackedWidget.setCurrentIndex(5)