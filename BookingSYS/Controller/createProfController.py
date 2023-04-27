import sys 
sys.path.append( './Entity' )
#sys.path.append('C:/Users/USER/Desktop/BookingSys/bookingSys/BookingSYS/Entity')
from profCreate import profCreate

class createProfController:
    def createProf(self, stackedWidget, profilename, systemR):
        self.stackedWidget = stackedWidget
        print("in Controller")
        profCreate().fuc(self.stackedWidget, profilename,systemR)
       