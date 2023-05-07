import sys 
sys.path.append( './Entity' )
from account import Account

class editAccountController:
    def editAccount(self, stackedWidget, item_name):
        self.stackedWidget = stackedWidget
        self.item_name = item_name
        Account().editAccount(self.stackedWidget,item_name)
        