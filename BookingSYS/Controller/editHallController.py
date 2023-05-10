import sys 
sys.path.append( './Entity' )
from PyQt5.QtWidgets import QMessageBox
#sys.path.append('C:/Users/USER/Desktop/BookingSys/bookingSys/BookingSYS/Entity')
from cinemaHall import cinemaHall

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