import sys 
sys.path.append( './Entity' )
from account import Account

class viewAccountController:
    def viewAccount(self, stackedWidget):
        self.stackedWidget = stackedWidget
        Account().viewAccount(self.stackedWidget)
        