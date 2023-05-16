import sqlite3

from PyQt5.QtCore import QStringListModel, Qt

from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QHBoxLayout, \
    QGridLayout, QComboBox, QListView, QAbstractItemView

class purchaseTicUI(QWidget):
    def __init__(self, stackedWidget):
        super().__init__()
        self.stackedWidget = stackedWidget

        self.setWindowTitle('SilverVillage Movie')
        self.resize(800, 600)

        self.welcome_label = QLabel('Welcome, customer!')
        self.welcome_label.setStyleSheet('font-size: 20px;')

        self.genres_list = ['Comedy', 'Action', 'Love', 'Horror', 'Sci-fi']
        self.sort_options = ['New', 'Hottest']

        self.genre_label = QLabel('Movie type:')
        self.genre_combobox = QComboBox()
        self.genre_combobox.addItems(self.genres_list)
        self.sort_label = QLabel('Sort by:')
        self.sort_combobox = QComboBox()
        self.sort_combobox.addItems(self.sort_options)

        self.search_label = QLabel('Search movies:')
        self.search_edit = QLineEdit()
        self.search_edit.setPlaceholderText('Enter movie name')
        self.search_button = QPushButton('Search')
        self.reset_button = QPushButton('Reset')
        self.search_button.clicked.connect(self.search_movies)
        self.reset_button.clicked.connect(self.reset_movies)

        self.movies_label = QLabel('Movie list:')
        self.movies_listview = QListView()
        self.movies_listview.setSelectionMode(QAbstractItemView.SingleSelection)
        self.movies_listview.setMinimumSize(500, 400)

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
        layout.addWidget(self.sort_label, 1, 3)
        layout.addWidget(self.sort_combobox, 1, 4)
        layout.addLayout(search_layout, 2, 0, 1, 5)
        layout.addWidget(self.movies_label, 3, 0)
        layout.addWidget(self.movies_listview, 4, 0, 1, 5)
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
        cursor.execute('SELECT * FROM movies')
        movies_data = cursor.fetchall()
        movie_strings = []
        for row in movies_data:
            movie_string = '{:<20}\t{:<30}\t{:<70}'.format(row[0], row[1], row[2])
            movie_strings.append(movie_string)
        movie_model = QStringListModel(movie_strings)
        self.movies_listview.setModel(movie_model)
        conn.close()

    def show_food(self):
        conn = sqlite3.connect('SilverVillageUserAcc.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM food')
        food_data = cursor.fetchall()
        food_strings = []
        for row in food_data:
            food_string = '{:<20}\t{:<30}\t{:<70}'.format(row[0], row[1], row[2])
            food_strings.append(food_string)
        food_model = QStringListModel(food_strings)
        self.food_listview.reset()
        self.food_listview.setModel(food_model)
        conn.close()

    def search_movies(self):
        conn = sqlite3.connect('SilverVillageUserAcc.db')
        cursor = conn.cursor()
        search_text = self.search_edit.text().strip()
        if search_text:
            cursor.execute("SELECT * FROM movies WHERE movieName LIKE ?", ('%' + search_text + '%',))
        else:
            cursor.execute('SELECT * FROM movies')
        movies_data = cursor.fetchall()
        movie_strings = []
        for row in movies_data:
            movie_string = '{:<20}\t{:<30}\t{:<70}'.format(row[0], row[1], row[2])
            movie_strings.append(movie_string)
        movie_model = QStringListModel(movie_strings)
        self.movies_listview.setModel(movie_model)
        conn.close()

    def reset_movies(self):
        self.search_edit.setText("")
        self.show_movies()


    def buy_ticket(self):
        return











