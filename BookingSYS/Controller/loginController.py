import sys 
sys.path.append( './Entity' )
from account import Account

class loginController:
    def checkLogin(self, userID, pw)->str:
        self.usrname = userID
        self.pw = pw

        #Call the entitity
        user = Account().login(userID, pw)

        return user