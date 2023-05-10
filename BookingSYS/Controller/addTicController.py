import sys 
sys.path.append( './Entity' )
from PyQt5.QtWidgets import QMessageBox
#sys.path.append('C:/Users/USER/Desktop/BookingSys/bookingSys/BookingSYS/Entity')
from manage import Manage

class addTicController:
    def addTicC(self, stackedWidget, name , price):
        self.stackedWidget = stackedWidget
        try:
            if price.isnumeric():
                Manage().addTicket(self.stackedWidget, name ,price)
            else:
                raise ValueError("Price is not numerical")
        except ValueError as e:
            QMessageBox.warning(self, 'Error', str(e))