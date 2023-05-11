import sys 
sys.path.append( './Entity' )
#sys.path.append('C:/Users/USER/Desktop/BookingSys/bookingSys/BookingSYS/Entity')
from cinemaHall import cinemaHall

class delHallsController:
    def delHallsC(self, stackedWidget, hallList):
        self.stackedWidget = stackedWidget
        self.hallList = hallList
        cinemaHall().susHall(self.stackedWidget, self.hallList)