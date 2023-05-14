import sys 
sys.path.append( './Entity' )
from account import Account

class viewAccountController:
    def viewAccount(self, stackedWidget, item_name):
        self.stackedWidget = stackedWidget
        self.item_name = item_name
        Account().viewAccount(self.stackedWidget,item_name)
        