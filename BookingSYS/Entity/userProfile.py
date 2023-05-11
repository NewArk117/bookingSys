#Import to use SQL database
import sqlite3

#GUI Imports
from PyQt5.QtWidgets import QMessageBox, QLineEdit, QGridLayout, QWidget, QLabel, QTextEdit

#Import links to different scripts in Boundary
import sys 
sys.path.append('./Boundary')

class UserProfile:
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
            message_box.setText("Account ID: " + str(row[0]) + "\n" + "Name: " + str(row[1]) + "\n" + "Date of Birth: " + str(row[2]) + "\n" + "Account Type: " + str(row[3]))
            message_box.setWindowTitle(str(row[0]))
            message_box.exec_()
        
        # Close the cursor and the database connection
        cursor.close()
        conn.close()

    def editProfile(self, stackedWidget, item_name):
        self.stackedWidget = stackedWidget

        conn = sqlite3.connect('SilverVillageUserAcc.db')

        # Get a cursor object
        cursor = conn.cursor()

        sql = """SELECT * 
                 FROM userProfile 
                 JOIN account ON userProfile.userID = account.userID 
                 WHERE userProfile.userID = ?"""
        value1 = item_name

        cursor.execute(sql, (value1,))

        rows = cursor.fetchall()


        for row in rows:
            message_box = QMessageBox()
            message_box.setWindowTitle(str(row[0]))
            message_box.setText('Edit Profile')

            field_labels = ["Name:", "Date of Birth:", "Account Type:"]
            layout = QGridLayout()

            for label_text in field_labels:
                    label = QLabel(label_text)
                    
                    i = 0
                    if label_text == "Name:":
                        line_edit = QLineEdit(str(row[1]))
                        layout.addWidget(label,1,0)
                        layout.addWidget(line_edit,1,1)      
                    elif label_text == "Date of Birth:":
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

            result = message_box.exec_()

            if result == QMessageBox.Ok:
                texts = [line_edit.text() for line_edit in widget.findChildren(QLineEdit)]
                comments = [line_edit.toPlainText() for line_edit in widget.findChildren(QTextEdit) if line_edit.objectName() == 'comments']
                conn = sqlite3.connect('SilverVillageUserAcc.db')
                c = conn.cursor()
                sql1 = "DELETE FROM userProfile WHERE userProfile.userID = ?"
                value2 = row[0]
                c.execute(sql1,(row[0],))
                c.execute("INSERT INTO userProfile (userID, name, DOB, accType) VALUES (?, ?, ?, ?)", (row[0],texts[0], texts[1], texts[2]))
                conn.commit()
                conn.close()