import sys 
sys.path.append( './Entity' )
#sys.path.append('C:/Users/USER/Desktop/BookingSys/bookingSys/BookingSYS/Entity')
from manage import Manage

class listTicketController:
    def listTicC(self, stackedWidget,list):
        self.stackedWidget = stackedWidget
        Manage().showTicType(self.stackedWidget, list)