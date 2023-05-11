import sys 
sys.path.append( './Entity' )
#sys.path.append('C:/Users/USER/Desktop/BookingSys/bookingSys/BookingSYS/Entity')
from fnb import FnB

class delFBController:
    def delFBC(self, stackedWidget, fbList):
        self.stackedWidget = stackedWidget
        self.fbList = fbList
        FnB().delFB(self.stackedWidget, self.fbList)
