import sqlite3
import sys
sys.path.append('./Boundary')
from PyQt5.QtCore import QStringListModel, Qt

from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QHBoxLayout, \
    QGridLayout, QComboBox, QListWidget, QAbstractItemView,QVBoxLayout, QMessageBox, QListWidgetItem, QStyledItemDelegate

#This class shows the record of buying tickets or food
class customerInfoUI(QWidget):
    def __init__(self, stackedWidget):
        super().__init__()
        self.stackedWidget = stackedWidget

        self.userID = ""

        self.setWindowTitle('Account Information')
        self.resize(400, 300)

        self.record_button = QPushButton('Ticket Purchase Record', self)
        self.record_button.setGeometry(150, 100, 300, 30)

        self.fnb_record_button = QPushButton('F&B Purchase Record', self)
        self.fnb_record_button.setGeometry(150, 150, 300, 30)


        self.back_button = QPushButton('Back', self)
        self.back_button.setGeometry(150, 250, 300, 30)

        self.record_button.clicked.connect(self.show_ticket_record_window)
        self.fnb_record_button.clicked.connect(self.show_fnb_record_window)
        self.back_button.clicked.connect(self.go_back)

    def show_ticket_record_window(self):
        widget = self.stackedWidget.widget(20)
        widget.setID(self.userID)
        print("Sending", self.userID)
        self.stackedWidget.setCurrentIndex(20)

    def show_fnb_record_window(self):
        self.fnb_record_window = QWidget()
        self.fnb_record_window.setWindowTitle('F&B Purchase Record')
        self.fnb_record_window.resize(400, 300)

        self.fnb_text_box = QTextEdit(self.fnb_record_window)
        self.fnb_delete_button = QPushButton('Refund', self.fnb_record_window)
        self.fnb_update_button = QPushButton('Change', self.fnb_record_window)

        vbox = QVBoxLayout()
        vbox.addWidget(self.fnb_text_box)
        hbox = QHBoxLayout()
        hbox.addWidget(self.fnb_delete_button)
        hbox.addWidget(self.fnb_update_button)
        vbox.addLayout(hbox)
        self.fnb_record_window.setLayout(vbox)

        self.fnb_record_window.show()

    def go_back(self):
        self.stackedWidget.setCurrentIndex(6)

    def setID(self, userID):
        self.userID = userID
        print("Receieved", self.userID)
    

class ticketPurchasedUI(QWidget):
    def __init__(self, stackedWidget):
        super().__init__()
        self.stackedWidget = stackedWidget

        self.userID = ""
        ticket_string = '{:<10}\t{:<20}\t{:<20}\t{:<20}\t{:<20}\t{:<30}\t{:<10}\t{:<10}'.format('TicketID', "Movie Name", "Hall Name", "Seat Number", "Show Time", "Date", "Ticket Type", "Cost" )
        self.label1 = QLabel(ticket_string)
        self.ticketList = QListWidget()
        self.viewData()
        self.ticket_delete_button = QPushButton('Refund')
        self.ticket_update_button = QPushButton('Change')
        self.viewButton = QPushButton('View')
        self.backButton = QPushButton("Back")

        layout = QVBoxLayout()
        layout.addWidget(self.label1)
        layout.addWidget(self.ticketList)
        hbox = QHBoxLayout()
        hbox.addWidget(self.viewButton)
        hbox.addWidget(self.ticket_update_button)
        hbox.addWidget(self.ticket_delete_button)
        hbox.addWidget(self.backButton)

        

        self.backButton.clicked.connect(self.goBack)

        layout.addLayout(hbox)
       
        self.setLayout(layout)
        self.stackedWidget.currentChanged.connect(self.viewData)
    def setID(self, userID):
        self.userID = userID
        print("Received 2 ", userID)

    def goBack(self):
        self.stackedWidget.setCurrentIndex(8)

    def viewData(self):
        print("ID here",self.userID)
        conn = sqlite3.connect('SilverVillageUserAcc.db')
        cursor = conn.cursor()
        sql = 'SELECT ticket_ID, movieName ,hallName ,seat_No ,showtime ,date ,type ,price FROM ticket WHERE userID = ?'
        data = (self.userID,)
        cursor.execute(sql ,data)
        ticket_data = cursor.fetchall()
        ticket_strings = []
        for row in ticket_data:
            ticket_string = '{:<10}\t{:<20}\t{:<20}\t{:<20}\t{:<20}\t{:<20}\t{:<10}\t{:<10}'.format(row[0], row[1], row[2], row[3], row[4],row[5], row[6], row[7])
            ticket_strings.append(ticket_string)
        self.ticketList.clear()
        self.ticketList.addItems(ticket_strings)

        conn.commit()
        conn.close()








