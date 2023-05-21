import sys 
sys.path.append( './Entity' )
from account import Account

class editAccountController:
    def editAccount(self, item_name)->list:
        self.item_name = item_name
        list1 = Account().editAccount(item_name)
        return list1