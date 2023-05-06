#Import to use SQL database
import sqlite3

#GUI Imports
from PyQt5.QtWidgets import QMessageBox, QListWidgetItem

#Import links to different scripts in Boundary
import sys 
sys.path.append('./Boundary')

class UserProfile:
    def viewProfile(self,stackedWidget, item_name):
        self.stackedWidget = stackedWidget
        self.item_name = item_name
        view_items = []
        conn = sqlite3.connect('SilverVillageUserAcc.db')

        # Get a cursor object
        cursor = conn.cursor()

        # Execute the SQL query to retrieve data from the table
        cursor.execute("SELECT * FROM userProfile JOIN account on userProfile.userID = account.userID")

        # Fetch all the rows that match the query
        rows = cursor.fetchall()
        print(rows)
        # Iterate over the rows and populate the list widget with the data

        # Close the cursor and the database connection
        cursor.close()
        conn.close()
