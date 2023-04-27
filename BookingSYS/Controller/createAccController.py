import sys 
sys.path.append( './Entity' )
#sys.path.append('C:/Users/USER/Desktop/BookingSys/bookingSys/BookingSYS/Entity')
from accCreate import accCreate

class createAccController:
    def createAcc(self, stackedWidget, fname, lname, age, username, password, accType):
        self.stackedWidget = stackedWidget
        print("in Controller")
        accCreate().fuc(self.stackedWidget, fname, lname, age, username, password, accType)
        