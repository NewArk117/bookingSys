#Import to use SQL database
import sqlite3

#GUI imports
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QGridLayout, QListWidget, QListWidgetItem
from PyQt5 import QtGui

#Import links to different scripts in Controller
import sys 
sys.path.append('./Controller')
from backButtonController import backButtonController

#Admin profile main page GUI
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

        self.backButton.clicked.connect(self.goBack)
        self.buttonCreate2.clicked.connect(self.goCreateProf)

        layoutProf.addWidget(self.textBox2,1 ,0 ,4 ,1)
        layoutProf.addWidget(self.labelProf,0,0)
        layoutProf.addWidget(self.buttonCreate2, 1 ,1)
        layoutProf.addWidget(self.buttonDelete2, 1 ,2)
        layoutProf.addWidget(self.buttonEdit2, 2 ,1)
        layoutProf.addWidget(self.backButton, 6 ,3)

        self.setLayout(layoutProf)

         # Connect to the database
        conn = sqlite3.connect('SilverVillageUserAcc.db')
        
        # Create a cursor object from the connection
        cursor = conn.cursor()
        
        # Execute the SQL query to retrieve data from the table
        cursor.execute("SELECT * FROM userProfile JOIN admin ON userProfile.userID = admin.userID ")
        
        # Fetch all the rows that match the query
        rows = cursor.fetchall()

        # Iterate over the rows and populate the list widget with the data
        for row in rows:
            item = QListWidgetItem(str(row[1]))
            self.textBox2.addItem(item)

        # Close the cursor and the database connection
        cursor.close()
        conn.close()

        #QTimer to periodically refresh the list widget
        self.timer = QTimer()
        self.timer.timeout.connect(self.refreshAcc)
        self.timer.start(1000) # refresh every 1 second

    def goBack(self):
        backButtonController.backButtonC(self, self.stackedWidget)
    
    def goCreateProf(self):
        self.stackedWidget.setCurrentIndex(6)

    def refreshAcc(self):
        # connect to the database
        conn = sqlite3.connect('SilverVillageUserAcc.db')

        # execute a query to retrieve data from the database
        cursor = conn.execute("SELECT * FROM userProfile JOIN admin ON userProfile.userID = admin.userID ")

        # clear the list widget
        self.textBox2.clear()

        # populate the list widget with data from the query
        for row in cursor:
            item = QListWidgetItem(str(row[1]))
            self.textBox2.addItem(item)

        # close the database connection
        conn.close()