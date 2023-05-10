import sys 
sys.path.append( './Entity' )
#sys.path.append('C:/Users/USER/Desktop/BookingSys/bookingSys/BookingSYS/Entity')
from manage import Manage

class listFBController:
    def listFBC(self, stackedWidget,list):
        self.stackedWidget = stackedWidget
        Manage().showFB(self.stackedWidget, list)