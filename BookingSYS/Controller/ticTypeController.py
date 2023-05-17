import sys 
sys.path.append( './Entity' )
from PyQt5.QtWidgets import QMessageBox
#sys.path.append('C:/Users/USER/Desktop/BookingSys/bookingSys/BookingSYS/Entity')
from ticketType import ticketType

#18. Cinema Manager Controller
class addTicTypeController:
    def addTicTypeC(self, stackedWidget, name , price):
        self.stackedWidget = stackedWidget
        try:
            if price.isnumeric():
                #18. Cinema Manager Entity
                ticketType().addTicType(self.stackedWidget, name ,price)
            else:
                raise ValueError("Price is not numerical")
        except ValueError as e:
            QMessageBox.warning(self, 'Error', str(e))


#21. Cinema Manager Controller
class delTicTypeController:
    def delTicTypeC(self, stackedWidget, ticList):
        self.stackedWidget = stackedWidget
        self.ticList = ticList
        items = [item.text() for item in self.ticList.selectedItems()]
        try:
            if not items:
                raise ValueError("Please select a hall.")
            else:
                #21. Cinema Manager Entity
                ticketType().delTicType(self.stackedWidget, self.ticList)
        except ValueError as e:
            QMessageBox.warning(self.stackedWidget, 'Error', str(e))
        

#20. Cinema Manager Controller
class editTicTypeController:
    def editTicTypeC(self,dialog, stackedwidget, oldname,oldprice, newname, newprice):
        try:
            if newname and newprice:
                #20. Cinema Manager Entity
                ticketType().editTicType(dialog, stackedwidget, oldname,oldprice, newname, newprice)
            else:
                raise ValueError("New columns are empty")
        except ValueError as e:
            QMessageBox.warning(self, 'Error', str(e))

#19. Cinema Manager Controller
class listTicTypeController:
    def listTicTypeC(self, stackedWidget,list):
        self.stackedWidget = stackedWidget
        #19. Cinema Manager Entity (ticketType.py)
        ticketType().listTicType(self.stackedWidget, list)

