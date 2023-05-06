import sys 
sys.path.append( './Entity' )
from userProfile import UserProfile

class viewProfileController:
    def viewProfile(self, stackedWidget, item_name):
        self.stackedWidget = stackedWidget
        self.item_name = item_name
        UserProfile().viewProfile(self.stackedWidget,item_name)
        