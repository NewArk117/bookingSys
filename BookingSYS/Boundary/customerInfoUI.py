import sqlite3
import sys
import datetime
sys.path.append('./Boundary')
from PyQt5.QtCore import QStringListModel, Qt

from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QHBoxLayout, \
    QGridLayout, QComboBox, QListWidget, QAbstractItemView,QVBoxLayout, QMessageBox, QListWidgetItem, QStyledItemDelegate, QDialog

from ticController import editTicController, refundTicController, viewTicController

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
        #print("Receieved", self.userID)
    

class ticketPurchasedUI(QWidget):
    def __init__(self, stackedWidget):
        super().__init__()
        self.stackedWidget = stackedWidget

        self.userID = ""
        ticket_string = '{:<10}\t{:<20}\t{:<20}\t{:<20}\t{:<20}\t{:<30}\t{:<10}\t{:<10}'.format('TicketID', "Movie Name", "Hall Name", "Seat Number", "Show Time", "Date", "Ticket Type", "Cost" )
        self.label1 = QLabel(ticket_string)
        self.ticketList = QListWidget()
        self.listData()
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
        self.viewButton.clicked.connect(self.viewTic)
        self.ticket_update_button.clicked.connect(self.editTic)

        layout.addLayout(hbox)
       
        self.setLayout(layout)
        self.stackedWidget.currentChanged.connect(self.listData)
    def setID(self, userID):
        self.userID = userID
        #print("Received 2 ", userID)

    def goBack(self):
        self.stackedWidget.setCurrentIndex(8)

    def listData(self):
        #print("ID here",self.userID)
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

    def viewTic(self):
        viewTicController.viewTicC(self, self.stackedWidget,self.ticketList)

    def editTic(self):
        self.dialog = QDialog(self)
        self.dialog.setWindowTitle("My Dialog")

        try:
            items = [item.text() for item in self.ticketList.selectedItems()]
            if not items:
                raise ValueError("Please select a ticketType.")
            
            items = self.ticketList.currentItem()
            
            if items:
                ticketID = items.text()[:10].strip() 
                self.moviename = items.text()[11:30].strip()
                self.hallname = items.text()[31:50].strip()
                self.seatNo = items.text()[51:70].strip() 
                self.showtime = items.text()[71:90].strip() 
                self.date = items.text()[91:110].strip() 
                type = items.text()[111:121].strip() 
                price = items.text()[121:130].strip() 
                #print(ticketID, moveiname, hallname, seatNo, showtime, date, type, price)

                
              
                conn = sqlite3.connect('SilverVillageUserAcc.db')
                cursor = conn.cursor()
                sql = 'SELECT DISTINCT startdate, enddate FROM movie WHERE movieName = ?'
                data = (self.moviename,)
                cursor.execute(sql, data)
                movies_data = cursor.fetchall()
                for row in movies_data:
                    startDate = row[0]
                    endDate = row[1]
                conn.commit()
                conn.close()

                #get list of dates
                #startDate = datetime.datetime.strptime(startDate, '%Y-%m-%d')
                #endDate = datetime.datetime.strptime(endDate, '%Y-%m-%d')
                print(startDate, endDate)
                datelist = []
                delta = datetime.timedelta(days=1)
                currentDate = datetime.datetime.strptime(startDate, '%Y-%m-%d')
                endDate = datetime.datetime.strptime(endDate, '%Y-%m-%d')
                while currentDate <= endDate:
                    datelist.append(str(currentDate.date()))
                    currentDate += delta

                print(datelist)
                layout = QGridLayout(self.dialog)

                self.movieLabel = QLabel(f"Movie Name: {self.moviename}")

                self.date1_label = QLabel(f'Current Date: {self.date}')
                
                self.time1_label = QLabel(f'Current Time:{self.showtime}')

                self.date2_label = QLabel('New Date:')
                self.date2_edit = QComboBox()
                self.date2_edit.addItems(datelist)
                #self.name2_edit.setPlaceholderText(self.oldname)
                
                showtimes = ["1330", "1530", "1730", "1930","2130"]
                self.time2_label = QLabel('New Showtime:')
                self.time2_edit = QComboBox()
                self.time2_edit.addItems(showtimes)
                #self.price2_edit.setPlaceholderText(self.oldprice)
                
                self.backButton = QPushButton("Back")
                self.submitButton = QPushButton("Submit")

                layout.addWidget(self.movieLabel,0,0)
                layout.addWidget(self.date1_label, 1, 0)
                layout.addWidget(self.time1_label,2,0)
                layout.addWidget(self.date2_label,3,0)
                layout.addWidget(self.date2_edit, 3, 1)
                layout.addWidget(self.time2_label, 4, 0)
                layout.addWidget(self.time2_edit, 4, 1)

                layout.addWidget(self.backButton,6, 0 )
                layout.addWidget(self.submitButton,6 ,2)

                self.newDate = self.date2_edit.currentText()
                self.newTime = self.time2_edit.currentText()
                print(self.newDate, self.newTime)

                self.submitButton.clicked.connect(lambda: (self.confirmText(self.dialog ,self.stackedWidget, self.date, self.showtime, self.newDate, self.newTime, self.moviename, self.hallname, self.seatNo)))

                self.dialog.exec()

            
        except ValueError as e:
            QMessageBox.warning(self.stackedWidget, "Error", str(e))

    def confirmText(self,dialog ,stackedWidget, date, showtime, newDate, newTime, moviename, hallname, seatNo):
        self.stackedWidget = stackedWidget
        headingMsg = f"====== Are you sure to make these changes? =====\n"
        oldDate = f"\nOld Date: {self.date}\n"
        oldTime = f"Old Time: {self.showtime}\n"
        buffer = f"--------------------\n"
        nDate = f"New Date: {self.newDate}\n"
        nTime = f"New Time: {self.newTime}\n"

        message = headingMsg + oldDate + oldTime + buffer + nDate + nTime

        confirm = QMessageBox.question(self.stackedWidget, 'Change Ticket', message ,
                                        QMessageBox.Yes | QMessageBox.No)
        if confirm == QMessageBox.Yes:
            editTicController.editTicC(self,dialog ,stackedWidget, date, showtime,newDate, newTime, moviename, hallname, seatNo)

        self.listData()


    def refundTicket(self, stackedWidget,ticketList):
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
                
            refundTicController.refundTic(self, self.stackedWidget , ticketID ,moviename, hallname, seatNo, showtime, date, type, price)

            self.listData()
        
        except ValueError as e:
            QMessageBox.warning(self.stackedWidget, "Error" , str(e))

            
                
                #ticket().refundTic(self,dialog ,stackedWidget, date, showtime,newDate, newTime, moviename, hallname, seatNo)

            




