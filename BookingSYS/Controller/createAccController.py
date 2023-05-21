import sys 
sys.path.append( './Entity' )
#sys.path.append('C:/Users/USER/Desktop/BookingSys/bookingSys/BookingSYS/Entity')
from account import Account

class createAccController:
    def createAcc(self, userID, password, accType)->str:

        #Call the entity
        newAccount = Account().createAccount(userID, password, accType)

        if newAccount == "Success":
            return "Success"
        elif newAccount == "IDError":
            return "IDError"
        else:
            return "emptyError"
        