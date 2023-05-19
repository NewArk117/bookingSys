import sys 
sys.path.append( './Entity' )
from PyQt5.QtWidgets import QMessageBox
#sys.path.append('C:/Users/USER/Desktop/BookingSys/bookingSys/BookingSYS/Entity')
from fnb import FnB

class addFBController:
    def addFBC(self, stackedWidget, name , price, quantity):
        self.stackedWidget = stackedWidget
        try:
            if price.isnumeric() and quantity.isnumeric():
                FnB().addFB(self.stackedWidget, name ,price, quantity)
            else:
                raise ValueError("Price/Quantity is not numerical")
        except ValueError as e:
            QMessageBox.warning(self, 'Error', str(e))

class delFBController:
    def delFBC(self, stackedWidget, fbList):
        self.stackedWidget = stackedWidget
        self.fbList = fbList
        items = [item.text() for item in self.fbList.selectedItems()]
        try:
            if not items:
                raise ValueError("Please select an item.")
            else:
                FnB().delFB(self.stackedWidget, self.fbList)
        except ValueError as e:
            QMessageBox.warning(self.stackedWidget, 'Error', str(e))
        

class editFBController:
    def editFBC(self,dialog, stackedwidget, oldname,oldprice,oldquant, newname, newprice, newquant):
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


class PurchaseFoodController:
    def __init__(self):
        self.food_model = FnB()

    def get_food_data(self):
        return self.food_model.get_food_data()

    def save_food_order(self, user_id, ticket_id, order_list):
        self.food_model.save_food_order(user_id, ticket_id, order_list)

    def close_connection(self):
        self.food_model.close_connection()


