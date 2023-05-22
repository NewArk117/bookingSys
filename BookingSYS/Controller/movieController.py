import sys 
import sqlite3
import datetime
from PyQt5.QtWidgets import QMessageBox
sys.path.append( './Entity' )
#sys.path.append('C:/Users/USER/Desktop/BookingSys/bookingSys/BookingSYS/Entity')
from movie import movie
from ticketType import ticketType


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
        list = movie().searchMovie(self.stackedWidget,item_name, list) 
        return list

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
#Customer Controller
class purchaseTicketController:
    def __init__(self, stackedWidget):
        self.stackedWidget = stackedWidget
        self.movie_entity = movie()
        self.ticket_entity = ticketType()

    def get_movies(self):
        return self.movie_entity.get_movies()

    def search_movies(self, search_text):
        return self.movie_entity.search_movies(search_text)

    def filter_movies(self, selected_genre):
        return self.movie_entity.filter_movies(selected_genre)

    def get_show_dates(self, name, genre):
        return self.movie_entity.get_show_dates(name, genre)

    def getRowcol(self, movie_name, genre):
        return self.movie_entity.get_hall_details(movie_name, genre)


    def getSeat(self, hall_name, showtime, date):
        return self.movie_entity.get_seats(hall_name, showtime, date)

    def get_ticket_types(self):
        return self.ticket_entity.get_ticket_types()


