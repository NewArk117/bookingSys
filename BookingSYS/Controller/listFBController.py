import sys 
sys.path.append( './Entity' )
#sys.path.append('C:/Users/USER/Desktop/BookingSys/bookingSys/BookingSYS/Entity')
from fnb import FnB

class listFBController:
    def listFBC(self, stackedWidget,list):
        self.stackedWidget = stackedWidget
        FnB().listManagerFB(self.stackedWidget, list)