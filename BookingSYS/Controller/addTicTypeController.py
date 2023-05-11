import sys 
sys.path.append( './Entity' )
from PyQt5.QtWidgets import QMessageBox
#sys.path.append('C:/Users/USER/Desktop/BookingSys/bookingSys/BookingSYS/Entity')
from ticketType import ticketType

class addTicTypeController:
    def addTicTypeC(self, stackedWidget, name , price):
        self.stackedWidget = stackedWidget
        try:
            if price.isnumeric():
                ticketType().addTicType(self.stackedWidget, name ,price)
            else:
                raise ValueError("Price is not numerical")
        except ValueError as e:
            QMessageBox.warning(self, 'Error', str(e))