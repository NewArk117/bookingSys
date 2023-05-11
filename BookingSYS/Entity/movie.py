import sqlite3

#GUI Imports
from PyQt5.QtWidgets import QMessageBox, QLineEdit, QGridLayout, QWidget, QLabel, QTextEdit
from PyQt5.QtCore import Qt
#Import links to different scripts in Boundary
import sys 
sys.path.append('./Boundary')

class movie:
    def delMovie(self, stackedWidget, moviesList):
        self.stackedWidget = stackedWidget
        self.moviesList = moviesList
        items = [self.moviesList.item(i).text() for i in range(self.moviesList.count())]
        items_str = ' '.join(items)
        try:
            if not items_str:
                raise ValueError("No movies selected")
            message = f'Are you sure you want to remove {items_str} ?'     
            confirm = QMessageBox.question(self, 'Remove movie', message ,
                                            QMessageBox.Yes | QMessageBox.No)
            if confirm == QMessageBox.Yes:
                print("ok")
                #insert sql to remove movie here 
        except ValueError as e:
            QMessageBox.warning(self.stackedWidget, 'Error', str(e))
            print(str(e))

    def addMovie(self, stackedWidget, name , genre ,list):
        self.stackedWidget = stackedWidget
        conn = sqlite3.connect('SilverVillageUserAcc.db')
        cursor = conn.cursor()
        
        for x in list:
            time = int(x[0])
            hall = str(x[1])
            print("This is time " + str(time) + " This is hall " + hall)
            sql2 = "INSERT INTO movie (movieName, genre, showtime, hallName) VALUES (?, ?, ?,?)"
            data2 = (name, genre, time, hall)
            cursor.execute(sql2, data2)
            conn.commit()

            sql3 = "UPDATE hallshowtime SET isAvailable = ? WHERE hallName = ? AND showtime = ?"
            data3 = (0, hall, time)
            cursor.execute(sql3, data3)
            conn.commit()

        
        conn.close()

        print ("Done adding")

        self.stackedWidget.setCurrentIndex(10)
    
    
    def listManagerMovie(self, stackWidget, list):
        self.list = list
        conn = sqlite3.connect('SilverVillageUserAcc.db')
        cursor = conn.cursor()
        cursor.execute('SELECT DISTINCT movieName, genre FROM movie')
        movie_data = cursor.fetchall()
        movie_strings = []
        for row in movie_data:
            movie_string = '{:<20}\t{:<30}'.format(row[0], row[1])
            movie_strings.append(movie_string)
        self.list.clear()
        self.list.addItems(movie_strings)
        conn.close()

    def delMovie(self, stackedWidget, movieList):
            self.stackedWidget = stackedWidget
            self.movieList = movieList
            items = [self.movieList.item(i).text() for i in range(self.movieList.count())]
            for item in items:
                words = item.split()
                moviename = words[0]
                print(moviename)
            items_str = ' '.join(' '.join(items).split())     

            try:
                if not items_str:
                    raise ValueError("No F&B selected")
                message = f'Are you sure you want to remove {moviename} ?'     
                confirm = QMessageBox.question(self.stackedWidget, 'Remove Movie', message ,
                                                QMessageBox.Yes | QMessageBox.No)
                if confirm == QMessageBox.Yes:
                    print("ok")
                    #insert sql to remove movie here 
                    conn = sqlite3.connect('SilverVillageUserAcc.db')
                    cursor = conn.cursor()

                    sql = "SELECT showtime, hallname FROM movie WHERE movieName = ?"
                    data = (moviename,)
                    cursor.execute(sql, data)
                    movie_data = cursor.fetchall()
                    for row in movie_data:
                        time = row[0]
                        hall = row[1]
                        sql2 = "UPDATE hallshowtime SET isAvailable = ? WHERE hallName = ? AND showtime = ?"
                        data2 = (1, hall, time)
                        cursor.execute(sql2, data2)

                    sql3 = "DELETE FROM movie WHERE movieName = ? "
                    data3 = (moviename,)
                    cursor.execute(sql3, data3)

                    conn.commit()
                    conn.close()

                    self.listManagerMovie(self.stackedWidget, self.movieList) 

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

        
        



        