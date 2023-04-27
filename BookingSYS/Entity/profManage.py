import sys 
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QStackedWidget, QGridLayout
sys.path.append('./Boundary')

class profManage:
    def fuc(self,stackedWidget):
        self.stackedWidget = stackedWidget
        print("in manageProf")
        self.stackedWidget.setCurrentIndex(4)