import sys 
sys.path.append( './Entity' )
from account import Account

class searchAccountController:
    def searchAccount(self, stackedWidget, item_name):
        self.stackedWidget = stackedWidget
        self.item_name = item_name
        Account().searchAccount(self.stackedWidget,item_name)
        