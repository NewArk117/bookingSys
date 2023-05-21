import sys 
sys.path.append( './Entity' )
from userProfile import UserProfile

class createProfController:
    def createProf(self, userID, name, DOB, accType)->str:
        
        newProfile = UserProfile().createProfile(userID, name, DOB, accType)
        if newProfile == "Success":
            return "Success"
        elif newProfile == "stringError":
            return "stringError"
        else:
            return "integerError"