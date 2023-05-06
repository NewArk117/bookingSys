import sys 
sys.path.append( './Entity' )
from account import Account

class loginController:
    def checkLogin(self, stackedWidget, usrname, pw, acctype):
        self.stackedWidget = stackedWidget
        self.usrname = usrname
        self.pw = pw
        self.acctype = acctype
        Account().login(self.stackedWidget, usrname, pw, acctype)
        