import sys 
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QStackedWidget, QGridLayout
sys.path.append('./Boundary')
#from createAccUI import createAccUI

#SQL STATEMENTS TO CREATE profile TO BE HERE

class profCreate:
    def fuc(self,stackedWidget, profilename, systemR):
        self.stackedWidget = stackedWidget
        print("in profAcc")
        print(profilename, systemR)
