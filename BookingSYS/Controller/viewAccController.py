import sys 
sys.path.append( './Entity' )
from account import Account

class viewAccountController:
    def viewAccount(self, item_name)->list:
        self.item_name = item_name
        accountDetails = Account().viewAccount(item_name)
        return accountDetails
        