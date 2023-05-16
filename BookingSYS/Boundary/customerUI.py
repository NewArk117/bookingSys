import sqlite3
import sys
sys.path.append('./Boundary')
from PyQt5.QtCore import  Qt

from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QHBoxLayout, \
    QGridLayout, QComboBox, QListWidget, QVBoxLayout, QMessageBox, QListWidgetItem, QTableWidget, QTableWidgetItem
from ticController import purchaseTicController, getTicController
from logOutController import logOutController

class customerUI(QWidget):
    def __init__(self, stackedWidget):
        super().__init__()
        self.stackedWidget = stackedWidget

        self.userID = ""

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
        widget = self.stackedWidget.widget(7)
        widget.setID(self.userID)

    def buy_food(self):
        self.stackedWidget.setCurrentIndex(18)

    def show_personal_info(self):
        widget = self.stackedWidget.widget(8)
        widget.setID(self.userID)
        print("sending", self.userID)
        self.stackedWidget.setCurrentIndex(8)

    def logOut(self):
        logOutController.loggingOut(self, self.stackedWidget)

    def setID(self, userID):
        self.userID = userID


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
    
    def setID (self, userID):
        self.userID = userID

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
        try:
            selected_rows = self.movies_table.selectionModel().selectedRows()
            if len(selected_rows) > 0:
                row = selected_rows[0].row()
                name = self.movies_table.item(row, 0).text().strip()
                genre = self.movies_table.item(row, 1).text().strip()
                time = self.movies_table.item(row, 2).text().strip()
                print(name + " " + genre + " " + time)
                hallname, rows, cols = self.getRowCol(name, genre)
                datelist = self.getShowDate(name, genre)
                purchaseTicUI2_instance = purchaseTicUI2(self.stackedWidget)
                purchaseTicUI2_instance.setList(name, genre, datelist, rows, cols, hallname, self.userID)
                self.stackedWidget.addWidget(purchaseTicUI2_instance)
                self.stackedWidget.setCurrentWidget(purchaseTicUI2_instance)
                self.stackedWidget.show()
            else:
                raise ValueError("No movies selected")
        except ValueError as e:
            QMessageBox.warning(self, 'Error', str(e))
            print(str(e))

    def getShowDate(self, name ,genre):
        conn = sqlite3.connect('SilverVillageUserAcc.db')
        cursor = conn.cursor()

        datelist = []
        sql = " SELECT date FROM hallshowtime WHERE hallName = (SELECT hallName FROM movie WHERE movieName = ? AND genre = ?) AND date BETWEEN (SELECT startdate FROM movie WHERE movieName = ? AND genre = ?) AND (SELECT enddate FROM movie WHERE movieName = ? AND genre = ?)"
        data = (name, genre, name, genre, name, genre)
        cursor.execute(sql, data)
        movie_data = cursor.fetchall()
        for row in movie_data:
            datelist.append(row[0])
        #print(datelist)

        conn.commit()
        conn.close()

        return datelist
    
    def getRowCol(self,name, genre):
        conn = sqlite3.connect('SilverVillageUserAcc.db')
        cursor = conn.cursor()

        hallrow = 0
        hallcol = 0
        sql = "SELECT hallName, rows, columns FROM hall WHERE hallName = (SELECT hallName FROM movie WHERE movieName = ? AND genre = ?)"
        data = (name, genre)
        cursor.execute(sql, data)
        movie_data = cursor.fetchall()
        for row in movie_data:
            hallname = row[0]
            hallrow = row[1]
            hallcol = row[2]
        #print(datelist)

        conn.commit()
        conn.close()

        return hallname, hallrow, hallcol

        # Remove the widget at index 2
        #self.stackedWidget.removeWidget(self.stackedWidget.widget(20))

        #go to purchaseTicUI2 page
        


