import sys 
sys.path.append( './Entity' )
from userProfile import UserProfile

class viewProfileController:
    def viewProfile(self, item_name)->list:
        self.item_name = item_name
        profileDetails = UserProfile().viewProfile(item_name)
        return profileDetails
