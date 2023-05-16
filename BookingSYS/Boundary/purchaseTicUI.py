import sqlite3
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QHBoxLayout, \
    QGridLayout, QComboBox, QTableWidget, QTableWidgetItem


class purchaseTicUI(QWidget):
    def __init__(self, stackedWidget):
        super().__init__()
        self.stackedWidget = stackedWidget

        self.setWindowTitle('SilverVillage Movie')
        self.resize(800, 600)

        self.welcome_label = QLabel('Welcome, customer!')
        self.welcome_label.setStyleSheet('font-size: 20px;')

        self.genres_list = ['Love', 'Thriller', 'Action', 'Family', 'Adventure', 'Sci-fi', 'Crime']

        self.genre_label = QLabel('Movie type:')
        self.genre_combobox = QComboBox()
        self.genre_combobox.addItems(self.genres_list)

        self.genre_combobox.currentIndexChanged.connect(self.filter_movies)

        self.search_label = QLabel('Search movies:')
        self.search_edit = QLineEdit()
        self.search_edit.setPlaceholderText('Enter movie name')
        self.search_button = QPushButton('Search')
        self.reset_button = QPushButton('Reset')
        self.search_button.clicked.connect(self.search_movies)
        self.reset_button.clicked.connect(self.reset_movies)

        self.movies_label = QLabel('Movie list:')
        self.movies_table = QTableWidget()
        self.movies_table.setColumnCount(4)
        self.movies_table.setHorizontalHeaderLabels(['Movie Name', 'Genre', 'Show Time', 'Hall Name'])
        self.movies_table.setMinimumSize(500, 400)

        self.buy_button = QPushButton('Buy ticket')
        self.buy_button.clicked.connect(self.buy_ticket)

        self.back_button = QPushButton('Back')
        self.back_button.clicked.connect(self.go_back)

        search_layout = QHBoxLayout()
        search_layout.addWidget(self.search_label)
        search_layout.addWidget(self.search_edit)
        search_layout.addWidget(self.search_button)
        search_layout.addWidget(self.reset_button)

        layout = QGridLayout()
        layout.addWidget(self.welcome_label, 0, 0, 1, 5)
        layout.addWidget(self.genre_label, 1, 0)
        layout.addWidget(self.genre_combobox, 1, 1)
        layout.addLayout(search_layout, 2, 0, 1, 5)
        layout.addWidget(self.movies_label, 3, 0)
        layout.addWidget(self.movies_table, 4, 0, 1, 5)
        layout.addWidget(self.buy_button, 5, 4, alignment=Qt.AlignRight)
        layout.addWidget(self.back_button, 5, 0, alignment=Qt.AlignLeft)
        layout.setSpacing(20)
        layout.setContentsMargins(40, 20, 40, 20)

        self.setLayout(layout)
        self.show_movies()

    def go_back(self):
        self.stackedWidget.setCurrentIndex(6)

    def show_movies(self):
        conn = sqlite3.connect('SilverVillageUserAcc.db')
        cursor = conn.cursor()
        cursor.execute('SELECT movieName, genre, showtime, hallName FROM movie')
        movies_data = cursor.fetchall()
        self.movies_table.setRowCount(len(movies_data))
        for row, data in enumerate(movies_data):
            for col, value in enumerate(data):
                item= QTableWidgetItem(str(value))
                self.movies_table.setItem(row, col, item)
        conn.close()

    def search_movies(self):
        conn = sqlite3.connect('SilverVillageUserAcc.db')
        cursor = conn.cursor()
        search_text = self.search_edit.text().strip()
        if search_text:
            cursor.execute("SELECT * FROM movie WHERE movieName LIKE ?", ('%' + search_text + '%',))
        else:
            cursor.execute('SELECT * FROM movie')
        movies_data = cursor.fetchall()
        self.movies_table.setRowCount(len(movies_data))
        for row, data in enumerate(movies_data):
            for col, value in enumerate(data):
                item = QTableWidgetItem(str(value))
                self.movies_table.setItem(row, col, item)
        conn.close()

    def reset_movies(self):
        self.search_edit.setText("")
        self.genre_combobox.setCurrentIndex(0)
        self.show_movies()

    def filter_movies(self):
        selected_genre = self.genre_combobox.currentText()
        conn = sqlite3.connect('SilverVillageUserAcc.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM movie WHERE genre=?", (selected_genre,))
        movies_data = cursor.fetchall()
        self.movies_table.setRowCount(len(movies_data))
        for row, data in enumerate(movies_data):
            for col, value in enumerate(data):
                item = QTableWidgetItem(str(value))
                self.movies_table.setItem(row, col, item)
        conn.close()

    def buy_ticket(self):
        pass
















