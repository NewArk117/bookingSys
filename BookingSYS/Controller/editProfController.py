import sys 
sys.path.append( './Entity' )
from userProfile import UserProfile

class editProfileController:
    def editProfile(self, item_name, name, age, accType, suspended)->str:
        self.item_name = item_name

        editedProf = UserProfile().editProfile(item_name, name, age, accType, suspended)
        
        return editedProf
        