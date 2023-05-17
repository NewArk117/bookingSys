import sys 
import sqlite3
from PyQt5.QtWidgets import QMessageBox, QDialog
from ticket import ticket

class purchaseTicController:
    def purchaseTicC(self, stackedWidget, movieName, genre, hallname, selectedDate, selectedTime,ticCount,seatList, totalCost, userID):
        ticket().purchaseTic(stackedWidget, movieName, genre, hallname, selectedDate, selectedTime,ticCount,seatList, totalCost, userID)

class getTicController:
    def getTicC(self, number):
        return ticket().getTic(number)
    
class editTicController:
    def editTicC(self, dialog, stackedwidget, odate, otime, ndate, ntime, mName, hallName, seat):
        try:
            self.stackWidget = stackedwidget
            conn = sqlite3.connect('SilverVillageUserAcc.db')
            cursor = conn.cursor()

            sql = "SELECT isAvailable FROM seat WHERE hallName = ? AND showtime = ? AND date = ? AND seat_No = ?"
            data = (hallName, ntime, ndate, seat)
            cursor.execute(sql,data)
            result = cursor.fetchone()
            print(hallName, ntime, ndate, seat)
            
            isAvail = result[0]
            print(isAvail)

            if isAvail == 1:
                ticket().editTic(dialog, self.stackWidget, odate, otime, ndate, ntime, mName, hallName, seat)
            else:
                raise ValueError("Seat not available in this showtime")

            conn.commit()
            conn.close()

        except ValueError as e:
            QMessageBox.warning(self.stackWidget, "Error", str(e))

class refundTicController:
    def refundTicC(self, stackedWidget , ticketID ,moviename, hallname, seatNo, showtime, date, type, price):
        self.stackedwidget = stackedWidget
        self.dialog = QDialog(self)
        self.dialog.setWindowTitle("My Dialog")

        headingMsg = f"====== Are you sure to refund this ticket? =====\n"
        movieMsg = f"\nMovie name: {moviename}\n"
        hallMsg = f"Hall Number: {hallname}\n"
        seatMsg = f"Seat No: {seatNo}\n"
        timeMsg = f"Show Time: {showtime}\n"
        dateMsg = f"Date: {date}\n"
        typeMsg = f"Ticket Type: {type}, ${price}\n"

        message = headingMsg + movieMsg + hallMsg + seatMsg + timeMsg + dateMsg + typeMsg

        confirm = QMessageBox.question(self.stackedWidget, 'Refund Ticket', message ,
                                    QMessageBox.Yes | QMessageBox.No)
        if confirm == QMessageBox.Yes:
            ticket().refundTic(self, self.dialog, ticketID, seatNo, hallname, showtime, date)

class viewTicController:
    def viewTicC(self, stackedWidget, ticketList):
        self.stackedWidget = stackedWidget
        self.ticketList = ticketList

        try:
            items = [item.text() for item in self.ticketList.selectedItems()]
            if not items:
                raise ValueError("Please select a ticketType.")
            
            items = self.ticketList.currentItem()
            
            if items:
                ticketID = items.text()[:10].strip() 
                moviename = items.text()[11:30].strip()
                hallname = items.text()[31:50].strip()
                seatNo = items.text()[51:70].strip() 
                showtime = items.text()[71:90].strip() 
                date = items.text()[91:110].strip() 
                type = items.text()[111:121].strip() 
                price = items.text()[121:130].strip() 

            ticket().viewTic(self.stackedWidget, moviename, hallname, seatNo, showtime, date, type, price)

        except ValueError as e:
            QMessageBox.warning(self.stackedWidget, "Error", str(e))