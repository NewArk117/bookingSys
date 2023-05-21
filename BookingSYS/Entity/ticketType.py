import sqlite3

#GUI Imports
from PyQt5.QtWidgets import QMessageBox, QListWidgetItem, QGridLayout, QWidget, QLabel, QTextEdit
from PyQt5.QtCore import Qt
#Import links to different scripts in Boundary
import sys 
sys.path.append('./Boundary')

class ticketType:
    def susTicType(self, stackedWidget, ticList):
        self.stackedWidget = stackedWidget
        self.ticList = ticList
        item = self.ticList.currentItem()
        type = item.text().strip()
 
        conn = sqlite3.connect('SilverVillageUserAcc.db')
        cursor = conn.cursor()

        sql = "UPDATE ticketType SET isAvailable = ? WHERE type = ?"
        data = (0 ,type)
        cursor.execute(sql, data)

        conn.commit()
        conn.close()
    

        

    def addTicType(self, stackedWidget, name , price):
        self.stackedWidget = stackedWidget

        conn = sqlite3.connect('SilverVillageUserAcc.db')

        # Get a cursor object
        cursor = conn.cursor()

        cursor.execute('SELECT type FROM ticketType')
        tictype_data = cursor.fetchall()
        ticList = []
        for row in tictype_data:
            ticList.append(row[0])

        if name not in ticList:
            
            # Insert a new record into the account table
            sql = "INSERT INTO ticketType (type, price, isAvailable) VALUES (?, ?, ?)"
            data = (name, price, 1)
            cursor.execute(sql, data)

            # Commit the transaction
            conn.commit()

            

            self.stackedWidget.setCurrentIndex(13)
        else:
            self.stackedWidget.setCurrentIndex(13)

        # Close the database connection
        conn.close()


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

    def editTicType(self, dialog, stackedwidget, name1 , price1, avail1, name2, price2, avail2):
        self.stackedWidget = stackedwidget
        self.dialog = dialog
        conn = sqlite3.connect('SilverVillageUserAcc.db')
        cursor = conn.cursor()

        if name2 == "":
            name2 = name1
        if price2 == "":
            price2 = price1
        if avail2 == "":
            avail2 = avail1
            
        cursor.execute('SELECT type FROM ticketType')
        tictype_data = cursor.fetchall()
        ticList = []
        for row in tictype_data:
            ticList.append(row[0])

        if name2 not in ticList:
            # Update an existing record in the ticketType table
            sql = "UPDATE ticketType SET type = ?, price = ?, isAvailable = ? WHERE type = ? AND price = ? AND isAvailable = ?"
            data = (name2, price2,avail2, name1, price1, avail1)
            cursor.execute(sql, data)

        # Commit the transaction
        conn.commit()

        # Close the database connection
        conn.close()
        #self.listTicType(self.stackedWidget, )
        self.dialog.reject()

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
            #message_box = QMessageBox()
            text = ("Ticket Type: " + str(row[0]) + "\n" + "Price: $" + str(row[1]) + "\n" + "Availability: " + str(row[2]))
            type = (str(row[0]))
            #message_box.exec()
        
        # Close the cursor and the database connection
        cursor.close()
        conn.close()
    
        return text ,type

    def getData(self, item_name):
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
            self.ticketType = str(row[0])
            self.price = str(row[1])
            self.avail = str(row[2])

        # Close the cursor and the database connection
        cursor.close()
        conn.close()

        return self.ticketType, self.price, self.avail
