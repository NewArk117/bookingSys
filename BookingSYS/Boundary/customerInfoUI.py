import sqlite3
import sys
import re

sys.path.append('./Boundary')

from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QHBoxLayout, QListWidget, QVBoxLayout, QMessageBox, \
    QListWidgetItem, QDialog, QLineEdit, QDialogButtonBox
from viewTicPurchasedController import TicketController
from fnbRefundController import FnbRefundController
from custAccController import AccountController



# This class shows the record of buying tickets or food
class customerInfoUI(QWidget):
    def __init__(self, stackedWidget):
        super().__init__()
        self.stackedWidget = stackedWidget
        self.fnb_record_window = None

        self.userID = ""

        self.setWindowTitle('Account Information')
        self.resize(400, 300)

        self.record_button = QPushButton('Ticket Purchase Record', self)
        self.record_button.setGeometry(150, 100, 300, 30)

        self.fnb_record_button = QPushButton('F&B Purchase Record', self)
        self.fnb_record_button.setGeometry(150, 150, 300, 30)

        self.account_info_button = QPushButton('Account Information', self)
        self.account_info_button.setGeometry(150, 200, 300, 30)

        self.account_info_button.clicked.connect(self.show_account_info)

        self.back_button = QPushButton('Back', self)
        self.back_button.setGeometry(150, 250, 300, 30)

        self.record_button.clicked.connect(self.show_ticket_record_window)
        self.fnb_record_button.clicked.connect(self.show_fnb_record_window)
        self.back_button.clicked.connect(self.go_back)

    def go_back(self):
        self.stackedWidget.setCurrentIndex(6)

    def setID(self, userID):
        self.userID = userID

    def show_ticket_record_window(self):
        widget = self.stackedWidget.widget(20)
        widget.setID(self.userID)
        self.stackedWidget.setCurrentIndex(20)

    def show_fnb_record_window(self):
        widget = self.stackedWidget.widget(21)
        widget.setID(self.userID)
        self.stackedWidget.setCurrentIndex(21)

    def show_account_info(self):
        widget = self.stackedWidget.widget(23)
        widget.setID(self.userID)
        self.stackedWidget.setCurrentIndex(23)

class ticketPurchasedUI(QWidget):
    def __init__(self, stackedWidget):
        super().__init__()
        self.stackedWidget = stackedWidget

        self.userID = ""
        ticket_string = '{:<10}\t{:<20}\t{:<20}\t{:<20}\t{:<20}\t{:<30}\t{:<10}\t{:<10}'.format('TicketID',
                                                                                                "Movie Name",
                                                                                                "Hall Name",
                                                                                                "Seat Number",
                                                                                                "Show Time", "Date",
                                                                                                "Ticket Type", "Cost")
        self.label1 = QLabel(ticket_string)
        self.ticketList = QListWidget()
        self.listData()
        self.ticket_delete_button = QPushButton('Refund')
        self.ticket_update_button = QPushButton('Change')
        self.backButton = QPushButton("Back")

        layout = QVBoxLayout()
        layout.addWidget(self.label1)
        layout.addWidget(self.ticketList)
        hbox = QHBoxLayout()
        hbox.addWidget(self.ticket_update_button)
        hbox.addWidget(self.ticket_delete_button)
        hbox.addWidget(self.backButton)

        self.backButton.clicked.connect(self.goBack)
        self.ticket_delete_button.clicked.connect(self.confirmRefund)

        layout.addLayout(hbox)

        self.setLayout(layout)
        self.stackedWidget.currentChanged.connect(self.viewData)

    def setID(self, userID):
        self.userID = userID
        #print("Received 2 ", userID)

    def goBack(self):
        self.stackedWidget.setCurrentIndex(8)

    def viewData(self):
        ticket_controller = TicketController(self)
        ticket_controller.retrieveUserTickets()

    def confirmRefund(self):
        selected_items = self.ticketList.selectedItems()
        if not selected_items:
            return

        selected_item = selected_items[0]
        ticket_info = selected_item.text()
        ticket_id = ticket_info.split('\t')[0]
        movie_name = ticket_info.split('\t')[1]
        hall_name = ticket_info.split('\t')[2]
        seat_number = ticket_info.split('\t')[3]
        show_time = ticket_info.split('\t')[4]
        data = ticket_info.split('\t')[5]
        ticket_type = ticket_info.split('\t')[6]
        cost = ticket_info.split('\t')[7]

        confirm_dialog = QMessageBox(self)
        confirm_dialog.setIcon(QMessageBox.Question)
        confirm_dialog.setWindowTitle("Confirm Refund")
        confirm_dialog.setText(f"Are you sure you want to refund the following ticket?\n\nTicket ID: {ticket_id}"
                               f"\nMovie Name:{movie_name}\nHall Name:{hall_name}\nSeat Number:{seat_number}\nShow Time:{show_time}"
                               f"\nDate:{data}\nTicket Type:{ticket_type}\nCost:{cost}")
        confirm_dialog.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        confirm_dialog.setDefaultButton(QMessageBox.No)

        result = confirm_dialog.exec_()
        if result == QMessageBox.Yes:
            ticket_controller = TicketController(self)
            ticket_controller.deleteTicket(ticket_id)


