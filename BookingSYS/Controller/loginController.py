import sys 
sys.path.append( './Entity' )
from account import Account

class loginController:
    def checkLogin(self, stackedWidget, usrname, pw):
        self.stackedWidget = stackedWidget
        self.usrname = usrname
        self.pw = pw
        Account().login(self.stackedWidget, usrname, pw)
        