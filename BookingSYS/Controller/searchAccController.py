import sys 
sys.path.append( './Entity' )
from account import Account

class searchAccountController:
    def searchAccount(self, stackedWidget, item_name, list)->list:
        self.stackedWidget = stackedWidget
        list = Account().searchAccount(self.stackedWidget,item_name, list)
        return list
        