class fnbRefundUI(QWidget):
    def __init__(self, stackedWidget):
        super().__init__()
        self.stackedWidget = stackedWidget
        self.order_id = None
        self.order_id_label = QLabel()
        self.refund_confirmation_button = QPushButton('Refund Confirmation')
        self.back_button = QPushButton('Back')

        self.back_button.clicked.connect(self.go_back)

        self.food_list = QListWidget()
        self.food_list.setSelectionMode(QListWidget.MultiSelection)  # Enable multi-selection mode

        layout = QVBoxLayout(self)
        layout.addWidget(self.order_id_label)
        layout.addWidget(QLabel('Food List:'))
        layout.addWidget(self.food_list)

        button_layout = QHBoxLayout()
        button_layout.addWidget(self.back_button)
        button_layout.addWidget(self.refund_confirmation_button)
        layout.addLayout(button_layout)

        self.controller = FnbRefundController(self)
        self.refund_confirmation_button.clicked.connect(self.controller.confirm_refund)

    def set_order_id(self, order_id):
        self.order_id = order_id
        self.order_id_label.setText("Order ID: {}".format(order_id))
        self.controller.show_food_list(order_id)  # Update the food list when order ID is set

    def go_back(self):
        self.stackedWidget.setCurrentIndex(21)

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

            

class fnbPurchasedUI(QWidget):
    def __init__(self, stackedWidget):
        super().__init__()
        self.stackedWidget = stackedWidget
        self.userID = ""
        self.order_id = None
        self.fnb_list = QListWidget()
        self.back_button = QPushButton('Back')
        self.refund_button = QPushButton('Refund')

        self.fnb_list.itemClicked.connect(self.enable_refund_button)

    def setID(self, userID):
        self.userID = userID
        print("Received 2", userID)
        self.setup_ui(self.userID)

    def setup_ui(self, userID):
        layout = QVBoxLayout(self)
        layout.addWidget(QLabel('F&B Purchase Record'))
        layout.addWidget(self.fnb_list)

        button_layout = QHBoxLayout()
        button_layout.addWidget(self.back_button)
        button_layout.addWidget(self.refund_button)

        layout.addLayout(button_layout)

        self.back_button.clicked.connect(self.go_back)
        self.refund_button.clicked.connect(self.refund_ticket)

        self.show_fnb_record(userID)

    def go_back(self):
        self.stackedWidget.setCurrentIndex(8)

    def show_fnb_record(self, userID):
        # Clear the fnb_list before displaying new records
        self.fnb_list.clear()

        try:
            conn = sqlite3.connect('SilverVillageUserAcc.db')
            cursor = conn.cursor()

            sql = '''
            SELECT fo.order_id, t.movieName, t.showtime, t.date, GROUP_CONCAT(foi.food_name || ' (' || foi.quantity || ')'), SUM(foi.quantity), SUM(foi.quantity * food.price)
            FROM food_orders fo
            JOIN ticket t ON fo.ticket_id = t.ticket_ID
            JOIN food_order_items foi ON fo.order_id = foi.order_id
            JOIN food ON foi.food_name = food.foodName
            WHERE fo.user_id = ?
            GROUP BY fo.order_id, t.movieName, t.date, t.showtime
            '''

            data = (userID,)
            cursor.execute(sql, data)
            fnb_data = cursor.fetchall()

            conn.close()

            for row in fnb_data:
                order_id, movie_name, showtime, date, food_name, quantity, total_price = row
                fnb_info = f"Order ID: {order_id}\nMovie Name: {movie_name}\nTime: {showtime}\nDate: {date}\nFood Items and Quantity: {food_name}\nTotal Quantity: {quantity}\nTotal Price: {total_price:.2f}\n"
                self.fnb_list.addItem(fnb_info)

        except Exception as e:
            print(f"An error occurred: {str(e)}")

    def enable_refund_button(self, item):
        # Enable the refund button when a food order row is selected
        selected_text = item.text()
        order_id = self.extract_order_id(selected_text)
        if order_id is not None:
            self.order_id = order_id
            self.refund_button.setEnabled(True)
        else:
            self.refund_button.setEnabled(False)
            self.order_id = None  # Clear the order_id when no valid order is selected

    def extract_order_id(self, selected_text):
        order_id = None
        match = re.search(r"Order ID:\s+(\d+)", selected_text)
        if match:
            order_id = match.group(1)
        return order_id

    def show_refund_ui(self, order_id):
        refund_ui = fnbRefundUI(self.stackedWidget)
        refund_ui.set_order_id(order_id)
        self.stackedWidget.addWidget(refund_ui)
        self.stackedWidget.setCurrentWidget(refund_ui)

    def refund_ticket(self):
        selected_item = self.fnb_list.currentItem()
        if selected_item is not None:
            selected_text = selected_item.text()
            order_id = self.extract_order_id(selected_text)
            if order_id is not None:
                refund_ui = fnbRefundUI(self.stackedWidget)
                refund_ui.set_order_id(order_id)
                self.stackedWidget.addWidget(refund_ui)
                self.stackedWidget.setCurrentWidget(refund_ui)
        else:
            QMessageBox.information(self, 'No Item Selected', 'Please select an item to refund.')



