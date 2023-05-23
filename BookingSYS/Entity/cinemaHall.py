import sqlite3
import datetime
from datetime import date
#GUI Imports
from PyQt5.QtWidgets import QMessageBox, QListWidgetItem, QGridLayout, QWidget, QLabel, QTextEdit, QPushButton
from PyQt5.QtCore import Qt
#Import links to different scripts in Boundary
import sys 
sys.path.append('./Boundary')

class cinemaHall:
    #6. Cinema Manager Controller
    def susHall(self, stackedWidget, hallList):
        self.stackedWidget = stackedWidget
        self.hallList = hallList
        items = self.hallList.currentItem()
        hallName = items.text().strip()
     
        print("ok")
        #insert sql to suspend hall here
        conn = sqlite3.connect('SilverVillageUserAcc.db')
        cursor = conn.cursor()

        sql = "UPDATE hall SET isAvailable = ? WHERE hallName = ?"
        data = (0, hallName)
        cursor.execute(sql, data)

        sql = "UPDATE hallshowtime SET isAvailable = ? WHERE hallName = ?"
        data = (0, hallName)
        cursor.execute(sql, data)

        conn.commit()
        conn.close()

    #3. Cinema Manager Entity
    def addHall(self, stackedwidget, name, rows, columns):
        self.stackedWidget = stackedwidget
        conn = sqlite3.connect('SilverVillageUserAcc.db')

        # Get a cursor object
        cursor = conn.cursor()
        
        cursor.execute('SELECT hallName FROM hall')
        hall_data = cursor.fetchall()
        hallList = []
        for row in hall_data:
            hallList.append(row[0])

        #print(hallList)
        if name not in hallList:
            #print("Not here")

            row_labels = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
            rows = int(rows)
            columns = int(columns)
            self.seats = ""
            #print (rows + " " + columns)
            for row in range(rows):
                x = "Seats: " + row_labels[row] + "1 - " + row_labels[row]+ str(columns+1)
                self.seats = self.seats + "\n" + x

            datelist = []
            showtimes = ["1330", "1530", "1730", "1930", "2130"]
            startDate = datetime.date(2023, 5, 1)
            #startDate = date.today()
            delta = datetime.timedelta(days=1)
            endDate = datetime.date(2023, 11 , 30)
            currentDate = startDate

            while currentDate <= endDate:
                datelist.append(currentDate)
                currentDate += delta


            for date1 in datelist:
                for time in showtimes:
                    sql1 = "INSERT INTO hallshowtime (hallName, showtime, date, isAvailable) VALUES (?, ?, ?, ?)"
                    data1 = (name,time,date1, 1)
                    cursor.execute(sql1, data1)
                    conn.commit()
                    self.addSeats(name, rows, columns, time ,date1)

            sql2 = "INSERT INTO hall (hallName, rows, columns, capacity, isAvailable) VALUES (?, ?, ?, ? ,?)"
            capacity = rows * columns
            data2 = (name, rows, columns, capacity, 1)
            cursor.execute(sql2, data2)
        
        # Commit the transaction
        conn.commit()

        # Close the database connection
        conn.close()

        self.stackedWidget.setCurrentIndex(11)

    #5. Cinema Manager Entity
    def editHall(self, stackedwidget, dialog ,name , avail, name2, avail2):
        self.dialog = dialog
        self.stackedWidget= stackedwidget  

        conn = sqlite3.connect('SilverVillageUserAcc.db')
        cursor = conn.cursor()
        if name2 == "":
            name2 = name
        if avail2 == "":
            avail2 = avail

        cursor.execute('SELECT hallName FROM hall')
        hall_data = cursor.fetchall()
        hallList = []
        for row in hall_data:
            hallList.append(row[0])

        if name2 == name:
                      
            
            # Update an existing record in hall

            sql = "UPDATE hall SET hallName = ?, isAvailable = ? WHERE hallName = ?"
            data = (name2, avail2, name)
            cursor.execute(sql, data)

            sql1 = "UPDATE hallshowtime SET hallName = ? WHERE hallName = ?"
            data1 = (name2, name)
            cursor.execute(sql1, data1)

            sql2 = "UPDATE movie SET hallName = ? WHERE hallName = ?"
            data2 = (name2,  name)
            cursor.execute(sql2, data2)

            sql3 = "UPDATE seat SET hallName = ? WHERE hallName = ?"
            data3 = (name2,  name)
            cursor.execute(sql3, data3)

            sql4 = "UPDATE ticket SET hallName = ? WHERE hallName = ?"
            data4 = (name2, name)
            cursor.execute(sql4, data4)

        #print(hallList)
        if name2 not in hallList:
                      
            
            # Update an existing record in hall

            sql = "UPDATE hall SET hallName = ?, isAvailable = ? WHERE hallName = ?"
            data = (name2, avail2, name)
            cursor.execute(sql, data)

            sql1 = "UPDATE hallshowtime SET hallName = ? WHERE hallName = ?"
            data1 = (name2, name)
            cursor.execute(sql1, data1)

            sql2 = "UPDATE movie SET hallName = ? WHERE hallName = ?"
            data2 = (name2,  name)
            cursor.execute(sql2, data2)

            sql3 = "UPDATE seat SET hallName = ? WHERE hallName = ?"
            data3 = (name2,  name)
            cursor.execute(sql3, data3)

            sql4 = "UPDATE ticket SET hallName = ? WHERE hallName = ?"
            data4 = (name2, name)
            cursor.execute(sql4, data4)

        # Commit the transaction
        conn.commit()

        # Close the database connection
        conn.close()

        self.dialog.reject()

    def listManagerHall(self, stackWidget, list):
        self.list = list
        conn = sqlite3.connect('SilverVillageUserAcc.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM hall')
        hall_data = cursor.fetchall()
        hall_strings = []
        for row in hall_data:
            #hall_string = '{:<20}\t{:<5}\t{:<5}\t{:<10}\t{:5}'.format(row[0])
            hall_string = '{:<20}'.format(row[0])
            hall_strings.append(hall_string)
        self.list.clear()
        self.list.addItems(hall_strings)
        conn.close()

    def delSeats(self, name , row, column):
        row_labels = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
        rows = int(row)
        columns = int(column)
  
        conn = sqlite3.connect('SilverVillageUserAcc.db')

        cursor = conn.cursor()

        for row in range(rows):
            for col in range(columns):
                seatNo = "" + row_labels[row] + "-" + str(col+1)
                sql = "DELETE FROM seat WHERE seat_No = ? AND hallName = ?"
                data =(seatNo, name)
                cursor.execute(sql, data)

        # Commit the transaction
        conn.commit()

        # Close the database connection
        conn.close()

    def addSeats(self, name , row, column, showtime, date):
        row_labels = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
        rows = int(row)
        columns = int(column)
  
        conn = sqlite3.connect('SilverVillageUserAcc.db')

        cursor = conn.cursor()

        for rowx in range(rows):
            for col in range(columns):
                seatNo = "" + row_labels[rowx] + "-" + str(col+1)
                sql = "INSERT INTO seat (seat_No, hallName, showtime, date, isAvailable) VALUES (?, ? , ?, ?,?)"
                data =(seatNo, name,showtime, date, 1)
                cursor.execute(sql, data)

        # Commit the transaction
        conn.commit()

        # Close the database connection
        conn.close()

    def searchHall(self, stackedWidget, item_name, list)->list:
        self.stackedWidget = stackedWidget
        self.list = list

        if item_name != "":
            conn = sqlite3.connect('SilverVillageUserAcc.db')
            cursor = conn.cursor()
            list.clear()
            sql = "SELECT * FROM hall WHERE hallName = ?"
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

            return list
        else:
            self.list = list
            # Connect to the database
            conn = sqlite3.connect('SilverVillageUserAcc.db')
            
            # Create a cursor object from the connection
            cursor = conn.cursor()
            list.clear()
            # Execute the SQL query to retrieve data from the table
            cursor.execute("SELECT * FROM hall")
            
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

    def viewHall(self, stackedWidget, item_name):
        conn = sqlite3.connect('SilverVillageUserAcc.db')
        # Get a cursor object
        cursor = conn.cursor()
        query = "SELECT * FROM hall WHERE hallName = ?"
        value1 = item_name.strip()
        # Execute the SQL query to retrieve data from the table
        cursor.execute(query, (value1,))
        # Fetch all the rows that match the query
        rows = cursor.fetchall()

        for row in rows:
            #message_box = QMessageBox()
            text = "Hall Name: " + str(row[0]) + "\n" + "Rows : " + str(row[1]) + "\n" + "Columns: " + str(row[2]) + "\n" + "Capacity: " + str(row[3])+ "\nAvailability: " + str(row[4])
            hallName = str(row[0])
            #message_box.exec_()
        
        # Close the cursor and the database connection
        cursor.close()
        conn.close()

        return text,hallName


    def getData(self, item_name):
        conn = sqlite3.connect('SilverVillageUserAcc.db')
        # Get a cursor object
        cursor = conn.cursor()
        query = "SELECT * FROM hall WHERE hallName = ?"
        value1 = item_name.strip()
        # Execute the SQL query to retrieve data from the table
        cursor.execute(query, (value1,))
        # Fetch all the rows that match the query
        rows = cursor.fetchall()
        for row in rows:
            self.hallname = str(row[0])
            self.rows = str(row[1])
            self.columns = str(row[2])
            self.avail = str(row[4])
        # Close the cursor and the database connection
        cursor.close()
        conn.close()

        return self.hallname, self.rows, self.columns, self.avail