import sys 
import sqlite3
from PyQt5.QtWidgets import QMessageBox
from ticket import ticket

class purchaseTicController:
    def purchaseTicC(self, stackedWidget, movieName, genre, hallname, selectedDate, selectedTime,ticCount,seatList, totalCost, userID):
        ticket().purchaseTic(stackedWidget, movieName, genre, hallname, selectedDate, selectedTime,ticCount,seatList, totalCost, userID)

class getTicController:
    def getTicC(self, number):
        return ticket().getTic(number)


class TicketController:
    def get_tickets(user_id):
        ticket_data = ticket.get_tickets(user_id)
        return ticket_data