class purchaseTicUI2(QWidget):
    def __init__(self, stackedWidget):
        super().__init__()
        self.stackedWidget = stackedWidget
        self.ticnumber = 0
        self.hallName = ""
        self.name = ""
        self.genre = ""
        self.time = ""
        self.dates = []
        self.rows = 0
        self.cols = 0
        self.userID = ""
        showtimes = ["1330", "1530", "1730", "1930", "2130"]


        self.setWindowTitle('SilverVillage Movie')
        self.resize(800, 600)

        self.layout = QGridLayout()

        self.empty =QLabel("")

        movielayout =QHBoxLayout()
        genrelayout =QHBoxLayout()
        datelayout = QHBoxLayout()
        timelayout = QHBoxLayout()

        self.movie_label = QLabel('Movie:')
        self.movie_text = QLabel(self.name)

        self.genre_label = QLabel("Genre:")
        self.genre_text = QLabel(self.genre) 

        self.confirm = QPushButton('Confirm')
        #self.confirm.clicked.connect(self.purchaseTicket)

        self.selDate_label = QLabel("Select Date:")
        self.selDate_cbox = QComboBox()

        self.selTime_Label = QLabel("Select Show Time:")
        self.selTime_cbox = QComboBox()
        self.selTime_cbox.addItems(showtimes)

        self.chooseSeat = QPushButton("Select Seat")

        self.ticketLabel = QLabel("Tickets chosen:")
        self.ticketList = QListWidget()

        self.removeTic = QPushButton("Remove Ticket")
        self.removeTic.clicked.connect(self.remove_item)
        self.back_button = QPushButton('Back')
        self.back_button.clicked.connect(self.goBack)

        #self.selDate_cbox.currentIndexChanged.connect(self.datechanged)
        #self.selTime_cbox.currentIndexChanged.connect(self.timechanged)
        self.chooseSeat.clicked.connect(self.addSeating)
        self.confirm.clicked.connect(self.pushMe)
        
        #self.confirm.clicked.connect(self.getShowDate)

        #self.ticketWidget = self.getTicketWidget(self)

        #purchaseTicController.purchaseTicC(self, self.stackedWidget, self.movies_listview)
        #print("Number of Tickets: " + self.noOfTics.currentText())

        #self.ticketList.setItemDelegate(self.CustomDelegate())
        #layout.addWidget(self.pushButton, 0 ,0 )
        self.layout.addWidget(self.empty, 0 ,0 , 9, 1)
        movielayout.addWidget(self.movie_label)
        movielayout.addWidget(self.movie_text,alignment=Qt.AlignLeft)
        genrelayout.addWidget(self.genre_label)
        genrelayout.addWidget(self.genre_text, alignment=Qt.AlignLeft)
        datelayout.addWidget(self.selDate_label)
        datelayout.addWidget(self.selDate_cbox, alignment=Qt.AlignLeft)
        timelayout.addWidget(self.selTime_Label)
        timelayout.addWidget(self.selTime_cbox, alignment=Qt.AlignLeft)
        self.layout.addLayout(movielayout,0,0)
        self.layout.addLayout(genrelayout, 1,0)
        self.layout.addLayout(datelayout,2,0)
        self.layout.addLayout(timelayout, 3,0)
        self.layout.addWidget(self.chooseSeat,4 ,0)
        self.layout.addWidget(self.ticketLabel, 7, 0, alignment=Qt.AlignLeft)
        self.layout.addWidget(self.ticketList, 8 , 0, 3, 1)
        self.layout.addWidget(self.removeTic, 8, 2)
        self.layout.addWidget(self.confirm, 12, 4, alignment = Qt.AlignRight)
        self.layout.addWidget(self.back_button, 12, 0, alignment=Qt.AlignLeft)

          

        self.setLayout(self.layout)

        #self.show()


    def setList(self, name ,genre ,list, rows, cols, hallname, userID):
        #print(rows, cols)
        self.name = name
        self.genre = genre
        self.dates = list
        self.rows = rows
        self.cols = cols
        self.hallName = hallname
        self.userID = userID
        self.movie_text.setText(self.name)
        self.genre_text.setText(self.genre)
        self.selDate_cbox.addItems(self.dates)
    
    def getTicketWidget(self):
        getTicController.getTicC(self, self.ticnumber)

    def goBack(self):
        current_widget_index = self.stackedWidget.currentIndex()
        current_widget = self.stackedWidget.widget(current_widget_index)
        self.stackedWidget.removeWidget(current_widget)
        self.stackedWidget.setCurrentIndex(7)

    def addSeating(self):
        # Create a grid layout to hold the seats
        grid = QGridLayout()
        screen = QLabel("Screen")
        grid.addWidget(screen, 0 ,1, 1, self.cols)
        screen.setAlignment(Qt.AlignCenter)
        screen.setFixedSize(self.cols*75,20)
        
        # List of alphabets for row labels
        row_labels = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
        

        conn = sqlite3.connect('SilverVillageUserAcc.db')
        cursor = conn.cursor()

        seatList = []
        sql = "SELECT seat_No, isAvailable FROM seat WHERE hallName = ? AND showtime = ? AND date =?"
        cShowtime = self.selTime_cbox.currentText()
        cDate =  self.selDate_cbox.currentText()
        data = (self.hallName, cShowtime, cDate )
        cursor.execute(sql,data)
        movie_data = cursor.fetchall()
        for row in movie_data:
            self.seatNo = row[0]
            self.isAvail = row[1]
            seatList.append([self.seatNo, self.isAvail])

        conn.commit()
        conn.close()

        
        # Add a button for each seat in the grid
        for row in range(self.rows):
            for col in range(self.cols):
                seat = QPushButton(f"Seat {row_labels[row]}-{col+1}")
                self.seatAvail(row_labels[row], col+1,seatList, seat)
                grid.addWidget(seat, row+1, col)
                seat.clicked.connect(lambda _, row=row, col=col: self.on_seat_selected(row_labels[row], col,seatList, seat))

        #grid.addWidget(randomBtn, (self.rows + 4 ), 0)

        self.layout.addLayout(grid,5,0,2, 2)

        #self.chooseSeat.hide()

    def seatAvail(self, row, col, seatList, seatButton):
        
        self.seatNumber = str(row) + "-" + str(col)
        for seat in seatList:
            if seat[0] == self.seatNumber:
                #print("Seat is ", type(seat[1]))
                if seat[1] == 1:
                    #print("seat is available")
                    seatButton.setEnabled(True)
                else:
                    #print("seat not avail")
                    seatButton.setEnabled(False)

    def on_seat_selected(self, row, col, seatList, seatbtn):
        text1 = self.selTime_cbox.currentText()
        text2 = self.selDate_cbox.currentText()
        seat = f"{row}-{col+1}"
        #print(f"Seat {seat} selected")
        #print(f"Time chosen: {text1}")
        #print(f"Date chosen: {text2}")
        try:
            # Check if seat is already in the list
            for i in range(self.ticketList.count()):
                item = self.ticketList.item(i)
                widget = self.ticketList.itemWidget(item)
                seatLabel = widget.findChild(QLabel, "seatLabel")
                if seatLabel.text() == f"Seat Number: {seat}":
                    #print(f"Seat {seat} already added")
                    raise ValueError("Seat already selected")
                
            #print("Seat added to list")
            # Add seat to the list
            widget = QWidget()
            layout1 = QHBoxLayout()
            seatLabel = QLabel(f"Seat Number: {seat}", objectName="seatLabel")
            self.typebox, typeList = self.tictypebox()
            layout1.addWidget(seatLabel)
            layout1.addWidget(self.typebox)
            widget.setLayout(layout1)

            item = QListWidgetItem()
            item.setSizeHint(widget.sizeHint())
            self.ticketList.addItem(item)
            self.ticketList.setItemWidget(item, widget)

        except ValueError as e:
            QMessageBox.warning(self.stackedWidget, 'Error', str(e))
            print(str(e))
        

        #print(self.ticketList.count())

    def remove_item(self):
        current_row = self.ticketList.currentRow()
        if current_row >= 0:
            item = self.ticketList.takeItem(current_row)
            del item

        
    def pushMe(self):
        selTime = self.selTime_cbox.currentText()
        selDate = self.selDate_cbox.currentText()
        movieMsg = f'Movie name: {self.name}\n'
        genreMsg = f'Genre: {self.genre}\n'
        dateMsg = f'Date: {selDate}\n'
        timeMsg = f'Show Time: {selTime}\n'
        hall = f'Hall:{self.hallName}\n'
        
        item_count = self.ticketList.count()
        ticNumMsg = f'Total Number of tickets: {item_count}\n'
        self.ticket = ""

        ticBox, ticketlist = self.tictypebox()

        totalCost = 0
        seatList = []
        for row in range(item_count):
            item = self.ticketList.item(row)
            item_widget = self.ticketList.itemWidget(item)
            label = item_widget.findChild(QLabel).text()
            combo_box = item_widget.findChild(QComboBox)
            combo_box_value = combo_box.currentText()
            #print(f"Selected option for item {row}: {combo_box_value}")
            #print(f"Label for item {row}: {label}")

            for x in ticketlist:
                if x[0] == combo_box_value:
                    price = x[1]
                    self.ticket = self.ticket + f"{label},  Type: {combo_box_value},  Price: {price}\n"
                    seat = label.split(":")[1].strip()
                    seatList.append([seat,combo_box_value, price])
                    totalCost = totalCost + price
                    
        costMsg = f"------------------\nTotal price is ${totalCost}\n------------------\n"
        payMsg = f"\nProceed to purchase?"

        message = movieMsg + genreMsg + dateMsg + timeMsg + hall + ticNumMsg + self.ticket + costMsg + payMsg
        confirm = QMessageBox.question(self.stackedWidget, 'Buy ticket', message ,
                                        QMessageBox.Yes | QMessageBox.No)
        if confirm == QMessageBox.Yes:
            print("Ok")
            purchaseTicController.purchaseTicC(self,self.stackedWidget, self.name, self.genre, self.hallName, selDate, selTime,item_count,seatList, totalCost, self.userID )


    def tictypebox(self):
        typeBox = QComboBox()
        conn = sqlite3.connect('SilverVillageUserAcc.db')
        cursor = conn.cursor()

        self.typeList = []
        self.priceList= []
        sql = "SELECT * FROM ticketType"
        cursor.execute(sql)
        type_data = cursor.fetchall()
        for row in type_data:
            typename = row[0]
            price = row[1]
            self.typeList.append(typename)
            self.priceList.append([typename, price])

        conn.commit()
        conn.close()

        typeBox.addItems(self.typeList)
        return typeBox, self.priceList
    
    

    
