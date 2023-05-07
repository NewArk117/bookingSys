import sys 
sys.path.append( './Entity' )
#sys.path.append('C:/Users/USER/Desktop/BookingSys/bookingSys/BookingSYS/Entity')
from manage import Manage

class delHallsController:
    def delHallsC(self, stackedWidget, hallList):
        self.stackedWidget = stackedWidget
        self.hallList = hallList
        Manage().susHall(self.stackedWidget, self.hallList)