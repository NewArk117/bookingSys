import sqlite3
import datetime
#GUI Imports
from PyQt5.QtWidgets import QMessageBox, QListWidgetItem, QGridLayout, QWidget, QLabel, QTextEdit
from PyQt5.QtCore import Qt
#Import links to different scripts in Boundary
import sys 
sys.path.append('./Boundary')

class movie:
    #8. Cinema Manager Entity
    def addMovie(self, stackedWidget, name , genre ,startDate, endDate):
        self.stackedWidget = stackedWidget
        conn = sqlite3.connect('SilverVillageUserAcc.db')
        cursor = conn.cursor()

        cursor.execute('SELECT movieName FROM movie')
        movie_data = cursor.fetchall()
        movieList = []
        for row in movie_data:
            movieList.append(row[0])

        if name not in movieList:

            self.hallAvail = ""
            self.hallYes = []

            datelist = []
            showtimes = ["1330", "1530", "1730", "1930", "2130"]
            showtimes2 = []
            #startDate = date.today()
            delta = datetime.timedelta(days=1)
            currentDate = startDate
            try:
                while currentDate <= endDate:
                    datelist.append(currentDate)
                    for time in showtimes:
                        showtimes2.append([currentDate, time])
                    currentDate += delta

                for date in datelist:
                    for time in showtimes:
                        sql = "SELECT hallName, date FROM hallshowtime WHERE showtime = ? AND isAvailable = ? AND date = ?"
                        data = (time,1, date)
                        cursor.execute(sql,data)
                        hall_data = cursor.fetchall()
                        for row in hall_data:
                            self.hallAvail = row[0]
                            self.hallYes.append([time,date, self.hallAvail])
                

                #print("This is hallNA" + str(self.hallNA))
                print("This is hallYes" + str(self.hallYes))

                startDateList = self.hallYes[0]
                endDateList = self.hallYes[-1]
                startDate = startDateList[1]
                endDate = endDateList[1]
                hall = startDateList[2]

                for x in showtimes:
                    sql2 = "INSERT INTO movie (movieName, genre, showtime, hallName, startdate, enddate, isAvailable) VALUES (?, ?, ?,?, ? ,?,?)"
                    data2 = (name, genre, int(x), hall, startDate, endDate, 1)
                    cursor.execute(sql2, data2)

                for x in self.hallYes:
                    time = int(x[0])
                    date = x[1]
                    hall = str(x[2])
                
                    sql3 = "UPDATE hallshowtime SET isAvailable = ? WHERE hallName = ? AND showtime = ? AND date = ?"
                    data3 = (0, hall, time , date)
                    cursor.execute(sql3, data3)
                    conn.commit()

                

                self.stackedWidget.setCurrentIndex(10)
            except:
                self.stackedWidget.setCurrentIndex(10)

        conn.close()


    def listManagerMovie(self, stackWidget, list, num):
        self.list = list
        conn = sqlite3.connect('SilverVillageUserAcc.db')
        cursor = conn.cursor()

        sql = "SELECT DISTINCT movieName, genre FROM movie"

        cursor.execute(sql)
        movie_data = cursor.fetchall()
        movie_strings = []
        for row in movie_data:
            #movie_string = '{:<20}\t{:<40}'.format(row[0], row[1])
            movie_string = '{:<20}'.format(row[0])
            movie_strings.append(movie_string)
        self.list.clear()
        self.list.addItems(movie_strings)
        conn.close()

    def susMovie(self, stackedWidget, movieList):
        self.stackedWidget = stackedWidget
        self.movieList = movieList
        items = self.movieList.currentItem()
        moviename = items.text()[:20].strip() 
        
        #insert sql to remove movie here 
        conn = sqlite3.connect('SilverVillageUserAcc.db')
        cursor = conn.cursor()

        sql = "SELECT showtime , hallname, startDate, endDate FROM movie WHERE movieName = ?"
        data = (moviename,)
        cursor.execute(sql, data)
        movie_data = cursor.fetchall()
        for row in movie_data:
            time = row[0]
            hall = row[1]
            startdate = row[2]
            enddate = datetime.datetime.strptime(row[3], '%Y-%m-%d')

            datelist = []
            delta = datetime.timedelta(days=1)
            #currentDate = startdate
            currentDate = datetime.datetime.strptime(startdate, '%Y-%m-%d')
            while currentDate <= enddate:
                datelist.append(currentDate)
                currentDateStr = currentDate.strftime('%Y-%m-%d')
                #print(currentDateStr)
                sql2 = "UPDATE hallshowtime SET isAvailable = ? WHERE hallName = ? AND showtime = ? AND  date = ?"
                data2 = (1, hall, time, currentDateStr)
                cursor.execute(sql2, data2)
                currentDate += delta

        sql3 = "UPDATE movie SET isAvailable = ? WHERE movieName = ? "
        data3 = (0 , moviename)
        cursor.execute(sql3, data3)

        conn.commit()
        conn.close()

        
    def editMovie(self, stackedwidget, dialog ,name , genre,avail1, name2, genre2,avail2):
        self.dialog = dialog
        self.stackedWidget= stackedwidget   

        conn = sqlite3.connect('SilverVillageUserAcc.db')
        cursor = conn.cursor()
        print(name , genre,avail1, name2, genre2,avail2)
        if name2 == "":
            name2 = name
        if genre2 == "":
            genre2 = genre
        if avail2 == "":
            avail2 = avail1
        print(name , genre,avail1, name2, genre2,avail2)
        cursor.execute('SELECT movieName FROM movie')
        movie_data = cursor.fetchall()
        movieList = []
        for row in movie_data:
            movieList.append(row[0])

        if name == name2:
            sql = "UPDATE movie SET movieName = ?, genre = ?, isAvailable = ? WHERE movieName = ? and genre = ? AND isAvailable = ?"
            data = (name2, genre2,avail2, name, genre, avail1)
            cursor.execute(sql, data)

            sql1 = "UPDATE ticket SET movieName = ? WHERE movieName = ?"
            data1 = (name2,  name)
            cursor.execute(sql1, data1)

        if name2 not in movieList:
            sql = "UPDATE movie SET movieName = ?, genre = ?, isAvailable = ? WHERE movieName = ? and genre = ? AND isAvailable = ?"
            data = (name2, genre2,avail2, name, genre, avail1)
            cursor.execute(sql, data)

            sql1 = "UPDATE ticket SET movieName = ? WHERE movieName = ?"
            data1 = (name2,  name)
            cursor.execute(sql1, data1)

            print(name2, name)

        # Commit the transaction
        conn.commit()

        # Close the database connection
        conn.close()

        self.dialog.reject()

        
    def searchMovie(self, stackedWidget, item_name, list):
            self.stackedWidget = stackedWidget
            self.list = list

            if item_name != "":
                conn = sqlite3.connect('SilverVillageUserAcc.db')
                cursor = conn.cursor()
                list.clear()
                sql = "SELECT DISTINCT * FROM Movie WHERE movieName = ?"
                value1 = item_name
                cursor.execute(sql, (value1,))
                
                rows = cursor.fetchall()
                # Iterate over the rows and populate the list widget with the data
                for row in rows:
                    item = QListWidgetItem(str(row[0]))
                self.list.addItem(item)

                # Close the cursor and the database connection
                cursor.close()
                conn.close()
                return list
            else:
                self.list = list
                # Connect to the database
                conn = sqlite3.connect('SilverVillageUserAcc.db')
                
                # Create a cursor object from the connection
                cursor = conn.cursor()
                list.clear()
                # Execute the SQL query to retrieve data from the table
                cursor.execute("SELECT DISTINCT movieName FROM movie")
                
                # Fetch all the rows that match the query
                rows = cursor.fetchall()

                # Iterate over the rows and populate the list widget with the data
                for row in rows:
                    item = QListWidgetItem(str(row[0]))
                    self.list.addItem(item)

                # Close the cursor and the database connection
                cursor.close()
                conn.close()

                return list
    def viewMovie(self, stackedWidget, item_name):
        conn = sqlite3.connect('SilverVillageUserAcc.db')
        # Get a cursor object
        cursor = conn.cursor()
        query = "SELECT * FROM movie WHERE movieName = ?"
        value1 = item_name.strip()
        # Execute the SQL query to retrieve data from the table
        cursor.execute(query, (value1,))
        # Fetch all the rows that match the query
        rows = cursor.fetchall()

        for row in rows:
            #self.message_box = QMessageBox()
            text = ("Movie Name: " + str(row[0]) + "\n" + "Genre: " + str(row[1]) + "\n" + "Hall Name: " + str(row[3]) + "\n" + "Start Date: " + str(row[4]) +"\n" + "End Date: " + str(row[5]) + "\n" +"Availability: " + str(row[6]))
            moviename=(str(row[0]))
        #self.message_box.exec_()
        
        # Close the cursor and the database connection
        cursor.close()
        conn.close()

        return text,moviename

    def getData(self, item_name):
        conn = sqlite3.connect('SilverVillageUserAcc.db')
        # Get a cursor object
        cursor = conn.cursor()
        query = "SELECT * FROM movie WHERE movieName = ?"
        value1 = item_name.strip()
        # Execute the SQL query to retrieve data from the table
        cursor.execute(query, (value1,))
        # Fetch all the rows that match the query
        rows = cursor.fetchall()
        for row in rows:
            self.moviename = str(row[0])
            self.genre = str(row[1])
            self.avail = str(row[6])
        # Close the cursor and the database connection
        cursor.close()
        conn.close()

        return self.moviename, self.genre, self.avail


    def get_movies(self):
        conn = sqlite3.connect('SilverVillageUserAcc.db')
        cursor = conn.cursor()
        cursor.execute('SELECT movieName, genre, showtime, hallName FROM movie')
        movies_data = cursor.fetchall()
        conn.close()
        return movies_data

    def search_movies(self, search_text):
        conn = sqlite3.connect('SilverVillageUserAcc.db')
        cursor = conn.cursor()
        if search_text:
            cursor.execute("SELECT * FROM movie WHERE movieName LIKE ?", ('%' + search_text + '%',))
        else:
            cursor.execute('SELECT * FROM movie')
        movies_data = cursor.fetchall()
        conn.close()
        return movies_data

    def filter_movies(self, selected_genre):
        conn = sqlite3.connect('SilverVillageUserAcc.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM movie WHERE genre=?", (selected_genre,))
        movies_data = cursor.fetchall()
        conn.close()
        return movies_data

    def get_show_dates(self, name, genre):
        conn = sqlite3.connect('SilverVillageUserAcc.db')
        cursor = conn.cursor()
        cursor.execute(
            "SELECT date FROM hallshowtime WHERE hallName = (SELECT hallName FROM movie WHERE movieName = ? AND genre = ?) AND date BETWEEN (SELECT startdate FROM movie WHERE movieName = ? AND genre = ?) AND (SELECT enddate FROM movie WHERE movieName = ? AND genre = ?)",
            (name, genre, name, genre, name, genre))
        show_dates = [row[0] for row in cursor.fetchall()]
        conn.close()
        return show_dates

    def get_hall_details(self, movie_name, genre):
        conn = sqlite3.connect('SilverVillageUserAcc.db')
        cursor = conn.cursor()

        hall_name = ""
        rows = 0
        columns = 0
        sql = "SELECT hallName, rows, columns FROM hall WHERE hallName = (SELECT hallName FROM movie WHERE movieName = ? AND genre = ?)"
        data = (movie_name, genre)
        cursor.execute(sql, data)
        movie_data = cursor.fetchall()
        for row in movie_data:
            hall_name = row[0]
            rows = row[1]
            columns = row[2]

        conn.commit()
        conn.close()

        return hall_name, rows, columns

    def get_seats(self, hall_name, showtime, date):
        conn = sqlite3.connect('SilverVillageUserAcc.db')
        cursor = conn.cursor()
        seatList = []
        sql = "SELECT seat_No, isAvailable FROM seat WHERE hallName = ? AND showtime = ? AND date =?"
        data = (hall_name, showtime, date)
        cursor.execute(sql, data)
        movie_data = cursor.fetchall()
        for row in movie_data:
            self.seatNo= row[0]
            self.isAvail = row[1]
            seatList.append([self.seatNo, self.isAvail])
        return seatList
        conn.commit()
        conn.close()
