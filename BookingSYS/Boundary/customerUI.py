import sqlite3

from PyQt5.QtCore import QStringListModel, Qt

from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QHBoxLayout, \
    QGridLayout, QComboBox, QListWidget, QAbstractItemView,QVBoxLayout, QMessageBox

from movieController import listMovieController
from ticController import purchaseTicController, getTicController
from logOutController import logOutController

class customerUI(QWidget):
    def __init__(self, stackedWidget):
        super().__init__()
        self.stackedWidget = stackedWidget

        self.setWindowTitle('SilverVillage Movie')
        self.resize(600, 400)

        self.buy_button = QPushButton('Purchase Movie Tickets')
        self.buy_button.clicked.connect(self.buy_movie_tickets)

        self.buy_food_button = QPushButton('Purchase F&B')
        self.buy_food_button.clicked.connect(self.buy_food)

        self.info_button = QPushButton('Account Information')
        self.info_button.clicked.connect(self.show_personal_info)


        self.logout_button = QPushButton('Logout')
        self.logout_button.clicked.connect(self.logOut)

        layout = QVBoxLayout()
        layout.addWidget(self.buy_button)
        layout.addWidget(self.buy_food_button)
        layout.addWidget(self.info_button)
        layout.addWidget(self.logout_button)

        self.setLayout(layout)


    def buy_movie_tickets(self):
        self.stackedWidget.setCurrentIndex(7)

    def buy_food(self):
        self.stackedWidget.setCurrentIndex(18)

    def show_personal_info(self):
        self.stackedWidget.setCurrentIndex(8)

    def logOut(self):
        logOutController.loggingOut(self, self.stackedWidget)


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
        self.movies_listview = QListWidget()
        self.movies_listview.setSelectionMode(QAbstractItemView.SingleSelection)
        self.movies_listview.setMinimumSize(500, 400)

        self.number_label = QLabel('Number of Tickets:')
        self.ticType = ["Adult", "Senior", "Child"]
        number = ["1", "2", "3", "4" ,"5", "6", "7", "8", "9", "10"]
        self.noOfTics = QComboBox()
        self.noOfTics.addItems(number)

        self.buy_button = QPushButton('Buy ticket')
        self.buy_button.clicked.connect(self.purchaseTicket)

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
        layout.addWidget(self.number_label,5,0)
        layout.addWidget(self.noOfTics, 5, 1)
        layout.addWidget(self.buy_button, 8, 4, alignment=Qt.AlignRight)
        layout.addWidget(self.back_button, 8, 0, alignment=Qt.AlignLeft)
        layout.setSpacing(20)
        layout.setContentsMargins(40, 20, 40, 20)

        self.setLayout(layout)

        self.listMovie()

        #self.purchaseTicUI2 = purchaseTicUI2(self.stackedWidget,self.noOfTics.currentText())
        #self.stackedWidget.addWidget(self.purchaseTicUI2)
        self.stackedWidget.removeWidget(self.stackedWidget.widget(20))
    def go_back(self):
        self.stackedWidget.setCurrentIndex(6)

    def listMovie(self):
        listMovieController.listMovieC(self, self.stackedWidget, self.movies_listview, 0)

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


    def purchaseTicket(self):
        try:
            items = self.movies_listview.currentItem()
            if items:
                name = items.text()[:20].strip() 
                genre = items.text()[21:51].strip()
                time = items.text()[51:].strip()
                print(name + " " + genre + " " + time)
                purchaseTicUI2_instance = purchaseTicUI2(self.stackedWidget)
                purchaseTicUI2_instance.setName(self.noOfTics.currentText())
                purchaseTicUI2_instance.setList(name, genre, time)
                self.stackedWidget.addWidget(purchaseTicUI2_instance)

                self.stackedWidget.setCurrentIndex(20)
            else:
                raise ValueError("No movies selected")
        except ValueError as e:
                QMessageBox.warning(self.stackedWidget, 'Error', str(e))
                print(str(e))

        

        # Remove the widget at index 2
        #self.stackedWidget.removeWidget(self.stackedWidget.widget(20))

        #go to purchaseTicUI2 page
        


class purchaseTicUI2(QWidget):
    def __init__(self, stackedWidget):
        super().__init__()
        self.stackedWidget = stackedWidget
        self.number = '1'
        self.name = ""
        self.genre = ""
        self.time = ""

        self.setWindowTitle('SilverVillage Movie')
        self.resize(800, 600)

        layout = QGridLayout()

        

        self.movie_label = QLabel('Movie:')
        self.movie_text = QLabel(self.name)
        self.genre_label = QLabel("Genre:")
        self.genre_text = QLabel(self.genre)
        self.showtime_label = QLabel("Show Time:")
        self.showtime_text = QLabel(self.time)

        self.pushButton = QPushButton("Get name")
        

        self.confirm = QPushButton('Confirm')
        #self.confirm.clicked.connect(self.purchaseTicket)

        self.back_button = QPushButton('Back')
        #self.back_button.clicked.connect(self.go_back)

        #self.ticketWidget = self.getTicketWidget(self)

        #purchaseTicController.purchaseTicC(self, self.stackedWidget, self.movies_listview)
        #print("Number of Tickets: " + self.noOfTics.currentText())

        self.pushButton.clicked.connect(self.printName)

        #layout.addWidget(self.pushButton, 0 ,0 )
        layout.addWidget(self.movie_label, 0, 0)
        layout.addWidget(self.movie_text, 0 , 1)
        layout.addWidget(self.genre_label, 1, 0)
        layout.addWidget(self.genre_text, 1, 1)
        layout.addWidget(self.showtime_label, 2, 0)
        layout.addWidget(self.showtime_text, 2, 1)
        layout.addWidget(self.confirm, 8, 4, alignment = Qt.AlignRight)
        layout.addWidget(self.back_button, 8, 0, alignment=Qt.AlignLeft)

          

        self.setLayout(layout)

        #self.show()

    def setName(self, number):
        self.number = str(number)

    def setList(self, name ,genre, time):
        self.name = name
        self.genre = genre
        self.time = time
        self.movie_text.setText(self.name)
        self.genre_text.setText(self.genre)
        self.showtime_text.setText(self.time)

    def printName(self):
        print(self.name)
    
    def getTicketWidget(self):
        getTicController.getTicC(self, self.number)