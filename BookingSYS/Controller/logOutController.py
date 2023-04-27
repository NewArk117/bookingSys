import sys 
sys.path.append( './Entity' )
#sys.path.append('C:/Users/USER/Desktop/BookingSys/bookingSys/BookingSYS/Entity')
from logO import logO

class logOutController:
    def loggingOut(self, stackedWidget):
        self.stackedWidget = stackedWidget
        print("in logout Controller")
        logO().fuc(self.stackedWidget)