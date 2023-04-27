import sys 
sys.path.append('./Controller')
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QStackedWidget, QGridLayout, QMessageBox, QListWidget
from PyQt5 import QtCore, QtGui, QtWidgets
from backButtonController import backButtonController

#widget index 4
class manageProf(QWidget):
    def __init__(self, stackedWidget):
        super().__init__()

        self.stackedWidget = stackedWidget
    
        self.setWindowTitle('Admin')
        font = QtGui.QFont()
        font.setPointSize(16)

        layoutProf = QGridLayout()

        #Buttons
        self.labelProf= QLabel("In profiles")
        self.textBox2 = QListWidget()
        self.buttonCreate2= QPushButton("Create Profile")
        self.buttonDelete2 = QPushButton("Delete Profile")
        self.buttonEdit2 = QPushButton("Edit Profile")
        self.backButton = QPushButton("Back")

        #self.pushButton1.clicked.connect(self.processHist)
        #self.pushButton2.clicked.connect(self.viewHist)
        self.backButton.clicked.connect(self.goBack)
        self.buttonCreate2.clicked.connect(self.goCreateProf)

        layoutProf.addWidget(self.textBox2,1 ,0 ,4 ,1)
        layoutProf.addWidget(self.labelProf,0,0)
        layoutProf.addWidget(self.buttonCreate2, 1 ,1)
        layoutProf.addWidget(self.buttonDelete2, 1 ,2)
        layoutProf.addWidget(self.buttonEdit2, 2 ,1)
        layoutProf.addWidget(self.backButton, 6 ,3)

        self.setLayout(layoutProf)


    def goBack(self):
        backButtonController.backButtonC(self, self.stackedWidget)
    
    def goCreateProf(self):
        self.stackedWidget.setCurrentIndex(6)