class AccountInfoUI(QWidget):
    def __init__(self, stackedWidget):
        super().__init__()
        self.stackedWidget = stackedWidget
        self.userID = ""

        self.setWindowTitle('Account Information')
        self.resize(400, 300)

        self.account_label = QLabel()
        self.update_button = QPushButton('Update')
        self.change_password_button = QPushButton('Change Password')
        self.back_button = QPushButton('Back')

        layout = QVBoxLayout()
        layout.addWidget(self.account_label)
        layout.addWidget(self.update_button)
        layout.addWidget(self.change_password_button)
        layout.addWidget(self.back_button)

        self.setLayout(layout)

        self.update_button.clicked.connect(self.update_account_info)
        self.change_password_button.clicked.connect(self.change_password)
        self.back_button.clicked.connect(self.go_back)

        self.controller = AccountController()

    def setID(self, userID):
        self.userID = userID
        self.show_account_info(self.userID)

    def show_account_info(self, userID):
        username = self.controller.get_username(userID)
        if username:
            self.account_label.setText(f'Account ID: {userID}\nAccount Name: {username}')
        else:
            self.account_label.setText('Account Name: N/A')

    def update_account_info(self):
        dialog = QDialog(self)
        dialog.setWindowTitle('Update Account')
        dialog.setFixedSize(300, 150)

        user_id_label = QLabel('New Account ID:')
        username_label = QLabel('New Account Name:')
        user_id_input = QLineEdit()
        username_input = QLineEdit()

        button_box = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)

        layout = QVBoxLayout(dialog)
        layout.addWidget(user_id_label)
        layout.addWidget(user_id_input)
        layout.addWidget(username_label)
        layout.addWidget(username_input)
        layout.addWidget(button_box)

        button_box.accepted.connect(dialog.accept)
        button_box.rejected.connect(dialog.reject)

        if dialog.exec_() == QDialog.Accepted:
            new_userID = user_id_input.text()
            new_username = username_input.text()

            self.controller.update_account_info(self.userID, new_userID, new_username)

            self.userID = new_userID
            self.show_account_info(self.userID)
            QMessageBox.information(self, 'Success', 'Account information updated successfully.')

    def change_password(self):
        dialog = QDialog(self)
        dialog.setWindowTitle('Change Password')
        dialog.setFixedSize(400, 250)

        old_password_label = QLabel('Old Password:')
        new_password_label = QLabel('New Password:')
        confirm_password_label = QLabel('Confirm Password:')

        old_password_input = QLineEdit()
        old_password_input.setEchoMode(QLineEdit.Password)

        new_password_input = QLineEdit()
        new_password_input.setEchoMode(QLineEdit.Password)

        confirm_password_input = QLineEdit()
        confirm_password_input.setEchoMode(QLineEdit.Password)

        button_box = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)

        layout = QVBoxLayout(dialog)
        layout.addWidget(old_password_label)
        layout.addWidget(old_password_input)
        layout.addWidget(new_password_label)
        layout.addWidget(new_password_input)
        layout.addWidget(confirm_password_label)
        layout.addWidget(confirm_password_input)
        layout.addWidget(button_box)

        button_box.accepted.connect(lambda: self.validate_and_change_password(dialog, old_password_input.text(), new_password_input.text(), confirm_password_input.text()))
        button_box.rejected.connect(dialog.reject)

        dialog.exec_()

    def validate_and_change_password(self, dialog, old_password, new_password, confirm_password):
        if old_password == self.controller.get_password(self.userID):
            if new_password == confirm_password:
                try:
                    self.controller.update_password(self.userID, new_password)
                    QMessageBox.information(self, 'Success', 'Password changed successfully.')
                except Exception as e:
                    print(f"An error occurred while changing password: {str(e)}")
            else:
                QMessageBox.warning(self, 'Error', 'New password and confirm password do not match.')
        else:
            QMessageBox.warning(self, 'Error', 'Incorrect old password.')

        dialog.accept()

    def go_back(self):
        self.stackedWidget.setCurrentIndex(8)


