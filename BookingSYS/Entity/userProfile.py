#Import to use SQL database
import sqlite3

#GUI Imports
from PyQt5.QtWidgets import QMessageBox

#Import links to different scripts in Boundary
import sys 
sys.path.append('./Boundary')

class UserProfile:
    def viewProfile(self, stackedWidget, item_name):
        self.stackedWidget = stackedWidget
        conn = sqlite3.connect('SilverVillageUserAcc.db')
        # Get a cursor object
        cursor = conn.cursor()
        query = """SELECT * 
                 FROM userProfile 
                 JOIN account ON userProfile.userID = account.userID 
                 WHERE userProfile.userID = ?"""
        value1 = item_name
        # Execute the SQL query to retrieve data from the table
        cursor.execute(query, (value1,))
        # Fetch all the rows that match the query
        rows = cursor.fetchall()

        for row in rows:
            message_box = QMessageBox()
            print(row[0])
            message_box.setText("Account ID: " + str(row[0]) + "\n" + "Name: " + str(row[1]) + "\n" + "Date of Birth: " + str(row[2]) + "\n" + "Account Type: " + str(row[3]))
            message_box.setWindowTitle(str(row[0]))
            message_box.exec_()
        
        # Close the cursor and the database connection
        cursor.close()
        conn.close()
