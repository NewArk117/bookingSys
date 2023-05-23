import sqlite3
import sys
import re

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont

sys.path.append('./Boundary')

from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QHBoxLayout, QListWidget, QVBoxLayout, QMessageBox, \
    QListWidgetItem, QDialog, QLineEdit, QDialogButtonBox, QGridLayout
from viewTicPurchasedController import TicketController
from fnbRefundController import FnbRefundController
from custAccController import AccountController
from FBController import FnbPurchasedController
from showTicController import ShowTicketController
from showFBController import ShowFBController

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
        #Call the showTic controlller
        showTicket = ShowTicketController.showTicketC(self)
        if showTicket == True:
            widget = self.stackedWidget.widget(20)
            widget.setID(self.userID)
            self.stackedWidget.setCurrentIndex(20)

    def show_fnb_record_window(self):
        #Call the showFB controlller
        showFB = ShowFBController.showFBC(self)
        if showFB == True:
            widget = self.stackedWidget.widget(21)
            widget.setID(self.userID)
            self.stackedWidget.setCurrentIndex(21)

    def show_account_info(self):
        widget = self.stackedWidget.widget(23)
        widget.setID(self.userID)
        print("1231",self.userID)
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
        self.viewData()
        self.ticket_delete_button = QPushButton('Refund')
        self.backButton = QPushButton("Back")

        layout = QVBoxLayout()
        layout.addWidget(self.label1)
        layout.addWidget(self.ticketList)
        hbox = QHBoxLayout()
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
        fnb_purchased_ui = self.stackedWidget.currentWidget()
        fnb_purchased_ui.refresh_fnb_record()



            

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

        self.controller = FnbPurchasedController(self.stackedWidget)

        self.layout = QVBoxLayout(self)
        self.layout.addWidget(QLabel('F&B Purchase Record'))
        self.layout.addWidget(self.fnb_list)

        button_layout = QHBoxLayout()
        button_layout.addWidget(self.back_button)
        button_layout.addWidget(self.refund_button)

        self.layout.addLayout(button_layout)

        self.back_button.clicked.connect(self.go_back)
        self.refund_button.clicked.connect(self.refund_ticket)

    def setID(self, userID):
        self.userID = userID
        self.show_fnb_record(userID)

    def show_fnb_record(self, userID):
        self.fnb_list.clear()

        try:
            fnb_data = self.controller.get_fnb_records(userID)

            for row in fnb_data:
                order_id, movie_name, showtime, date, food_name, quantity, total_price = row
                fnb_info = f"Order ID: {order_id}\nMovie Name: {movie_name}\nTime: {showtime}\nDate: {date}\nFood Items and Quantity: {food_name}\nTotal Quantity: {quantity}\nTotal Price: {total_price:.2f}\n"
                self.fnb_list.addItem(fnb_info)

        except Exception as e:
            print(f"An error occurred: {str(e)}")



    def go_back(self):
        self.stackedWidget.setCurrentIndex(8)
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
            self.show_refund_ui(order_id)
        else:
            QMessageBox.information(self, 'No Item Selected', 'Please select an item to refund.')

    def refresh_fnb_record(self):
        self.show_fnb_record(self.userID)


class AccountInfoUI(QWidget):
    def __init__(self, stackedWidget):
        super().__init__()
        self.stackedWidget = stackedWidget
        self.userID = ""

        self.setWindowTitle('Account Information')
        self.resize(400, 300)

        self.account_label = QLabel()
        self.account_label.setAlignment(Qt.AlignCenter)
        self.account_label.setFont(QFont("Arial", 12, QFont.Bold))

        self.update_button = QPushButton('Update')
        self.change_password_button = QPushButton('Change Password')
        self.back_button = QPushButton('Back')

        layout = QGridLayout()

        # Create a horizontal layout for the account_label
        account_layout = QHBoxLayout()
        account_layout.addWidget(self.account_label)
        account_layout.setAlignment(Qt.AlignCenter)

        layout.addLayout(account_layout, 0, 0, 3, 2)
        layout.addWidget(self.update_button, 3, 0, 1, 2)
        layout.addWidget(self.change_password_button, 4, 0, 1, 2)
        layout.addWidget(self.back_button, 5, 0, 1, 2)
        layout.setRowStretch(6, 1)

        self.setLayout(layout)

        self.update_button.clicked.connect(self.update_account_info)
        self.change_password_button.clicked.connect(self.change_password)
        self.back_button.clicked.connect(self.go_back)

        self.controller = AccountController()

    def setID(self, userID):
        self.userID = userID
        self.show_account_info(self.userID)

    def show_account_info(self, userID):
        username, DOB = self.controller.get_username(userID)
        self.account_label.setText(f'<b>Account ID:</b> {userID}<br><b>Name:</b> {username}<br><b>Age:</b> {DOB}')


    def update_account_info(self):
        try:
            dialog = QDialog(self)
            dialog.setWindowTitle('Update Account')
            dialog.setFixedSize(300, 250)

            user_id_label = QLabel('New Account ID:')
            username_label = QLabel('Name:')
            userage_label = QLabel('Age:')
            user_id_input = QLineEdit()
            username_input = QLineEdit()
            userage_input = QLineEdit()
            current_username, current_DOB = self.controller.get_username(self.userID)
            user_id_input.setText(self.userID)
            username_input.setText(current_username)
            userage_input.setText(str(current_DOB))

            button_box = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)

            layout = QVBoxLayout(dialog)
            layout.addWidget(user_id_label)
            layout.addWidget(user_id_input)
            layout.addWidget(username_label)
            layout.addWidget(username_input)
            layout.addWidget(userage_label)
            layout.addWidget(userage_input)

            layout.addWidget(button_box)

            button_box.accepted.connect(dialog.accept)
            button_box.rejected.connect(dialog.reject)

            if dialog.exec_() == QDialog.Accepted:
                new_userID = user_id_input.text()
                new_username = username_input.text()
                DOB = userage_input.text()
                if(current_username != new_userID):
                    if self.controller.is_user_id_exists(new_userID):
                        QMessageBox.information(self, 'Fail', 'The provided Account ID already exists. Please choose a different one.')
                    else:
                        self.controller.update_account_info(self.userID, new_userID, new_username, DOB)
                        self.userID = new_userID
                        self.show_account_info(self.userID)
                        QMessageBox.information(self, 'Success',
                                                'Account information updated successfully.Please log in again.')
                        self.stackedWidget.setCurrentIndex(1)
                else:
                    self.controller.update_account_info(self.userID, new_userID, new_username, DOB)
                    self.userID = new_userID
                    self.show_account_info(self.userID)
                    QMessageBox.information(self, 'Success', 'Account information updated successfully.')

        except Exception as e:
            print(f"An error occurred in the update_account_info method: {str(e)}")

    def change_password(self):
        try:
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
        except Exception as e:
            print(f"An error occurred in the change_password method: {str(e)}")

    def validate_and_change_password(self, dialog, old_password, new_password, confirm_password):
        try:
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
        except Exception as e:
            print(f"An error occurred in the validate_and_change_password method: {str(e)}")

    def go_back(self):
        try:
            self.stackedWidget.setCurrentIndex(8)
        except Exception as e:
            print(f"An error occurred in the go_back method: {str(e)}")


















