import sys 
sys.path.append( './Entity' )
from PyQt5.QtWidgets import QMessageBox
#sys.path.append('C:/Users/USER/Desktop/BookingSys/bookingSys/BookingSYS/Entity')
from fnb import FnB
#13. Cinema Manager Controller
class addFBController:
    def addFBC(self, stackedWidget, name , price, quantity):
        self.stackedWidget = stackedWidget
        try:
            if price.isnumeric() and quantity.isnumeric():
                #13. Cinema Manager Entity
                FnB().addFB(self.stackedWidget, name ,price, quantity)
            else:
                raise ValueError("Price/Quantity is not numerical")
        except ValueError as e:
            QMessageBox.warning(self, 'Error', str(e))

#16. Cinema Controller
class delFBController:
    def delFBC(self, stackedWidget, fbList):
        self.stackedWidget = stackedWidget
        self.fbList = fbList
        items = [item.text() for item in self.fbList.selectedItems()]
        try:
            if not items:
                raise ValueError("Please select an item.")
            else:
                #16. Cinema Manager Entity
                FnB().delFB(self.stackedWidget, self.fbList)
        except ValueError as e:
            QMessageBox.warning(self.stackedWidget, 'Error', str(e))
        
#15. Cinema Manager Controller
class editFBController:
    def editFBC(self,dialog, stackedwidget, oldname,oldprice,oldquant, newname, newprice, newquant):
        try:
            if newname and newprice:
                #15. Cinema Manager Entity
                FnB().editFB(dialog, stackedwidget, oldname,oldprice, newname, newprice)
            else:
                raise ValueError("New columns are empty")
        except ValueError as e:
            QMessageBox.warning(self, 'Error', str(e))

#14. Cinema Manager Controller
class listFBController:
    def listFBC(self, stackedWidget,list):
        self.stackedWidget = stackedWidget
        #14. Cinema Manager Entity
        FnB().listManagerFB(self.stackedWidget, list)
