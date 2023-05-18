import sqlite3
import sys
import re

sys.path.append('./Boundary')

from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QHBoxLayout, QListWidget, QVBoxLayout, QMessageBox, \
    QListWidgetItem, QDialog, QLineEdit, QDialogButtonBox


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
        print("Receieved", self.userID)

    def show_ticket_record_window(self):
        widget = self.stackedWidget.widget(20)
        widget.setID(self.userID)
        print("Sending", self.userID)
        self.stackedWidget.setCurrentIndex(20)

    def show_fnb_record_window(self):
        widget = self.stackedWidget.widget(21)
        widget.setID(self.userID)
        print("Sending", self.userID)
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
        self.viewData()
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
        print("Received 2 ", userID)

    def goBack(self):
        self.stackedWidget.setCurrentIndex(8)

    def viewData(self):
        print("ID here", self.userID)
        conn = sqlite3.connect('SilverVillageUserAcc.db')
        cursor = conn.cursor()
        sql = 'SELECT ticket_ID, movieName ,hallName ,seat_No ,showtime ,date ,type ,price FROM ticket WHERE userID = ?'
        data = (self.userID,)
        cursor.execute(sql, data)
        ticket_data = cursor.fetchall()
        ticket_strings = []
        for row in ticket_data:
            ticket_string = '{:<10}\t{:<20}\t{:<20}\t{:<20}\t{:<20}\t{:<20}\t{:<10}\t{:<10}'.format(row[0], row[1],
                                                                                                    row[2], row[3],
                                                                                                    row[4], row[5],
                                                                                                    row[6], row[7])
            ticket_strings.append(ticket_string)
        self.ticketList.clear()
        self.ticketList.addItems(ticket_strings)

        conn.commit()
        conn.close()

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
            self.deleteTicket(ticket_id)

    def deleteTicket(self, ticket_id):

        conn = sqlite3.connect('SilverVillageUserAcc.db')
        cursor = conn.cursor()

        sql = 'DELETE FROM ticket WHERE ticket_ID = ?'
        data = (ticket_id,)
        cursor.execute(sql, data)

        conn.commit()
        conn.close()

        QMessageBox.information(self, 'Success', 'Ticket refunded successfully.')
        self.viewData()

class fnbRefundUI(QWidget):
    def __init__(self, stackedWidget):
        super().__init__()
        self.stackedWidget = stackedWidget
        self.order_id = None
        self.order_id_label = QLabel()
        self.refund_confirmation_button = QPushButton('Refund Confirmation')
        self.back_button = QPushButton('Back')

        self.refund_confirmation_button.clicked.connect(self.confirm_refund)
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

    def set_order_id(self, order_id):
        self.order_id = order_id
        self.order_id_label.setText("Order ID: {}".format(order_id))
        self.show_food_list(order_id)  # Update the food list when order ID is set

    def go_back(self):
        self.stackedWidget.setCurrentIndex(21)

    def confirm_refund(self):
        selected_items = self.food_list.selectedItems()

        if len(selected_items) > 0:

            conn = sqlite3.connect('SilverVillageUserAcc.db')
            cursor = conn.cursor()

            for item in selected_items:
                food_info = item.text().split('\n')
                food_name = food_info[0].split(':')[1].strip()
                quantity = int(food_info[1].split(':')[1].strip())

                sql = '''
                DELETE FROM food_order_items
                WHERE order_id = ? AND food_name = ? AND quantity = ?
                '''

                data = (self.order_id, food_name, quantity)
                cursor.execute(sql, data)

            conn.commit()
            conn.close()

            self.show_food_list(self.order_id)# Update the food list after deletion
            self.stackedWidget.setCurrentIndex(8)


    def show_food_list(self, order_id):
        # Clear the food list
        self.food_list.clear()

       # Fetch and display the food items for the given order ID
        conn = sqlite3.connect('SilverVillageUserAcc.db')
        cursor = conn.cursor()

        sql = '''
        SELECT food_name, quantity
        FROM food_order_items
        WHERE order_id = ?
        '''

        data = (order_id,)
        cursor.execute(sql, data)
        food_items = cursor.fetchall()

        conn.close()

        for item in food_items:
            food_name, quantity = item
            food_info = f"Food Name: {food_name}\nQuantity: {quantity}\n"
            list_item = QListWidgetItem(food_info)
            self.food_list.addItem(list_item)



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

    def setID(self, userID):
        self.userID = userID
        self.show_account_info(self.userID)

    def show_account_info(self, userID):

        conn = sqlite3.connect('SilverVillageUserAcc.db')
        cursor = conn.cursor()

        # Get username from database based on userid
        sql = '''
        SELECT userName
        FROM account
        WHERE userID = ?
        '''
        data = (userID,)
        cursor.execute(sql, data)
        result = cursor.fetchone()

        conn.close()

        if result:
            username = result[0]
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


            conn = sqlite3.connect('SilverVillageUserAcc.db')
            cursor = conn.cursor()

            # Update userID and userName in the database
            sql = '''
            UPDATE account
            SET userID = ?,
                userName = ?
            WHERE userID = ?
            '''
            data = (new_userID, new_username, self.userID)
            cursor.execute(sql, data)
            conn.commit()

            conn.close()

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
        if old_password == self.get_password_from_database():
            if new_password == confirm_password:
                try:
                    conn = sqlite3.connect('SilverVillageUserAcc.db')
                    cursor = conn.cursor()

                    # update the password in the database
                    sql = '''
                    UPDATE account
                    SET password = ?
                    WHERE userID = ?
                    '''
                    data = (new_password, self.userID)
                    cursor.execute(sql, data)
                    conn.commit()

                    conn.close()

                    QMessageBox.information(self, 'Success', 'Password changed successfully.')
                except Exception as e:
                    print(f"An error occurred while changing password: {str(e)}")
            else:
                QMessageBox.warning(self, 'Error', 'New password and confirm password do not match.')
        else:
            QMessageBox.warning(self, 'Error', 'Incorrect old password.')

        dialog.accept()

    def get_password_from_database(self):

        conn = sqlite3.connect('SilverVillageUserAcc.db')
        cursor = conn.cursor()

        # Get password from database based on user id
        sql = '''
        SELECT password
        FROM account
        WHERE userID = ?
        '''
        data = (self.userID,)
        cursor.execute(sql, data)
        result = cursor.fetchone()

        conn.close()

        if result:
            return result[0]


    def go_back(self):
        self.stackedWidget.setCurrentIndex(8)





