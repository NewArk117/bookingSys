import sys 
sys.path.append( './Entity' )
#sys.path.append('C:/Users/USER/Desktop/BookingSys/bookingSys/BookingSYS/Entity')
from manage import Manage

class delTicsController:
    def delTicsC(self, stackedWidget, ticList):
        self.stackedWidget = stackedWidget
        self.ticList = ticList
        Manage().delTics(self.stackedWidget, self.ticList)