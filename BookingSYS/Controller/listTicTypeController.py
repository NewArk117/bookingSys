import sys 
sys.path.append( './Entity' )
#sys.path.append('C:/Users/USER/Desktop/BookingSys/bookingSys/BookingSYS/Entity')
from ticketType import ticketType

class listTicTypeController:
    def listTicTypeC(self, stackedWidget,list):
        self.stackedWidget = stackedWidget
        ticketType().listTicType(self.stackedWidget, list)