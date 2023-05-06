import sys 
sys.path.append('./Boundary')
from manageAcc import manageAcc


class accManage:
    def fuc(self,stackedWidget):
        self.stackedWidget = stackedWidget
        self.stackedWidget.setCurrentIndex(3)
