import sqlite3

from PyQt5.QtCore import QStringListModel


from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QGridLayout, QComboBox, QTextEdit, QListView


class purchaseUI(QWidget):
    def __init__(self, stackedWidget):
        super().__init__()
        self.stackedWidget = stackedWidget


        self.setWindowTitle('SilverVillage Movie')
        self.resize(600, 600)

        self.welcome_label = QLabel(f'Welcome，customer！')
        self.welcome_label.setStyleSheet('font-size: 20px;')


        self.genres_list = ['comedy', 'action', 'love', 'horror', 'Sci-fi']
        self.sort_options = ['New', 'hottest']

        self.genre_label = QLabel('movie type:')
        self.genre_combobox = QComboBox()
        self.genre_combobox.addItems(self.genres_list)
        self.sort_label = QLabel('sort by:')
        self.sort_combobox = QComboBox()
        self.sort_combobox.addItems(self.sort_options)


        self.search_label = QLabel('Search Movies:')
        self.search_edit = QLineEdit()
        self.search_edit.setPlaceholderText('Enter movie name')


        self.search_button = QPushButton('Search')
        self.reset_button = QPushButton('Reset')
        self.search_button.clicked.connect(self.search_movies)
        self.reset_button.clicked.connect(self.reset_movies)


        self.movies_label = QLabel('Movie List:')
        self.movies_listview = QListView()


        self.food_label = QLabel('Food')
        self.food_listview = QListView()



        layout = QGridLayout()
        layout.addWidget(self.welcome_label, 0, 0, 1, 2)
        layout.addWidget(self.genre_label, 1, 0)
        layout.addWidget(self.genre_combobox, 1, 1)
        layout.addWidget(self.sort_label, 1, 2)
        layout.addWidget(self.sort_combobox, 1, 3)
        layout.addWidget(self.search_label, 2, 0)
        layout.addWidget(self.search_edit, 2, 1, 1, 2)
        layout.addWidget(self.search_button, 2, 3)
        layout.addWidget(self.reset_button, 2, 4)
        layout.addWidget(self.movies_label, 3, 0)
        layout.addWidget(self.movies_listview, 4, 0, 1, 2)
        layout.addWidget(self.food_label, 3, 2)
        layout.addWidget(self.food_listview, 4, 2, 1, 2)

        self.buy_button = QPushButton('Buy Ticket')
        self.buy_button.clicked.connect(self.buy_ticket)
        layout.addWidget(self.buy_button, 4, 4)

        self.setLayout(layout)

        self.show_movies()
        self.show_food()

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
        self.food_listview.reset()  # 重置food_listview
        self.food_listview.setModel(food_model)  # 设置新的模型
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











