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
    def addMovie(self, stackedWidget, name , genre ,list, startDate, endDate):
        self.stackedWidget = stackedWidget
        conn = sqlite3.connect('SilverVillageUserAcc.db')
        cursor = conn.cursor()

        startDateList = list[0]
        endDateList = list[-1]
        startDate = startDateList[1]
        endDate = endDateList[1]
        hall = startDateList[2]

        showtimes = ["1330", "1530", "1730", "1930", "2130"]


        for x in showtimes:
            sql2 = "INSERT INTO movie (movieName, genre, showtime, hallName, startdate, enddate) VALUES (?, ?, ?,?, ? ,?)"
            data2 = (name, genre, int(x), hall, startDate, endDate)
            cursor.execute(sql2, data2)

        for x in list:
            time = int(x[0])
            date = x[1]
            hall = str(x[2])
        
            sql3 = "UPDATE hallshowtime SET isAvailable = ? WHERE hallName = ? AND showtime = ? AND date = ?"
            data3 = (0, hall, time , date)
            cursor.execute(sql3, data3)
            conn.commit()

        
        conn.close()

        print ("Done adding")

        self.stackedWidget.setCurrentIndex(10)
    
    
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

    def delMovie(self, stackedWidget, movieList):
            self.stackedWidget = stackedWidget
            self.movieList = movieList
            items = self.movieList.currentItem()
                 

            try:
                if not items:
                    raise ValueError("No Movie selected")
                else:
                    moviename = items.text()[:20].strip() 
                message = f'Are you sure you want to remove {moviename} ?'     
                confirm = QMessageBox.question(self.stackedWidget, 'Remove Movie', message ,
                                                QMessageBox.Yes | QMessageBox.No)
                if confirm == QMessageBox.Yes:
                    print("ok")
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

                    sql3 = "DELETE FROM movie WHERE movieName = ? "
                    data3 = (moviename,)
                    cursor.execute(sql3, data3)

                    conn.commit()
                    conn.close()

                    self.listManagerMovie(self.stackedWidget, self.movieList, 1) 

            except ValueError as e:
                QMessageBox.warning(self.stackedWidget, 'Error', str(e))
                print(str(e))

    def editMovie(self, stackedwidget, dialog ,name , genre, name2, genre2):
        self.dialog = dialog
        self.stackedWidget= stackedwidget
        try:   
            if name2 == "":
                name2 = name
            if genre2 == "":
                genre2 = genre
    
            message = f'Confirm these changes(?)\n\nOLD----\nMovie Name:{name}\nGenre:{genre}\n\nNEW----\nMovie Name:{name2}\nGenre:{genre2}'

            confirm = QMessageBox.question(self.stackedWidget, 'Update Movie', message ,
                                            QMessageBox.Yes | QMessageBox.No)
            if confirm == QMessageBox.Yes:
                conn = sqlite3.connect('SilverVillageUserAcc.db')
                cursor = conn.cursor()
  
                sql = "UPDATE movie SET movieName = ?, genre = ? WHERE movieName = ? and genre = ?"
                data = (name2, genre2, name, genre)
                cursor.execute(sql, data)

                # Commit the transaction
                conn.commit()

                # Close the database connection
                conn.close()

                self.dialog.reject()
                return True
                
        except ValueError as e:
            QMessageBox.warning(self.stackedWidget, 'Error', str(e))
            print(str(e))

        
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
            message_box = QMessageBox()
            message_box.setText("Movie Name: " + str(row[0]) + "\n" + "Genre: " + str(row[1]) + "\n" + "Hall Name: " + str(row[3]) + "\n" + "Start Date: " + str(row[4]) + "End Date: " + str(row[5]) + "Availability: " + str(row[6]))
            message_box.setWindowTitle(str(row[0]))
            message_box.exec_()
        
        # Close the cursor and the database connection
        cursor.close()
        conn.close()