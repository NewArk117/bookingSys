import sys 
sys.path.append( './Entity' )
from account import Account

class viewAllAccountController:
    def viewAllAccount(self, stackedWidget, list):
        self.stackedWidget = stackedWidget
        Account().viewAllAccount(self.stackedWidget, list)
        