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


    def get_user_tickets(user_id):
        conn = sqlite3.connect('SilverVillageUserAcc.db')
        cursor = conn.cursor()
        sql = 'SELECT ticket_ID, movieName, hallName, seat_No, showtime, date, type, price FROM ticket WHERE userID = ?'
        data = (user_id,)
        cursor.execute(sql, data)
        ticket_data = cursor.fetchall()
        conn.close()
        return ticket_data

    def delete_ticket(ticket_id):
        conn = sqlite3.connect('SilverVillageUserAcc.db')
        cursor = conn.cursor()

        # Retrieve hallName and seat_ID associated with the ticket ID
        cursor.execute('SELECT hallName, seat_No FROM ticket WHERE ticket_ID = ?', (ticket_id,))
        result = cursor.fetchone()
        hall_name, seat_id = result

        # Delete the ticket from the ticket table
        sql_delete_ticket = 'DELETE FROM ticket WHERE ticket_ID = ?'
        cursor.execute(sql_delete_ticket, (ticket_id,))

        # Update the isAvailable column in the seat table
        sql_update_seat = 'UPDATE seat SET isAvailable = 1 WHERE hallName = ? AND seat_No = ?'
        cursor.execute(sql_update_seat, (hall_name, seat_id))

        conn.commit()
        conn.close()

    def get_tickets(user_id):
        conn = sqlite3.connect('SilverVillageUserAcc.db')
        cursor = conn.cursor()
        sql = 'SELECT ticket_ID, movieName, showtime, date FROM ticket WHERE userID = ?'
        data = (user_id,)
        cursor.execute(sql, data)
        ticket_data = cursor.fetchall()
        conn.close()
        return ticket_data

        

           
