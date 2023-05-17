import sqlite3
import datetime
from datetime import date
#GUI Imports
from PyQt5.QtWidgets import QMessageBox, QLineEdit, QGridLayout, QWidget, QLabel, QTextEdit, QPushButton
from PyQt5.QtCore import Qt
#Import links to different scripts in Boundary
import sys 
sys.path.append('./Boundary')

class cinemaHall:
    #6. Cinema Manager Controller
    def susHall(self, stackedWidget, hallList):
        self.stackedWidget = stackedWidget
        self.hallList = hallList
        items = [self.hallList.item(i).text() for i in range(self.hallList.count())]
        for item in items:
            words = item.split()
            hallName = words[0]
        items_str = ' '.join(' '.join(items).split()) 
        try:
            if not items_str:
                raise ValueError("No Hall selected")
            message = f'Are you sure you want to suspend {hallName} ?'     
            confirm = QMessageBox.question(self.stackedWidget, 'Suspend Hall', message ,
                                            QMessageBox.Yes | QMessageBox.No)
            if confirm == QMessageBox.Yes:
                print("ok")
                #insert sql to suspend hall here
                conn = sqlite3.connect('SilverVillageUserAcc.db')
                cursor = conn.cursor()

                sql = "UPDATE hall SET isAccessible = ? WHERE hallName = ?"
                data = (0, hallName)
                cursor.execute(sql, data)

                conn.commit()
                conn.close()
                self.listManagerHall(self.stackedWidget, self.hallList) 

        except ValueError as e:
            QMessageBox.warning(self.stackedWidget, 'Error', str(e))
            print(str(e))
    #3. Cinema Manager Entity
    def addHall(self, stackedwidget, name, rows, columns):
        self.stackedWidget = stackedwidget
        row_labels = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
        message = f'Add Hall with the following values (?) :\nHall Name:{name}\n'
        rows = int(rows)
        columns = int(columns)
        self.seats = ""
        #print (rows + " " + columns)
        for row in range(rows):
            x = "Seats: " + row_labels[row] + "1 - " + row_labels[row]+ str(columns+1)
            self.seats = self.seats + "\n" + x

        message = message + self.seats
        #print(message)

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

        try:   


            confirm = QMessageBox.question(self.stackedWidget, 'Add Cinema Hall', message ,
                                            QMessageBox.Yes | QMessageBox.No)
            if confirm == QMessageBox.Yes:
                conn = sqlite3.connect('SilverVillageUserAcc.db')

                # Get a cursor object
                cursor = conn.cursor()


                for date1 in datelist:
                    for time in showtimes:
                        sql1 = "INSERT INTO hallshowtime (hallName, showtime, date, isAvailable) VALUES (?, ?, ?, ?)"
                        data1 = (name,time,date1, 1)
                        cursor.execute(sql1, data1)
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

        except ValueError as e:
            QMessageBox.warning(self.stackedWidget, 'Error', str(e))
            print(str(e))
    #5. Cinema Manager Entity
    def editHall(self, stackedwidget, dialog ,name , row, column, avail, name2, rows2, columns2, avail2):
        self.dialog = dialog
        self.stackedWidget= stackedwidget
        try:   
            if name2 == "":
                name2 = name
            if rows2 == "":
                rows2 = row
            if columns2 == "":
                columns2 = column
            if avail2 == "":
                avail2 = avail
            message = f'Confirm these changes(?)\n\nOLD----\nHall Name:{name}\nRows:{row}\nColumns:{column}\nAvailability:{avail}\n\nNEW----\nHall Name:{name2}\nRows:{rows2}\nColumns:{columns2}\nAvailability:{avail2}'

            confirm = QMessageBox.question(self.stackedWidget, 'Update Hall', message ,
                                            QMessageBox.Yes | QMessageBox.No)
            if confirm == QMessageBox.Yes:
                self.delSeats(name, row , column)
                
                conn = sqlite3.connect('SilverVillageUserAcc.db')
                cursor = conn.cursor()
                capacity = int(rows2) * int(columns2)
                # Update an existing record in hall

                sql = "UPDATE hall SET hallName = ?, rows = ?, columns = ?, capacity = ?, isAvailable = ? WHERE hallName = ?"
                data = (name2, rows2, columns2, capacity, avail2, name)
                cursor.execute(sql, data)

                # Commit the transaction
                conn.commit()

                # Close the database connection
                conn.close()

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
                        self.addSeats(name2, rows2, columns2, time, date1)

                self.dialog.reject()
                return True
                
        except ValueError as e:
            QMessageBox.warning(self.stackedWidget, 'Error', str(e))
            print(str(e))

    def listManagerHall(self, stackWidget, list):
        self.list = list
        conn = sqlite3.connect('SilverVillageUserAcc.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM hall')
        hall_data = cursor.fetchall()
        hall_strings = []
        for row in hall_data:
            hall_string = '{:<20}\t{:<5}\t{:<5}\t{:<10}\t{:5}'.format(row[0], row[1], row[2], row[3], row[4])
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