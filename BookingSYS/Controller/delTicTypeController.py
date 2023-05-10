import sys 
sys.path.append( './Entity' )
#sys.path.append('C:/Users/USER/Desktop/BookingSys/bookingSys/BookingSYS/Entity')
from ticketType import ticketType

class delTicTypeController:
    def delTicTypeC(self, stackedWidget, ticList):
        self.stackedWidget = stackedWidget
        self.ticList = ticList
        ticketType().delTicType(self.stackedWidget, self.ticList)