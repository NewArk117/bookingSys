#Import to use SQL database
import sqlite3

#GUI Imports
from PyQt5.QtWidgets import QMessageBox, QLineEdit, QGridLayout, QWidget, QLabel, QTextEdit, QListWidgetItem
from PyQt5.QtCore import Qt

#Import links to different scripts in Boundary
import sys 
sys.path.append('./Boundary')

class Account:
    #User Story 1/13
    def login(self, userID, password)->str:
        conn = sqlite3.connect('SilverVillageUserAcc.db')
        # Get a cursor object
        cursor = conn.cursor()

        #SQL Statement
        sql = "SELECT * FROM account WHERE userID = ? AND password = ?"
        value1 = userID
        value2 = password

        # Execute the SQL query with the values
        cursor.execute(sql, (value1, value2))
        
        row = cursor.fetchone()

        if row is None:
            return "error"
        elif row[3] == False:
            return "locked"
        else:
            user = str(row[2])
            #Close Transaction 
            cursor.close()
            conn.close()
            return user  
            
    #User Story 2
    def logout(self):
        return True

    #User Story 3    
    def createAccount(self, userID, password, accType)->str:

        conn = sqlite3.connect('SilverVillageUserAcc.db')

        # Get a cursor object
        cursor = conn.cursor()
        checkUser = []
        checkID = []
        checkPw = []
        cursor.execute("SELECT * FROM account")
        rows = cursor.fetchall()
        for row in rows:
            checkID.append(row[0])
            checkUser.append(row[1])
            checkPw.append(row[2])

        # Insert a new record into the account table
        sql = "INSERT INTO account (userID, password, accType, suspend) VALUES (?, ?, ?, ?)"
        data = (userID, password, accType, True)
        if data[0] == "" or data[1] == "":
            return "emptyError"
        elif data[0] in checkID:
            return "IDError"
        else:
            cursor.execute(sql, data)
            # Commit the transaction
            conn.commit()
            # Close the database connection
            conn.close()
            return "Success"
            
    #User Story 5
    def editAccount(self, item_name, line, suspended)->bool:
        if suspended == "True":
            suspended = False
        else:
            suspended = True
        conn = sqlite3.connect('SilverVillageUserAcc.db')
        cursor = conn.cursor()

        update_query = "UPDATE account SET password = ?, suspend = ? WHERE userID = ?"
        if line != "":
            values = (line, suspended, item_name)
            cursor.execute(update_query, values)
            conn.commit()
            cursor.close()
            conn.close()
            return True
        else:
            return False
    #User Story 4    
    def viewAccount(self, item_name)->list:
        conn = sqlite3.connect('SilverVillageUserAcc.db')
        # Get a cursor object
        cursor = conn.cursor()
        query = """SELECT * 
                 FROM account 
                 WHERE account.userID = ?"""
        value1 = item_name
        # Execute the SQL query to retrieve data from the table
        cursor.execute(query, (value1,))
        # Fetch all the rows that match the query
        accountDetails = cursor.fetchone()
        # Close the cursor and the database connection
        cursor.close()
        conn.close()

        return accountDetails
        
        
    def viewAllAccount(self, stackedWidget, list):
        self.list = list
        # Connect to the database
        conn = sqlite3.connect('SilverVillageUserAcc.db')
        
        # Create a cursor object from the connection
        cursor = conn.cursor()
        list.clear()
        # Execute the SQL query to retrieve data from the table
        cursor.execute("SELECT * FROM account")
        
        # Fetch all the rows that match the query
        rows = cursor.fetchall()

        # Iterate over the rows and populate the list widget with the data
        for row in rows:
            item = QListWidgetItem(str(row[0]))
            self.list.addItem(item)

        # Close the cursor and the database connection
        cursor.close()
        conn.close()
    
    #User Story 7
    def searchAccount(self, stackedWidget, item_name, list)->list:
        self.stackedWidget = stackedWidget
        self.list = list

        if item_name != "":
            conn = sqlite3.connect('SilverVillageUserAcc.db')
            cursor = conn.cursor()
            list.clear()
            sql = "SELECT * FROM account WHERE userID = ?"
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
            cursor.execute("SELECT * FROM account")
            
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
    
    #User Story 6
    def suspendAccount(self, item_name)->str:
        conn = sqlite3.connect('SilverVillageUserAcc.db')
        cursor = conn.cursor()

        update_query = "UPDATE account SET suspend = ? WHERE userID = ?"
        values = (False, item_name)
        cursor.execute(update_query, values)
        conn.commit()
        cursor.close()
        conn.close()
        return "changed"
        
    def process_registration(self, stackedWidget, dialog, id, password, confirm_password, name, age):
        if password == confirm_password:
            # Connect to thedatabase
            conn = sqlite3.connect('SilverVillageUserAcc.db')
            cursor = conn.cursor()
            try:
                # Check if ID already exists
                cursor.execute("SELECT * FROM account WHERE userID=?", (id,))
                if cursor.fetchone():
                    QMessageBox.critical(dialog, 'Error', 'ID already exists. Please enter a new ID.')
                else:
                    # Insert registration details into the database
                    cursor.execute(
                        "INSERT INTO account (userID, password, accType) VALUES (?, ?, ?)",
                        (id, password, 'customer'))
                    cursor.execute(
                        "INSERT INTO userProfile (userID, name, DOB, accType, suspend) VALUES (?, ?, ?, ?, ?)",
                        (id, name, int(age), 'customer', 1))

                    conn.commit()

                    # Registration successful
                    QMessageBox.information(dialog, 'Success', 'Registration successful.')
                    dialog.accept()
            except Exception as e:
                # Handle database errors
                QMessageBox.critical(dialog, 'Error', 'An error occurred during registration: {}'.format(str(e)))
        else:
            # Passwords do not match
            QMessageBox.critical(dialog, 'Error', 'Passwords do not match.')

    def get_info(self, user_id):
        conn = sqlite3.connect('SilverVillageUserAcc.db')
        cursor = conn.cursor()
        sql = 'SELECT name, DOB FROM userProfile WHERE userID = ?'
        cursor.execute(sql, (user_id,))
        result = cursor.fetchone()

        conn.close()
        name, Dob=result

        return name,Dob

    def update_account_info(self, user_id, new_user_id, new_username, DOB):
        conn = sqlite3.connect('SilverVillageUserAcc.db')
        cursor = conn.cursor()

        sql = '''
        UPDATE account
        SET userID = ?
        WHERE userID = ?
        '''
        cursor.execute(sql, (new_user_id, user_id))
        sql = '''UPDATE userProfile
        SET userID = ?, name = ?,DOB = ?
        WHERE userID = ?'''
        cursor.execute(sql, (new_user_id, new_username, int(DOB), user_id))

        conn.commit()
        conn.close()


    def update_food_orders_user_id(self, user_id, new_user_id):
        conn = sqlite3.connect('SilverVillageUserAcc.db')
        cursor = conn.cursor()

        sql = '''
        UPDATE food_orders
        SET user_id = ?
        WHERE user_id = ?;
        '''
        cursor.execute(sql, (new_user_id, user_id))
        conn.commit()

        cursor.close()
        conn.close()

    def update_ticket_user_id(self, user_id, new_user_id):
        conn = sqlite3.connect('SilverVillageUserAcc.db')
        cursor = conn.cursor()

        sql = '''
        UPDATE ticket
        SET userID = ?
        WHERE userID = ?;
        '''
        cursor.execute(sql, (new_user_id, user_id))
        conn.commit()

        cursor.close()
        conn.close()


    def get_password(self, user_id):
        conn = sqlite3.connect('SilverVillageUserAcc.db')
        cursor = conn.cursor()

        sql = '''
        SELECT password
        FROM account
        WHERE userID = ?
        '''
        cursor.execute(sql, (user_id,))
        result = cursor.fetchone()

        conn.close()

        return result[0] if result else None

    def update_password(self, user_id, new_password):
        conn = sqlite3.connect('SilverVillageUserAcc.db')
        cursor = conn.cursor()

        sql = '''
        UPDATE account
        SET password = ?
        WHERE userID = ?
        '''
        cursor.execute(sql, (new_password, user_id))
        conn.commit()

        conn.close()

    def is_user_id_exists(self, user_id):
        conn = sqlite3.connect('SilverVillageUserAcc.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM account WHERE userID = ?", (user_id,))
        result = cursor.fetchone()
        cursor.close()
        conn.close()
        return result is not None





