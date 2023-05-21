import sys
sys.path.append( './Entity' )
from account import Account
class userRegController:
    def process_registration(self, stackedWidget, dialog, id, username, password, confirm_password):
        print(1)
        self.stackedWidget=stackedWidget
        Account().process_registration(self.stackedWidget, dialog, id, username, password, confirm_password)








