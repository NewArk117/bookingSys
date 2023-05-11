import sys 
sys.path.append( './Entity' )
#sys.path.append('C:/Users/USER/Desktop/BookingSys/bookingSys/BookingSYS/Entity')
from cinemaHall import cinemaHall

class listHallController:
    def listHallC(self, stackedWidget,list):
        self.stackedWidget = stackedWidget
        cinemaHall().listManagerHall(self.stackedWidget, list)