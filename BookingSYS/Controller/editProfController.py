import sys 
sys.path.append( './Entity' )
from userProfile import UserProfile

class editProfileController:
    def editProfile(self, stackedWidget, item_name):
        self.stackedWidget = stackedWidget
        self.item_name = item_name
        UserProfile().editProfile(self.stackedWidget,item_name)
        