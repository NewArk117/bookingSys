import sys 
sys.path.append( './Entity' )
from account import Account

class editAccountController:
    def editAccount(self, item_name, line)->bool:
        self.item_name = item_name

        editedAcc = Account().editAccount(item_name, line)
        if editedAcc == True:
            return True
        else:
            return False