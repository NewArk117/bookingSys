import sys 
import sqlite3
import datetime
from PyQt5.QtWidgets import QMessageBox
sys.path.append( './Entity' )
#sys.path.append('C:/Users/USER/Desktop/BookingSys/bookingSys/BookingSYS/Entity')
from movie import movie

#11. Cinema Manager Controller
class susMovieController:
    def susMovieC(self, stackedWidget, moviesList):
        self.stackedWidget = stackedWidget
        self.moviesList = moviesList
        items = moviesList.currentItem()
        if items:
            movie().susMovie(self.stackedWidget, self.moviesList)
        

class addMovieController:
    def addMoviesC(self, stackedWidget, name , genre, startDate, endDate):
        self.stackedWidget = stackedWidget
        movie().addMovie(stackedWidget, name , genre, startDate, endDate)
        
 #9. Cinema Manager Controller
class listMovieController:
    def listMovieC(self, stackedWidget,list, num):
        self.stackedWidget = stackedWidget
        #9. Cinema Manager Entity (movie.py)
        movie().listManagerMovie(self.stackedWidget, list, num)

#10. Cinema Manager Controller
class editMovieController:
    def editMovieC(self, stackedwidget,dialog, movieList, name2, genre2, avail2):
        if movieList.currentItem():
            items = movieList.currentItem()
            print ("In controller")
            name = items.text()[:20].strip()
            movie1 = movie()
            moviename, genre, avail = movie1.getData(name)
            #print(moviename, genre, avail)
            #10. Cinema Manager Entity
            movie().editMovie(stackedwidget, dialog ,moviename ,genre,avail ,name2, genre2,avail2)


class searchMovieController:
    def searchMovieC(self, stackedWidget, item_name, list):
        self.stackedWidget = stackedWidget
        movie().searchMovie(self.stackedWidget,item_name, list) 

class viewMovieController:
    def viewMovieC(self, stackedWidget, moviesList):
        self.stackedWidget = stackedWidget
        self.moviesList = moviesList
        selected_item = self.moviesList.currentItem()
        # If an item is selected, display its name
        if selected_item is not None:
            item_name = selected_item.text()
            text,movieName = movie().viewMovie(self.stackedWidget,item_name)
            return text, movieName
        else:
            text=None
            moviename = None
            return text, moviename

