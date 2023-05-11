import sys 
sys.path.append( './Entity' )
from PyQt5.QtWidgets import QMessageBox
#sys.path.append('C:/Users/USER/Desktop/BookingSys/bookingSys/BookingSYS/Entity')
from cinemaHall import cinemaHall

class addHallController:
    def addHallC(self, stackedWidget, name , rows, columns):
        self.stackedWidget = stackedWidget
        try:
            if rows.isnumeric() and columns.isnumeric():
                cinemaHall().addHall(self.stackedWidget, name ,rows, columns)
            else:
                raise ValueError("Row/Column is not numerical")
        except ValueError as e:
            QMessageBox.warning(self, 'Error', str(e))