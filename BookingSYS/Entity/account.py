#Import to use SQL database
import sqlite3

#GUI Imports
from PyQt5.QtWidgets import QMessageBox

#Import links to different scripts in Boundary
import sys 
sys.path.append('./Boundary')

class Account:
    def login(self,stackedWidget, usrname, pw):
        self.stackedWidget = stackedWidget

        conn = sqlite3.connect('SilverVillageUserAcc.db')

        # Get a cursor object
        cursor = conn.cursor()

        #SQL Statement
        sql = "SELECT * FROM account WHERE userName = ? AND password = ?"
        value1 = usrname
        value2 = pw

        # Execute the SQL query with the values
        cursor.execute(sql, (value1, value2))

        rows = cursor.fetchall()
        
        for row in rows:
            if row[1] == usrname:
                if row[2] == pw:
                    self.stackedWidget.setCurrentIndex(2)
                else:
                    print("Wrong password")
            #if else to check with usrname and pw with database, if match then go to customer UI
            else:
                print('Invalid username')

        #Close Transaction 
        cursor.close()
        conn.close()

    def logout(self,stackedWidget):
        self.stackedWidget = stackedWidget

        reply = QMessageBox.question(self.stackedWidget, 'Confirm logout',
                                    'Are you sure you want to logout?',
                                    QMessageBox.Yes | QMessageBox.No,
                                    QMessageBox.No)
        
        if reply == QMessageBox.Yes:
            self.stackedWidget.setCurrentIndex(1)

    def createInfo(self,stackedWidget, userID, userName, password, permission):
        self.stackedWidget = stackedWidget

        conn = sqlite3.connect('SilverVillageUserAcc.db')

        # Get a cursor object
        cursor = conn.cursor()

        # Insert a new record into the account table
        sql = "INSERT INTO account (userID, userName, password, permission) VALUES (?, ?, ?, ?)"
        data = (userID, userName, password, permission)
        cursor.execute(sql, data)

        # Commit the transaction
        conn.commit()

        # Close the database connection
        conn.close()
        self.stackedWidget.setCurrentIndex(3)

    def createProfile(self,stackedWidget, userID, name, DOB, accType):
        self.stackedWidget = stackedWidget
        
        conn = sqlite3.connect('SilverVillageUserAcc.db')

        # Get a cursor object
        cursor = conn.cursor()

        # Insert a new record into the "admin" table
        sql = "INSERT INTO userProfile (userID, name, DOB, accType) VALUES (?, ?, ?, ?)"
        data = (userID, name, DOB, accType)
        cursor.execute(sql, data)

        # Commit the transaction
        conn.commit()

        # Close the database connection
        conn.close()
        self.stackedWidget.setCurrentIndex(3)
