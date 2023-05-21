import sys 
sys.path.append( './Entity' )
from userProfile import UserProfile

class searchProfileController:
    def searchProfile(self, stackedWidget, item_name, list)->list:
        self.stackedWidget = stackedWidget
        list = UserProfile().searchProfile(self.stackedWidget,item_name, list)
        return list
        