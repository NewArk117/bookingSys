import sqlite3

#GUI Imports
from PyQt5.QtWidgets import QMessageBox, QListWidgetItem, QGridLayout, QWidget, QLabel, QTextEdit
from PyQt5.QtCore import Qt
#Import links to different scripts in Boundary
import sys 
sys.path.append('./Boundary')

class ticketType:
    def delTicType(self, stackedWidget, ticList):
        self.stackedWidget = stackedWidget
        self.ticList = ticList
        items = [self.ticList.item(i).text() for i in range(self.ticList.count())]
        for item in items:
            words = item.split()
            type = words[0]
            price = words[1]
        items_str = ' '.join(' '.join(items).split())           
        try:
            if not items_str:
                raise ValueError("No ticket type selected")
            message = f'Are you sure you want to remove(?)\nTicket Type: {type}\nPrice: {price} '     
            confirm = QMessageBox.question(self.stackedWidget, 'Remove ticket type', message ,
                                            QMessageBox.Yes | QMessageBox.No)
            if confirm == QMessageBox.Yes:
                print("ok")
                conn = sqlite3.connect('SilverVillageUserAcc.db')
                cursor = conn.cursor()

                sql = "DELETE FROM ticketType WHERE type = ? AND price = ?"
                data = (type, price)
                cursor.execute(sql, data)

                conn.commit()
                conn.close()
                self.listTicType(self.stackedWidget, self.ticList) 
        except ValueError as e:
            QMessageBox.warning(self.stackedWidget, 'Error', str(e))
            print(str(e))


        

    def addTicType(self, stackedWidget, name , price):
        self.stackedWidget = stackedWidget
        message = f'Add ticket type named:{name} \nPrice:{price} '
        try:   
            confirm = QMessageBox.question(self.stackedWidget, 'Add Ticket Type', message ,
                                            QMessageBox.Yes | QMessageBox.No)
            if confirm == QMessageBox.Yes:
                conn = sqlite3.connect('SilverVillageUserAcc.db')

                # Get a cursor object
                cursor = conn.cursor()

                # Insert a new record into the account table
                sql = "INSERT INTO ticketType (type, price) VALUES (?, ?)"
                data = (name, price)
                cursor.execute(sql, data)

                # Commit the transaction
                conn.commit()

                # Close the database connection
                conn.close()

                self.stackedWidget.setCurrentIndex(13)

        except ValueError as e:
            QMessageBox.warning(self.stackedWidget, 'Error', str(e))
            print(str(e))

    def listTicType(self, stackWidget, list):
        self.list = list
        conn = sqlite3.connect('SilverVillageUserAcc.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM ticketType')
        ticType_data = cursor.fetchall()
        ticType_strings = []
        for row in ticType_data:
            #ticket_string = '{:<20}\t{:<30}'.format(row[0], row[1])
            ticket_string = '{:<20}'.format(row[0])
            ticType_strings.append(ticket_string)
        self.list.clear()
        self.list.addItems(ticType_strings)
        conn.close()

    def editTicType(self, dialog, stackedwidget, name1 , price1, name2, price2):
        self.stackedWidget = stackedwidget
        self.dialog = dialog
        message = f'Confirm to update(?)\nOld Name:{name1}\nOld Price:{price1}\nTo\nNew Name:{name2}\nNew Price:{price2}'
        try:   
            confirm = QMessageBox.question(self.stackedWidget, 'Update Ticket', message ,
                                            QMessageBox.Yes | QMessageBox.No)
            if confirm == QMessageBox.Yes:
                conn = sqlite3.connect('SilverVillageUserAcc.db')
                cursor = conn.cursor()

                # Update an existing record in the ticketType table
                sql = "UPDATE ticketType SET type = ?, price = ? WHERE type = ? AND price = ?"
                data = (name2, price2, name1, price1)
                cursor.execute(sql, data)

                # Commit the transaction
                conn.commit()

                # Close the database connection
                conn.close()

                self.dialog.reject()

        except ValueError as e:
            QMessageBox.warning(self.stackedWidget, 'Error', str(e))
            print(str(e))

    def searchTicType(self, stackedWidget, item_name, list):
        self.stackedWidget = stackedWidget
        self.list = list

        if item_name != "":
            conn = sqlite3.connect('SilverVillageUserAcc.db')
            cursor = conn.cursor()
            list.clear()
            sql = "SELECT * FROM ticketType WHERE type = ?"
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
            cursor.execute("SELECT * FROM ticketType")
            
            # Fetch all the rows that match the query
            rows = cursor.fetchall()

            # Iterate over the rows and populate the list widget with the data
            for row in rows:
                item = QListWidgetItem(str(row[0]))
                self.list.addItem(item)

            # Close the cursor and the database connection
            cursor.close()
            conn.close()

    def viewTicType(self, stackedWidget, item_name):
        conn = sqlite3.connect('SilverVillageUserAcc.db')
        # Get a cursor object
        cursor = conn.cursor()
        query = "SELECT * FROM ticketType WHERE type = ?"
        value1 = item_name.strip()
        # Execute the SQL query to retrieve data from the table
        cursor.execute(query, (value1,))
        # Fetch all the rows that match the query
        rows = cursor.fetchall()
        for row in rows:
            print(str(row[0]))
            message_box = QMessageBox()
            message_box.setText("Ticket Type: " + str(row[0]) + "\n" + "Price: $" + str(row[1]) + "\n" + "Availability: " + str(row[2]))
            message_box.setWindowTitle(str(row[0]))
            message_box.exec()
        
        # Close the cursor and the database connection
        cursor.close()
        conn.close()
