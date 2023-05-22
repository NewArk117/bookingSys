import sys 
sys.path.append( './Entity' )
from account import Account

class editAccountController:
    def editAccount(self, item_name, line, suspended)->bool:
        self.item_name = item_name

        editedAcc = Account().editAccount(item_name, line, suspended)
        
        return editedAcc