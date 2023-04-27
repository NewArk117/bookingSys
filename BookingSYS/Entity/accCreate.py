import sys 
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QStackedWidget, QGridLayout
sys.path.append('./Boundary')
#from createAccUI import createAccUI

#SQL STATEMENTS TO CREATE ACCOUNT TO BE HERE

class accCreate:
    def fuc(self,stackedWidget, fname, lname, age, username, password, accType):
        self.stackedWidget = stackedWidget
        print("in createAcc")
        print(fname, lname, age,username, password, accType)
