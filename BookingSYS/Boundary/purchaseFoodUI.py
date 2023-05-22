from PyQt5.QtWidgets import QWidget, QTableWidget, QHBoxLayout, QVBoxLayout, QLabel, QPushButton, QTableWidgetItem, \
    QSpinBox, QMessageBox
from PyQt5.QtCore import Qt
from custFnBController import FoodController
from ticController import TicketController
from FBController import PurchaseFoodController

class purchaseFoodUI(QWidget):
    def __init__(self, stackedWidget):
        super().__init__()
        self.stackedWidget = stackedWidget

        self.userID = ""

        self.setWindowTitle('Food Purchase')
        self.resize(600, 300)

        self.food_table = QTableWidget(self)
        self.food_table.setColumnCount(5)
        self.food_table.setHorizontalHeaderLabels(['Food', 'Price', 'Quantity', "Purchase", 'Total'])

        self.movie_table = QTableWidget(self)
        self.movie_table.setColumnCount(4)
        self.movie_table.setHorizontalHeaderLabels(["Ticket ID", 'Movie Name', 'Time', 'Date'])

        self.purchase_button = QPushButton('Purchase', self)
        self.back_button = QPushButton('Back', self)

        title_label = QLabel('Food and Beverage', self)
        title_label.setAlignment(Qt.AlignCenter)
        title_label.setStyleSheet('font-size: 20px; font-weight: bold;')

        hbox = QHBoxLayout()
        hbox.addWidget(self.food_table)
        hbox.addWidget(self.movie_table)

        vbox = QVBoxLayout()
        vbox.addWidget(title_label)
        vbox.addLayout(hbox)
        vbox.addWidget(self.purchase_button)
        vbox.addWidget(self.back_button)
        vbox.setContentsMargins(20, 20, 20, 20)

        self.setLayout(vbox)
        self.controller = PurchaseFoodController()


        self.purchase_button.clicked.connect(self.purchase)
        self.back_button.clicked.connect(self.back)
        self.show_food()


    def setID(self, userID):
        self.userID = userID
        self.refresh_ui(userID)


    def show_food(self):
        food_data = FoodController.get_food(self)
        self.food_table.setRowCount(len(food_data))
        for row, data in enumerate(food_data):
            food_name, price, quantity, available = data[0], data[1], data[2], data[3]
            item_name = QTableWidgetItem(food_name)
            item_price = QTableWidgetItem(str(price))
            item_quantity = QTableWidgetItem(str(quantity))
            item_purchase = QSpinBox()
            item_purchase.setMinimum(0)
            item_purchase.setMaximum(quantity)
            item_purchase.setValue(0)
            item_purchase.valueChanged.connect(self.update_total_price)
            item_total = QTableWidgetItem('0.00')
            self.food_table.setItem(row, 0, item_name)
            self.food_table.setItem(row, 1, item_price)
            self.food_table.setItem(row, 2, item_quantity)
            self.food_table.setCellWidget(row, 3, item_purchase)
            self.food_table.setItem(row, 4, item_total)

            if available == 0:
                item_name.setFlags(item_name.flags() & ~Qt.ItemIsSelectable)
                item_price.setFlags(item_price.flags() & ~Qt.ItemIsSelectable)
                item_quantity.setFlags(item_quantity.flags() & ~Qt.ItemIsSelectable)
                item_purchase.setEnabled(False)
                item_total.setFlags(item_total.flags() & ~Qt.ItemIsSelectable)

    def viewData(self, userID):
        self.userID = userID
        ticket_data = TicketController.get_tickets(self.userID)
        self.movie_table.setRowCount(len(ticket_data))
        for row, data in enumerate(ticket_data):
            ticket_id, movie_name, showtime, date = data
            item_ticket = QTableWidgetItem(str(ticket_id))
            item_movie = QTableWidgetItem(movie_name)
            item_time = QTableWidgetItem(str(showtime))
            item_date = QTableWidgetItem(date)
            self.movie_table.setItem(row, 0, item_ticket)
            self.movie_table.setItem(row, 1, item_movie)
            self.movie_table.setItem(row, 2, item_time)
            self.movie_table.setItem(row, 3, item_date)

    def purchase(self):
        total_price = 0.0
        flag = True
        order_list = []

        for row in range(self.food_table.rowCount()):
            item_purchase = self.food_table.cellWidget(row, 3)
            quantity = item_purchase.value()
            if quantity != 0:
                flag = False
                food_name = self.food_table.item(row, 0).text()
                order_list.append((food_name, quantity))

        if flag:
            QMessageBox.warning(self, 'Invalid Selection', 'All food items are out of stock.')
            return
        selected_row = self.movie_table.currentRow()
        if selected_row == -1:
            QMessageBox.warning(self, 'No Movie Selected', 'Please select which movie you want to buy F&B for.')
            return


        for row in range(self.food_table.rowCount()):
            item_purchase = self.food_table.cellWidget(row, 3)
            item_price = float(self.food_table.item(row, 1).text())
            quantity = item_purchase.value()
            total = item_price * quantity
            self.food_table.item(row, 4).setText('{:.2f}'.format(total))
            total_price += total

        confirmation_text = "Food Order:\n"
        for food_name, quantity in order_list:
            confirmation_text += f"- {food_name}: {quantity}\n"
        confirmation_text += f"\nTotal Price: ${total_price:.2f}"
        confirmation_text += "\nMovie Details:\n"
        movie_name_item = self.movie_table.item(selected_row, 1)
        movie_time_item = self.movie_table.item(selected_row, 2)
        movie_date_item = self.movie_table.item(selected_row, 3)
        movie_name = movie_name_item.text()
        movie_time = movie_time_item.text()
        movie_date = movie_date_item.text()
        confirmation_text += f"- Movie: {movie_name}\n"
        confirmation_text += f"- Time: {movie_time}\n"
        confirmation_text += f"- Date: {movie_date}\n"

        confirm_dialog = QMessageBox(self)
        confirm_dialog.setWindowTitle("Confirmation")
        confirm_dialog.setText("Please confirm your purchase:")
        confirm_dialog.setInformativeText(confirmation_text)
        confirm_dialog.setIcon(QMessageBox.Question)
        confirm_dialog.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        confirm_dialog.setDefaultButton(QMessageBox.No)
        confirm_dialog.setStyleSheet("QLabel{min-width: 500px;}")
        result = confirm_dialog.exec()

        if result == QMessageBox.Yes:
            ticket_id_item = self.movie_table.item(selected_row, 0)
            ticket_id = int(ticket_id_item.text())
            self.controller.save_food_order(self.userID, ticket_id, order_list)
            for food_name, quantity in order_list:
                self.controller.update_fnb(food_name, quantity)
            QMessageBox.information(self, 'Successful Purchase', 'Your purchase has been successfully processed.')
            self.refresh_ui(self.userID)
        else:
            QMessageBox.information(self, 'Purchase Cancelled', 'Your purchase has been cancelled.')

    def update_total_price(self):
        total_price = 0.0
        for row in range(self.food_table.rowCount()):
            item_quantity = self.food_table.cellWidget(row, 3)
            item_price = float(self.food_table.item(row, 1).text())
            quantity = item_quantity.value()
            total = item_price * quantity
            self.food_table.item(row, 4).setText('{:.2f}'.format(total))
            total_price += total
        return total_price

    def back(self):
        self.stackedWidget.setCurrentIndex(6)

    def refresh_ui(self, userID):
        self.show_food()
        self.viewData(userID)



















