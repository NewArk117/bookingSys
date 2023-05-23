import sys 
sys.path.append( './Entity' )
from account import Account

class ShowAccController:
    def showAccC(self)->bool:
        AccRecord = Account().showAccRecord()
        if AccRecord == True:
            return True