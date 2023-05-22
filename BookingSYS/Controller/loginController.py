import sys 
sys.path.append( './Entity' )
from account import Account

class loginController:
    def checkLogin(self, userID, password)->str:
        self.usrname = userID
        self.pw = password

        #Call the entitity
        user = Account().login(userID, password)
        if user == "error":
            return "error"
        elif user == "locked":
            return "locked"
        else:
            return user