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



class delTicTypeController:
    def delTicTypeC(self, stackedWidget, ticList):
        self.stackedWidget = stackedWidget
        self.ticList = ticList
        items = [item.text() for item in self.ticList.selectedItems()]
        try:
            if not items:
                raise ValueError("Please select a hall.")
            else:
                ticketType().delTicType(self.stackedWidget, self.ticList)
        except ValueError as e:
            QMessageBox.warning(self.stackedWidget, 'Error', str(e))
        


class editTicTypeController:
    def editTicTypeC(self,dialog, stackedwidget, oldname,oldprice, newname, newprice):
        try:
            if newname and newprice:
                ticketType().editTicType(dialog, stackedwidget, oldname,oldprice, newname, newprice)
            else:
                raise ValueError("New columns are empty")
        except ValueError as e:
            QMessageBox.warning(self, 'Error', str(e))


class listTicTypeController:
    def listTicTypeC(self, stackedWidget,list):
        self.stackedWidget = stackedWidget
        ticketType().listTicType(self.stackedWidget, list)

