import sys 
sys.path.append( './Entity' )
from PyQt5.QtWidgets import QMessageBox
#sys.path.append('C:/Users/USER/Desktop/BookingSys/bookingSys/BookingSYS/Entity')
from fnb import FnB

class addFBController:
    def addFBC(self, stackedWidget, name , price):
        self.stackedWidget = stackedWidget
        try:
            if price.isnumeric():
                FnB().addFB(self.stackedWidget, name ,price)
            else:
                raise ValueError("Price is not numerical")
        except ValueError as e:
            QMessageBox.warning(self, 'Error', str(e))

class delFBController:
    def delFBC(self, stackedWidget, fbList):
        self.stackedWidget = stackedWidget
        self.fbList = fbList
        items = [item.text() for item in self.fbList.selectedItems()]
        try:
            if not items:
                raise ValueError("Please select a hall.")
            else:
                FnB().delFB(self.stackedWidget, self.fbList)
        except ValueError as e:
            QMessageBox.warning(self.stackedWidget, 'Error', str(e))
        

class editFBController:
    def editFBC(self,dialog, stackedwidget, oldname,oldprice, newname, newprice):
        try:
            if newname and newprice:
                FnB().editFB(dialog, stackedwidget, oldname,oldprice, newname, newprice)
            else:
                raise ValueError("New columns are empty")
        except ValueError as e:
            QMessageBox.warning(self, 'Error', str(e))

class listFBController:
    def listFBC(self, stackedWidget,list):
        self.stackedWidget = stackedWidget
        FnB().listManagerFB(self.stackedWidget, list)