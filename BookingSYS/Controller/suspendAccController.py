import sys 
sys.path.append( './Entity' )
from account import Account

class suspendAccountController:
    def suspendAccount(self, item_name)->str:
        self.item_name = item_name

        suspendAcc = Account().suspendAccount(item_name)

        return suspendAcc