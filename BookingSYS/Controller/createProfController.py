import sys 
sys.path.append( './Entity' )
from userProfile import UserProfile

class createProfController:
    def createProf(self, userID, name, age, accType)->str:
        
        newProfile = UserProfile().createProfile(userID, name, age, accType)
        if newProfile == "Success":
            return "Success"
        elif newProfile == "stringError":
            return "stringError"
        elif newProfile == "emptyError":
            return "emptyError"
        else:
            return "integerError"
        