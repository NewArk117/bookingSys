import sys 
sys.path.append( './Entity' )
from account import Account

class searchAccountController:
    def searchAccount(self, stackedWidget, item_name, list):
        self.stackedWidget = stackedWidget
        Account().searchAccount(self.stackedWidget,item_name, list)
        