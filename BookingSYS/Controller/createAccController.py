import sys 
sys.path.append( './Entity' )
#sys.path.append('C:/Users/USER/Desktop/BookingSys/bookingSys/BookingSYS/Entity')
from account import Account

class createAccController:
    def createAcc(self, stackedWidget, userID, username, password, accType):
        self.stackedWidget = stackedWidget
        Account().createAccount(self.stackedWidget, userID,username, password, accType)
        