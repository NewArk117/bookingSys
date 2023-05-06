import sys 
sys.path.append( './Entity' )
from account import Account

class createProfController:
    def createProf(self, stackedWidget, userID, name, DOB, accType):
        self.stackedWidget = stackedWidget
        Account().createProfile(self.stackedWidget, userID, name, DOB, accType)
       