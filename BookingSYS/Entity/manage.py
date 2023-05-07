import sqlite3

#GUI Imports
from PyQt5.QtWidgets import QMessageBox

#Import links to different scripts in Boundary
import sys 
sys.path.append('./Boundary')

class Manage:
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

    def susHall(self, stackedWidget, moviesList):
        self.stackedWidget = stackedWidget
        self.moviesList = moviesList
        items = [self.moviesList.item(i).text() for i in range(self.moviesList.count())]
        items_str = ' '.join(items)
        try:
            if not items_str:
                raise ValueError("No hall selected")
            message = f'Are you sure you want to suspend {items_str} ?'     
            confirm = QMessageBox.question(self, 'Suspend hall', message ,
                                            QMessageBox.Yes | QMessageBox.No)
            if confirm == QMessageBox.Yes:
                print("ok")
                #insert sql to remove movie here 
        except ValueError as e:
            QMessageBox.warning(self.stackedWidget, 'Error', str(e))
            print(str(e))
    
    def delTics(self, stackedWidget, ticList):
        self.stackedWidget = stackedWidget
        self.ticList = ticList
        items = [self.ticList.item(i).text() for i in range(self.ticList.count())]
        items_str = ' '.join(items)
        try:
            if not items_str:
                raise ValueError("No ticket type selected")
            message = f'Are you sure you want to remove {items_str} ?'     
            confirm = QMessageBox.question(self, 'Remove ticket type', message ,
                                            QMessageBox.Yes | QMessageBox.No)
            if confirm == QMessageBox.Yes:
                print("ok")
                #insert sql to remove movie here 
        except ValueError as e:
            QMessageBox.warning(self.stackedWidget, 'Error', str(e))
            print(str(e))

    def delFB(self, stackedWidget, moviesList):
        self.stackedWidget = stackedWidget
        self.moviesList = moviesList
        items = [self.moviesList.item(i).text() for i in range(self.moviesList.count())]
        items_str = ' '.join(items)
        try:
            if not items_str:
                raise ValueError("No F&B selected")
            message = f'Are you sure you want to remove {items_str} ?'     
            confirm = QMessageBox.question(self, 'Remove F&B', message ,
                                            QMessageBox.Yes | QMessageBox.No)
            if confirm == QMessageBox.Yes:
                print("ok")
                #insert sql to remove movie here 
        except ValueError as e:
            QMessageBox.warning(self.stackedWidget, 'Error', str(e))
            print(str(e))