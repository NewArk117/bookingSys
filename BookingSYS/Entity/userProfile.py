#Import to use SQL database
import sqlite3

#GUI Imports
from PyQt5.QtWidgets import QMessageBox, QLineEdit, QGridLayout, QWidget, QLabel, QTextEdit, QListWidgetItem

import re

#Import links to different scripts in Boundary
import sys 
sys.path.append('./Boundary')

class UserProfile:
    def contains_integer(self, string):
        
        pattern = r'\d+'
        return bool(re.search(pattern, string))
    
    #User story 8
    def createProfile(self, userID, name, age, accType)->str:
        conn = sqlite3.connect('SilverVillageUserAcc.db')

        # Get a cursor object
        cursor = conn.cursor()


        # Insert a new record into the "admin" table
        sql = "INSERT INTO userProfile (userID, name, DOB, accType, suspend) VALUES (?, ?, ?, ?, ?)"
        if name == "" or age == "":
            return "emptyError"
        elif self.contains_integer(name):
            return "integerError"
        elif not re.fullmatch(r'\d+', age):
            return "stringError"
        else:
            data = (userID, name, int(age), accType, True)
            cursor.execute(sql, data)
            # Commit the transaction
            conn.commit()
            # Close the database connection
            conn.close()
            return "Success"
        
    def viewAllProfile(self, stackedWidget, list):
        self.list = list
        #Show Database on textbox
        # Connect to the database
        conn = sqlite3.connect('SilverVillageUserAcc.db')
        
        # Create a cursor object from the connection
        cursor = conn.cursor()
        list.clear()
        # Execute the SQL query to retrieve data from the table
        cursor.execute("SELECT * FROM userProfile")
        
        # Fetch all the rows that match the query
        rows = cursor.fetchall()

        # Iterate over the rows and populate the list widget with the data
        for row in rows:
            item = QListWidgetItem(str(row[0]))
            self.list.addItem(item)

        # Close the cursor and the database connection
        cursor.close()
        conn.close()

    #User story 9
    def viewProfile(self, item_name)->list:
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
        profileDetails = cursor.fetchone()
        # Close the cursor and the database connection
        cursor.close()
        conn.close()
        if profileDetails[2] == False:
            pass
        else:
            return profileDetails
    
    #User story 6
    def editProfile(self, item_name, name, age, accType, suspended)->str:
        if suspended == "True":
            suspended = False
        else:
            suspended = True
        conn = sqlite3.connect('SilverVillageUserAcc.db')
        cursor = conn.cursor()

        update_query = "UPDATE userProfile SET name = ?, DOB = ?, accType = ?, suspend = ? WHERE userID = ?"
        
        if name == "" or age == "":
            return "emptyError"
        elif self.contains_integer(name):
            return "integerError"
        elif not re.fullmatch(r'\d+', age):
            return "stringError"
        else:
            values = (name, age, accType, suspended, item_name)
            cursor.execute(update_query, values)
            conn.commit()
            cursor.close()
            conn.close()
            return "Success"
        
    #User Story 12    
    def searchProfile(self, stackedWidget, item_name, list)->list:
        self.stackedWidget = stackedWidget
        self.list = list

        if item_name != "":
            conn = sqlite3.connect('SilverVillageUserAcc.db')
            cursor = conn.cursor()
            list.clear()
            sql = "SELECT * FROM userProfile WHERE userID = ?"
            value1 = item_name
            cursor.execute(sql, (value1,))
            
            rows = cursor.fetchall()
            
            for row in rows:
                item = QListWidgetItem(str(row[0]))
                self.list.addItem(item)


            # Close the cursor and the database connection
            cursor.close()
            conn.close()
            
            return list
        
        else:
            # Connect to the database
            conn = sqlite3.connect('SilverVillageUserAcc.db')
            
            # Create a cursor object from the connection
            cursor = conn.cursor()
            list.clear()
            # Execute the SQL query to retrieve data from the table
            cursor.execute("SELECT * FROM userProfile")
            
            # Fetch all the rows that match the query
            rows = cursor.fetchall()

            # Iterate over the rows and populate the list widget with the data
            for row in rows:
                item = QListWidgetItem(str(row[0]))
                self.list.addItem(item)

            # Close the cursor and the database connection
            cursor.close()
            conn.close()
            return list
        
    #User Story 11
    def suspendProfile(self, item_name)->str:
        conn = sqlite3.connect('SilverVillageUserAcc.db')
        cursor = conn.cursor()

        update_query = "UPDATE userProfile SET suspend = ? WHERE userID = ?"
        values = (False, item_name)
        cursor.execute(update_query, values)
        conn.commit()
        cursor.close()
        conn.close()
        return "changed"