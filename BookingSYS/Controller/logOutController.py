import sys 
sys.path.append( './Entity' )
from account import Account

class logOutController:
    def showTicketC(self)->bool:
        logout = Account().logout()
        if logout == True:
            return True