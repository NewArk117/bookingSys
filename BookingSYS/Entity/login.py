import sys 
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QStackedWidget, QGridLayout

sys.path.append('./Boundary')
from adminUI import adminUI
class login:
    def fuc(self,stackedWidget,usrname, pw):
        self.stackedWidget = stackedWidget
        self.usrname = usrname
        self.pw = pw
        print("in login entity")
        #check what user is logging in
        if self.usrname == 'admin':
            if self.pw == 'password':
                self.stackedWidget.setCurrentIndex(2)
            else:
                print("Wrong password")
        #do if else to check with usrname and pw with database, if match then go to customer UI
        else:
            print('Invalid username')



        
        
