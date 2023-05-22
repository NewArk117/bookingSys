import sys
sys.path.append( './Entity' )
from account import Account
class userRegController:
    def process_registration(self, stackedWidget, dialog, id, password, confirm_password, name, age):
        print(1)
        self.stackedWidget=stackedWidget
        Account().process_registration(self.stackedWidget, dialog, id, password, confirm_password, name, age)











