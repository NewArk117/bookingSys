import sys 
sys.path.append( './Entity' )
#sys.path.append('C:/Users/USER/Desktop/BookingSys/bookingSys/BookingSYS/Entity')
from manage import Manage

class delFBController:
    def delFBC(self, stackedWidget, fbList):
        self.stackedWidget = stackedWidget
        self.fbList = fbList
        Manage().delFB(self.stackedWidget, self.fbList)