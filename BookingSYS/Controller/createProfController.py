import sys 
sys.path.append( './Entity' )
from userProfile import UserProfile

class createProfController:
    def createProf(self, stackedWidget, userID, name, DOB, accType):
        self.stackedWidget = stackedWidget
        UserProfile().createProfile(self.stackedWidget, userID, name, DOB, accType)
       