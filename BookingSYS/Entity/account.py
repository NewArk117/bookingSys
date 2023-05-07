#Import to use SQL database
import sqlite3

#GUI Imports
from PyQt5.QtWidgets import QMessageBox, QLineEdit, QGridLayout, QWidget, QLabel, QTextEdit
from PyQt5.QtCore import Qt
#Import links to different scripts in Boundary
import sys 
sys.path.append('./Boundary')

class Account:
    def login(self,stackedWidget, usrname, pw, acctype):
        self.stackedWidget = stackedWidget
        self.acctype = acctype

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
                    if acctype == 'admin':
                        self.stackedWidget.setCurrentIndex(2)
                    else:
                        self.stackedWidget.setCurrentIndex(6)
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

    def editAccount(self, stackedWidget, item_name):
        self.stackedWidget = stackedWidget

        conn = sqlite3.connect('SilverVillageUserAcc.db')

        # Get a cursor object
        cursor = conn.cursor()

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

            result = message_box.exec_()

            if result == QMessageBox.Ok:
                texts = [line_edit.text() for line_edit in widget.findChildren(QLineEdit)]
                comments = [line_edit.toPlainText() for line_edit in widget.findChildren(QTextEdit) if line_edit.objectName() == 'comments']
                conn = sqlite3.connect('SilverVillageUserAcc.db')
                c = conn.cursor()
                sql1 = "DELETE FROM account WHERE account.userID = ?"
                value2 = row[0]
                c.execute(sql1,(row[0],))
                c.execute("INSERT INTO account (userID, userName, password, permission) VALUES (?, ?, ?, ?)", (row[0],texts[0], texts[1], texts[2]))
                conn.commit()
                conn.close()