#Import to use SQL database
import sqlite3

#GUI imports
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import  QWidget, QLabel, QPushButton, QGridLayout, QListWidget, QListWidgetItem

#Import links to different scripts in Controller
import sys 
sys.path.append('./Controller')
from PyQt5 import QtGui
from backButtonController import backButtonController
from createAccController import createAccController

#Admin account main page GUI
class manageAcc(QWidget):
    def __init__(self, stackedWidget):
        super().__init__()

        self.stackedWidget = stackedWidget
        
        self.setWindowTitle('Admin')
        font = QtGui.QFont()
        font.setPointSize(16)

        #layout for manage accounts 
        layoutAcc = QGridLayout()

        #Buttons
        self.labelAcc= QLabel("In accounts")
        self.textBox1 = QListWidget()
        self.buttonCreate= QPushButton("Create Account")
        self.buttonDelete = QPushButton("Delete Account")
        self.buttonEdit = QPushButton("Edit Account")
        self.backButton = QPushButton("Back")

        self.backButton.clicked.connect(self.goBack)
        self.buttonCreate.clicked.connect(self.goCreateAcc)


        layoutAcc.addWidget(self.textBox1,1 ,0 ,4 ,1)
        layoutAcc.addWidget(self.labelAcc,0,0)
        layoutAcc.addWidget(self.buttonCreate, 1 ,1)
        layoutAcc.addWidget(self.buttonDelete, 1 ,2)
        layoutAcc.addWidget(self.buttonEdit, 2 ,1)
        layoutAcc.addWidget(self.backButton, 6 ,3)
        
        self.setLayout(layoutAcc)

        #Show Database on textbox
        # Connect to the database
        conn = sqlite3.connect('SilverVillageUserAcc.db')
        
        # Create a cursor object from the connection
        cursor = conn.cursor()
        
        # Execute the SQL query to retrieve data from the table
        cursor.execute("SELECT * FROM admin")
        
        # Fetch all the rows that match the query
        rows = cursor.fetchall()

        # Iterate over the rows and populate the list widget with the data
        for row in rows:
            item = QListWidgetItem(str(row[1]))
            self.textBox1.addItem(item)

        # Close the cursor and the database connection
        cursor.close()
        conn.close()
        
        #QTimer to periodically refresh the list widget
        self.timer = QTimer()
        self.timer.timeout.connect(self.refreshAcc)
        self.timer.start(1000) # refresh every 1 second

    def deleteAcc(self):
        backButtonController.backButtonC(self, self.stackedWidget)

    def goBack(self):
        backButtonController.backButtonC(self, self.stackedWidget)

    def goCreateAcc(self):
        self.stackedWidget.setCurrentIndex(5)

    def refreshAcc(self):
        # connect to the database
        conn = sqlite3.connect('SilverVillageUserAcc.db')

        # execute a query to retrieve data from the database
        cursor = conn.execute("SELECT * FROM admin")

        # clear the list widget
        self.textBox1.clear()

        # populate the list widget with data from the query
        for row in cursor:
            item = QListWidgetItem(str(row[1]))
            self.textBox1.addItem(item)

        # close the database connection
        conn.close()
        

        