import sqlite3

#GUI Imports
from PyQt5.QtWidgets import QMessageBox, QLineEdit, QGridLayout, QWidget, QLabel, QTextEdit, QComboBox, QListWidget, QVBoxLayout
from PyQt5.QtCore import Qt
#Import links to different scripts in Boundary
import sys 
sys.path.append('./Boundary')

class ticket:

    def purchaseTic(self, stackedWidget, movieName, genre, hallName, selectedDate, selectedTime,ticCount,seatList, totalCost, userID):
        self.stackedWidget = stackedWidget

        print(movieName, genre, hallName, selectedDate, selectedTime,ticCount, seatList, totalCost, userID)
        #try:
        conn = sqlite3.connect('SilverVillageUserAcc.db')
        cursor = conn.cursor()

        for x in seatList:
            sql = "UPDATE seat SET isAvailable = ? WHERE seat_No = ? AND hallName = ? AND showtime = ? AND date = ?"
            data = (0, x[0] , hallName, selectedTime, selectedDate )
            cursor.execute(sql, data)

            sql2 = "INSERT INTO ticket (userID ,movieName , hallName , seat_No ,showtime,date, type, price) VALUES (?, ?,?, ?,? ,?, ?, ?)"
            data2 = (userID, movieName, hallName, x[0], selectedTime, selectedDate, x[1], x[2])
            cursor.execute(sql2, data2)
            
        
        conn.commit()
        conn.close()
        
        current_widget_index = self.stackedWidget.currentIndex()
        current_widget = self.stackedWidget.widget(current_widget_index)
        self.stackedWidget.removeWidget(current_widget)
        self.stackedWidget.setCurrentIndex(7)

                
           # raise ValueError("No movies selected")
       # except ValueError as e:
        #    QMessageBox.warning(self.stackedWidget, 'Error', str(e))
       #     print(str(e))

    def getTic(self, number):
        conn = sqlite3.connect('SilverVillageUserAcc.db')
        cursor = conn.cursor()

        self.number = int(number)
        self.ticketsList = QListWidget
        self.tictype = QComboBox

        sql = "SELECT * FROM ticketType"
        cursor.execute(sql)
        type_data = cursor.fetchall()
        type_box = []
        for row in type_data:
            type_string = row[0]
            type_box.append(type_string)
        self.tictype.addItems(type_box)
        list = []

        layout = QVBoxLayout

        for x in range(number):
             ticket = QLabel("Ticket " + (number+1))
        
        conn.commit()

        conn.close()

    def editTic(self,dialog, stackedwidget, odate, otime, ndate, ntime, mName, hallName, seat):
        self.dialog = dialog

        conn = sqlite3.connect('SilverVillageUserAcc.db')
        cursor = conn.cursor()

        sql = "UPDATE seat SET isAvailable = ? WHERE seat_No = ? AND hallName = ? AND showtime = ? AND date = ?"
        data = (1, seat , hallName, otime, odate )
        cursor.execute(sql, data)

        sql2 = "UPDATE seat SET isAvailable = ? WHERE seat_No = ? AND hallName = ? AND showtime = ? AND date = ?"
        data2 = (0, seat , hallName, ntime, ndate)
        cursor.execute(sql2, data2)

        sql3 = "UPDATE ticket SET date = ?, showtime = ? WHERE movieName = ? and showtime = ? AND date = ? AND hallName = ? AND seat_No = ?"
        data3 = (ndate, ntime, mName, otime, odate, hallName, seat)
        cursor.execute(sql3, data3)

        self.dialog.close()

        conn.commit()

        conn.close()
        
    def refundTic(self, dialog, ticketID, seat, hallName, otime, odate):
        self.dialog = dialog
        self.ticetID = ticketID

        conn = sqlite3.connect('SilverVillageUserAcc.db')
        cursor = conn.cursor()

        sql = "UPDATE seat SET isAvailable = ? WHERE seat_No = ? AND hallName = ? AND showtime = ? AND date = ?"
        data = (1, seat , hallName, otime, odate )
        cursor.execute(sql, data)

        sql2 = "DELETE FROM ticket WHERE ticket_ID = ?"
        data2 = (ticketID,)
        cursor.execute(sql2, data2)

        conn.commit()

        conn.close()

        self.dialog.close()
           
    def viewTic(self, stackedWidget, moviename, hallname, seatNo, showtime, date, type, price):
        self.stackedWidget = stackedWidget
        headingMsg = f"====== SHOW THIS TICKET TO ENTER =====\n"
        movieMsg = f"\nMovie name: {moviename}\n"
        hallMsg = f"Hall Number: {hallname}\n"
        seatMsg = f"Seat No: {seatNo}\n"
        timeMsg = f"Show Time: {showtime}\n"
        dateMsg = f"Date: {date}\n"
        typeMsg = f"Ticket Type: {type}, ${price}\n"

        message = headingMsg + movieMsg + hallMsg + seatMsg + timeMsg + dateMsg + typeMsg

        QMessageBox.information(self.stackedWidget, 'Show Ticket', message)