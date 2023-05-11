import sys 
import sqlite3
from PyQt5.QtWidgets import QMessageBox
sys.path.append( './Entity' )
#sys.path.append('C:/Users/USER/Desktop/BookingSys/bookingSys/BookingSYS/Entity')
from movie import movie

class delMovieController:
    def delMovieC(self, stackedWidget, moviesList):
        self.stackedWidget = stackedWidget
        self.moviesList = moviesList
        items = [item.text() for item in self.moviesList.selectedItems()]
        try:
            if not items:
                raise ValueError("Please select a hall.")
            else:
                movie().delMovie(self.stackedWidget, self.moviesList)
        except ValueError as e:
            QMessageBox.warning(self.stackedWidget, 'Error', str(e))
        

class addMovieController:
    def addMoviesC(self, stackedWidget, name , genre):
        self.stackedWidget = stackedWidget
        showtimes = ["1330", "1530", "1730", "1930", "2130"]
        self.hallAvail = ""
        self.hallNA = []
        self.hallYes = []
        try:
            conn = sqlite3.connect('SilverVillageUserAcc.db')
            cursor = conn.cursor()
            for time in showtimes:
                sql = "SELECT hallName FROM hallshowtime WHERE showtime = ? AND isAvailable = ?"
                data = (time, 1)
                cursor.execute(sql,data)
                hall_data = cursor.fetchall()
                for row in hall_data:
                    sql = "SELECT isAvailable FROM hall WHERE hallName = ?"
                    data = (row[0],)
                    cursor.execute(sql,data)
                    result = cursor.fetchone()
                    is_available = result[0]
                    if is_available == True:
                        self.hallAvail = row[0]
                    else:
                        self.hallAvail = ""
                
                if self.hallAvail == "":
                    self.hallNA.append(time)
                else:
                    self.hallYes.append([time, self.hallAvail])
                
            conn.close()
            print("This is hallNA" + str(self.hallNA))
            print("This is hallYes" + str(self.hallYes))

            if len(self.hallNA) == len(showtimes):
                raise ValueError("No cinema halls available for this movie.")
            elif len(self.hallNA) != 0: 
                showT = "| "
                for x in self.hallNA:
                    showT = showT + x + " | "
                message = f'These showtime(s) are not available for this movie:\n {showT} \nWould you like to proceed adding this movie?'
          
                confirm = QMessageBox.question(self.stackedWidget, 'Add Movies', message ,
                                                QMessageBox.Yes | QMessageBox.No)
                if confirm == QMessageBox.Yes:
                    movie().addMovie(stackedWidget,name,genre, self.hallYes)
            else:
                message = f'Proceed to add this movie?'
                confirm = QMessageBox.question(self.stackedWidget, 'Add Movies', message ,
                                                QMessageBox.Yes | QMessageBox.No)
                if confirm == QMessageBox.Yes:
                    movie().addMovie(stackedWidget,name,genre, self.hallYes)

        except ValueError as e:
            QMessageBox.warning(self.stackedWidget, 'Error', str(e))
        
        
class listMovieController:
    def listMovieC(self, stackedWidget,list):
        self.stackedWidget = stackedWidget
        movie().listManagerMovie(self.stackedWidget, list)

class editMovieController:
    def editMovieC(self, stackedwidget,dialog ,name , genre, name2, genre2):
        try:
            print ("In controller")
            if name2 == "" and genre2 == "" :
                print("All are empty")
                raise ValueError("New columns are empty")
            else:
                x = movie().editMovie(stackedwidget, dialog ,name ,genre,name2, genre2)
                return x
        except ValueError as e:
            QMessageBox.warning(self, 'Error', str(e))
