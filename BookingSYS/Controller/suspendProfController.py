import sys 
sys.path.append( './Entity' )
from userProfile import UserProfile

class suspendProfileController:
    def suspendProfile(self, item_name)->str:
        self.item_name = item_name

        suspendProf = UserProfile().suspendProfile(item_name)

        return suspendProf