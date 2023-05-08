import sqlite3

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QTableWidget, QTableWidgetItem, QPushButton, QLabel


class purchaseFoodUI(QWidget):
    def __init__(self, stackedWidget):
        super().__init__()
        self.stackedWidget = stackedWidget

        self.setWindowTitle('Food Purchase')
        self.resize(400, 300)

        self.food_table = QTableWidget(self)
        self.food_table.setColumnCount(3)
        self.food_table.setHorizontalHeaderLabels(['Food', 'Price', 'Quantity'])

        self.purchase_button = QPushButton('Purchase', self)
        self.back_button = QPushButton('Back', self)

        title_label = QLabel('Food and Beverage', self)
        title_label.setAlignment(Qt.AlignCenter)
        title_label.setStyleSheet('font-size: 20px; font-weight: bold;')

        vbox = QVBoxLayout()
        vbox.addWidget(title_label)
        vbox.addWidget(self.food_table)
        vbox.addWidget(self.purchase_button)
        vbox.addWidget(self.back_button)
        vbox.setContentsMargins(20, 20, 20, 20)

        self.setLayout(vbox)

        self.purchase_button.clicked.connect(self.purchase)
        self.back_button.clicked.connect(self.back)
        self.show_food()


    def show_food(self):
        conn = sqlite3.connect('SilverVillageUserAcc.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM food')
        food_data = cursor.fetchall()
        self.food_table.setRowCount(len(food_data))
        for row, data in enumerate(food_data):
            for col, value in enumerate(data):
                item = QTableWidgetItem(str(value))
                self.food_table.setItem(row, col, item)
        conn.close()

    def purchase(self):
        pass

    def back(self):
        self.stackedWidget.setCurrentIndex(6)













