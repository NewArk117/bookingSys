import sys 
sys.path.append( './Entity' )
#sys.path.append('C:/Users/USER/Desktop/BookingSys/bookingSys/BookingSYS/Entity')
from login import login

class loginController:
    def checkLogin(self, stackedWidget, usrname, pw):
        self.stackedWidget = stackedWidget
        self.usrname = usrname
        self.pw = pw
        print("in Controller")
        login().fuc(self.stackedWidget, usrname, pw)
        