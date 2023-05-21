#Import to use SQL database
import sqlite3

#GUI Imports
from PyQt5.QtWidgets import QMessageBox, QLineEdit, QGridLayout, QWidget, QLabel, QTextEdit, QListWidgetItem
from PyQt5.QtCore import Qt

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
        loginTitle = "Login Successful"
        loginMessage = "You have successfully logged in."
        loginTitleF = "Login Error"
        loginWarning = "Wrong Username or Password."
        row = cursor.fetchone()
        widget1 = QWidget()
        if row:
            QMessageBox.information(widget1, loginTitle, loginMessage)
            if row[3] == 'sysAdmin':
                self.stackedWidget.setCurrentIndex(2)
            elif row[3] == 'customer':
                widget = self.stackedWidget.widget(6)
                widget.setID(row[0])
                self.stackedWidget.setCurrentIndex(6)
            elif row[3] == 'cinemaManager':
                self.stackedWidget.setCurrentIndex(9)
        else:
            QMessageBox.warning(widget1, loginTitleF, loginWarning)


        #Close Transaction 
        cursor.close()
        conn.close()

    def logout(self,stackedWidget):
        self.stackedWidget = stackedWidget
        self.stackedWidget.setCurrentIndex(0)
        #reply = QMessageBox.question(self.stackedWidget, 'Confirm logout',
                                   # 'Are you sure you want to logout?',
                                   # QMessageBox.Yes | QMessageBox.No)
        
        #if reply == QMessageBox.Yes:
            #self.stackedWidget.setCurrentIndex(0)

    def createAccount(self,stackedWidget, userID, userName, password, accType):
        self.stackedWidget = stackedWidget
        widget2 = QWidget()
        conn = sqlite3.connect('SilverVillageUserAcc.db')

        # Get a cursor object
        cursor = conn.cursor()
        checkUser = []
        checkID = []
        checkPw = []
        checkPer = []
        cursor.execute("SELECT * FROM account")
        rows = cursor.fetchall()
        for row in rows:
            checkID.append(row[0])
            checkUser.append(row[1])
            checkPw.append(row[2])
            checkPer.append(row[3])

        createErrorTitle = "Invalid Input"
        emptyError = "A column is empty please fill up all the details"
        IDError = "ID already in used"
        userError = "Username already in used"

        # Insert a new record into the account table
        sql = "INSERT INTO account (userID, userName, password, permission) VALUES (?, ?, ?, ?)"
        data = (userID, userName, password, accType)
        if data[0] == "" or data[1] == "" or data[2] == "" or data[3] == "":
            QMessageBox.information(widget2, createErrorTitle, emptyError)
        elif data[0] in checkID:
            QMessageBox.information(widget2, createErrorTitle, IDError)
        elif data[1] in checkUser:
            QMessageBox.information(widget2,createErrorTitle, userError)
        else:
            cursor.execute(sql, data)

            # Commit the transaction
            conn.commit()
            # Close the database connection
            conn.close()
            self.stackedWidget.setCurrentIndex(3)
    def editAccount(self, stackedWidget, item_name):
        self.stackedWidget = stackedWidget
        widget = QWidget()
        conn = sqlite3.connect('SilverVillageUserAcc.db')

        # Get a cursor object
        cursor = conn.cursor()
        checkUser = []
        checkID = []
        checkPw = []
        checkPer = []
        cursor.execute("SELECT * FROM account")
        rowChecker = cursor.fetchall()
        for checker in rowChecker:
            checkID.append(checker[0])
            checkUser.append(checker[1])
            checkPw.append(checker[2])
            checkPer.append(checker[3])

        sql = "SELECT * FROM account WHERE userID = ?"
        value1 = item_name

        cursor.execute(sql, (value1,))

        rows = cursor.fetchall()


        for row in rows:
            message_box = QMessageBox()
            message_box.setWindowTitle(str(row[0]))
            message_box.setText('Edit Account')

            field_labels = ["Username:", "Password:", "Permission:"]
            layout = QGridLayout()

            for label_text in field_labels:
                    label = QLabel(label_text)
                    
                    i = 0
                    if label_text == "Username:":
                        line_edit = QLineEdit(str(row[1]))
                        layout.addWidget(label,1,0)
                        layout.addWidget(line_edit,1,1)      
                    elif label_text == "Password:":
                        line_edit = QLineEdit(str(row[2]))
                        layout.addWidget(label,2,0)
                        layout.addWidget(line_edit,2,1)
                    else:
                        line_edit = QLineEdit(str(row[3]))
                        layout.addWidget(label,3,0)
                        layout.addWidget(line_edit,3,1)

            # Create a widget to hold the layout and set it as the message box's body
            widget = QWidget()
            widget.setLayout(layout)
            message_box.layout().addWidget(widget)
            message_box.addButton(QMessageBox.Ok)
            
            while True:
                result = message_box.exec_()
                if result == QMessageBox.Ok:
                    texts = [line_edit.text() for line_edit in widget.findChildren(QLineEdit)]
                    if texts[0] == "" or texts[1] == "" or texts[2] == "":
                        QMessageBox.information(widget,"Invalid Input", "A column is empty please fill up all the details")
                    elif texts[0] in checkUser and texts[1] not in checkPw:
                        conn = sqlite3.connect('SilverVillageUserAcc.db')
                        c = conn.cursor()

                        sql1 = "DELETE FROM account WHERE account.userID = ?"
                        c.execute(sql1,(row[0],))

                        c.execute("INSERT INTO account (userID, userName, password, permission) VALUES (?, ?, ?, ?)", (row[0],texts[0], texts[1], texts[2]))
                        conn.commit()
                        conn.close()
                        return False
                    
                    elif texts[1] in checkPw and texts[0] not in checkUser:
                        conn = sqlite3.connect('SilverVillageUserAcc.db')
                        c = conn.cursor()

                        sql1 = "DELETE FROM account WHERE account.userID = ?"
                        c.execute(sql1,(row[0],))
                
                        c.execute("INSERT INTO account (userID, userName, password, permission) VALUES (?, ?, ?, ?)", (row[0],texts[0], texts[1], texts[2]))

                        conn.commit()
                        conn.close()
                        return False
                    
                    elif texts[1] not in checkPw and texts[0] not in checkUser:
                        conn = sqlite3.connect('SilverVillageUserAcc.db')
                        c = conn.cursor()

                        sql1 = "DELETE FROM account WHERE account.userID = ?"
                        c.execute(sql1,(row[0],))

                        c.execute("INSERT INTO account (userID, userName, password, permission) VALUES (?, ?, ?, ?)", (row[0],texts[0], texts[1], texts[2]))

                        conn.commit()
                        conn.close()
                        return False
                    
                    elif QMessageBox.Cancel:
                        return False
                    else:
                        QMessageBox.information(widget,"Invalid Input", "Username and Password already in used")
                    
                        
    def viewAccount(self, stackedWidget, item_name):
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
        rows = cursor.fetchall()

        for row in rows:
            message_box = QMessageBox()
            message_box.setText("Account ID: " + str(row[0]) + "\n" + "Username: " + str(row[1]) + "\n" + "Password: " + str(row[2]) + "\n" + "Permission: " + str(row[3]))
            message_box.setWindowTitle(str(row[0]))
            message_box.exec_()
        
        # Close the cursor and the database connection
        cursor.close()
        conn.close()

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
    
    def searchAccount(self, stackedWidget, item_name, list):
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
            # Iterate over the rows and populate the list widget with the data
            for row in rows:
                item = QListWidgetItem(str(row[0]))
                self.list.addItem(item)

            # Close the cursor and the database connection
            cursor.close()
            conn.close()
        else:
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
    def process_registration(self, stackedWidget, dialog, id, username, password, confirm_password):
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
                    # Check if username already exists
                    cursor.execute("SELECT * FROM account WHERE userName=?", (username,))
                    if cursor.fetchone():
                        QMessageBox.critical(dialog, 'Error', 'Username already exists.')
                    else:
                        # Insert registration details into the database
                        cursor.execute(
                            "INSERT INTO account (userID, userName, password, permission) VALUES (?, ?, ?, ?)",
                            (id, username, password, 'customer'))
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

    def get_username(self, user_id):
        conn = sqlite3.connect('SilverVillageUserAcc.db')
        cursor = conn.cursor()

        sql = '''
        SELECT userName
        FROM account
        WHERE userID = ?
        '''
        cursor.execute(sql, (user_id,))
        result = cursor.fetchone()

        conn.close()

        return result[0] if result else None

    def update_account_info(self, user_id, new_user_id, new_username):
        conn = sqlite3.connect('SilverVillageUserAcc.db')
        cursor = conn.cursor()

        sql = '''
        UPDATE account
        SET userID = ?,
            userName = ?
        WHERE userID = ?
        '''
        cursor.execute(sql, (new_user_id, new_username, user_id))
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

    def update_user_profile_user_id(self, user_id, new_user_id):
        conn = sqlite3.connect('SilverVillageUserAcc.db')
        cursor = conn.cursor()

        sql = '''
        UPDATE userProfile
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


