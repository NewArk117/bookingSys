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

        row = cursor.fetchone()
        widget1 = QWidget()
        if row:
            QMessageBox.information(widget1,"Login Successful", "You have successfully logged in.")
            if row[3] == 'sysAdmin':
                self.stackedWidget.setCurrentIndex(2)
            elif row[3] == 'customer':
                self.stackedWidget.setCurrentIndex(6)
            elif row[3] == 'cinemaManager':
                self.stackedWidget.setCurrentIndex(9)
        else:
            QMessageBox.warning(widget1,"Login Error", "Wrong Username or Password.")
                    

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
            self.stackedWidget.setCurrentIndex(0)

    def createAccount(self,stackedWidget, userID, userName, password, permission):
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

        # Insert a new record into the account table
        sql = "INSERT INTO account (userID, userName, password, permission) VALUES (?, ?, ?, ?)"
        data = (userID, userName, password, permission)
        if data[0] == "" or data[1] == "" or data[2] == "" or data[3] == "":
            QMessageBox.information(widget2,"Invalid Input", "A column is empty please fill up all the details")
        elif data[0] in checkID:
            QMessageBox.information(widget2,"Invalid Input", "ID already in used")
        elif data[1] in checkUser:
            QMessageBox.information(widget2,"Invalid Input", "Username already in used")
        elif data[2] in checkUser:
            QMessageBox.information(widget2,"Invalid Input", "Password already in used")
        else:
            cursor.execute(sql, data)
            self.stackedWidget.setCurrentIndex(3)

            # Commit the transaction
            conn.commit()


            # Close the database connection
            conn.close()

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
                    elif texts[0] in checkUser:
                        QMessageBox.information(widget,"Invalid Input", "Username already in used")
                    elif texts[1] in checkPw:
                        QMessageBox.information(widget,"Invalid Input", "Password already in used")
                    else:
                        conn = sqlite3.connect('SilverVillageUserAcc.db')
                        c = conn.cursor()
                        sql1 = "DELETE FROM account WHERE account.userID = ?"
                        c.execute(sql1,(row[0],))
                        c.execute("INSERT INTO account (userID, userName, password, permission) VALUES (?, ?, ?, ?)", (row[0],texts[0], texts[1], texts[2]))

                        conn.commit()
                        conn.close()
                        return False

    def viewAccount(self, stackedWidget):
        # Connect to the database
        conn = sqlite3.connect('SilverVillageUserAcc.db')
        
        # Create a cursor object from the connection
        cursor = conn.cursor()
        
        # Execute the SQL query to retrieve data from the table
        cursor.execute("SELECT * FROM account")
        
        # Fetch all the rows that match the query
        rows = cursor.fetchall()

        # Iterate over the rows and populate the list widget with the data
        for row in rows:
            item = QListWidgetItem(str(row[0]))
            self.staffBox.addItem(item)

        # Close the cursor and the database connection
        cursor.close()
        conn.close()
    """
        #Show Database on textbox
        # Connect to the database
        conn = sqlite3.connect('SilverVillageUserAcc.db')
        
        # Create a cursor object from the connection
        cursor = conn.cursor()
        
        # Execute the SQL query to retrieve data from the table
        cursor.execute("SELECT * FROM userProfile")
        
        # Fetch all the rows that match the query
        rows = cursor.fetchall()

        # Iterate over the rows and populate the list widget with the data
        for row in rows:
            item = QListWidgetItem(str(row[0]))
            self.custBox.addItem(item)

        # Close the cursor and the database connection
        cursor.close()
        conn.close()
        """
    def searchAccount(self, stackedWidget, item_name):
        self.stackedWidget = stackedWidget

        conn = sqlite3.connect('SilverVillageUserAcc.db')
        cursor = conn.cursor()
  
        sql = "SELECT * FROM account WHERE userID = ?"
        value1 = item_name
        cursor.execute(sql, (value1,))

        rows = cursor.fetchall()
        listItem = str(rows[0][0])
        
        # Iterate over the rows and populate the list widget with the data
        # Close the cursor and the database connection
        cursor.close()
        conn.close()
        
        return listItem