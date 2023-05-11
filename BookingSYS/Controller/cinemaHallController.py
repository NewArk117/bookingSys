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

class delHallsController:
    def delHallsC(self, stackedWidget, hallList):
        self.stackedWidget = stackedWidget
        self.hallList = hallList
        items = [item.text() for item in self.hallList.selectedItems()]
        try:
            if not items:
                raise ValueError("Please select a hall.")
            else:
                cinemaHall().susHall(self.stackedWidget, self.hallList)
        except ValueError as e:
            QMessageBox.warning(self.stackedWidget, 'Error', str(e))
        


class editHallController:
    def editHallC(self, stackedwidget,dialog ,name , row, column, avail, name2, rows2, columns2, avail2):
        try:
            print ("In controller")
            if name2 == "" and rows2 == "" and columns2 == "" and avail2 == "" :
                print("All are empty")
                raise ValueError("New columns are empty")
            else:
                x = cinemaHall().editHall(stackedwidget, dialog ,name , row, column, avail, name2, rows2, columns2, avail2)
                return x
        except ValueError as e:
            QMessageBox.warning(self, 'Error', str(e))

class listHallController:
    def listHallC(self, stackedWidget,list):
        self.stackedWidget = stackedWidget
        cinemaHall().listManagerHall(self.stackedWidget, list)

