import sys 
sys.path.append( './Entity' )
from userProfile import UserProfile

class viewAllProfileController:
    def viewAllProfile(self, stackedWidget, list):
        self.stackedWidget = stackedWidget
        UserProfile().viewAllProfile(self.stackedWidget, list)
        