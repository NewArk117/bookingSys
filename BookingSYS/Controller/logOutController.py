import sys 
sys.path.append( './Entity' )
#sys.path.append('C:/Users/USER/Desktop/BookingSys/bookingSys/BookingSYS/Entity')
from account import Account

class logOutController:
    def loggingOut(self, stackedWidget):
        self.stackedWidget = stackedWidget
        Account().logout(self.stackedWidget)