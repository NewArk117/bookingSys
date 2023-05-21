import sys 
sys.path.append( './Entity' )
from PyQt5.QtWidgets import QMessageBox
#sys.path.append('C:/Users/USER/Desktop/BookingSys/bookingSys/BookingSYS/Entity')
from fnb import FnB
#13. Cinema Manager Controller
class addFBController:
    def addFBC(self, stackedWidget, name , price, quantity):
        self.stackedWidget = stackedWidget
        if price.isnumeric() and quantity.isnumeric():
            #13. Cinema Manager Entity
            FnB().addFB(self.stackedWidget, name ,price, quantity)
            
#16. Cinema Controller
class susFBController:
    def susFBC(self, stackedWidget, fbList):
        self.stackedWidget = stackedWidget
        self.fbList = fbList
        items = self.fbList.currentItem()
        if items:
            FnB().susFB(self.stackedWidget, self.fbList)
    
        
#15. Cinema Manager Controller
class editFBController:
    def editFBC(self,dialog, stackedwidget, fbList, newname, newprice, newquant,avail2):
        self.fbList = fbList
        items = self.fbList.currentItem()
        if items:
            name = items.text()[:20].strip()
            fb1 = FnB()
            itemname,price,quantity,avail = fb1.getData(name)
            print(itemname,price,quantity,avail)
            #15. Cinema Manager Entity
            FnB().editFB(dialog, stackedwidget, itemname,price,quantity, avail ,newname, newprice,newquant, avail2)
            

#14. Cinema Manager Controller
class listFBController:
    def listFBC(self, stackedWidget,list):
        self.stackedWidget = stackedWidget
        #14. Cinema Manager Entity
        FnB().listManagerFB(self.stackedWidget, list)


class searchFBController:
    def searchFBC(self, stackedWidget, item_name, list):
        self.stackedWidget = stackedWidget
        FnB().searchFB(self.stackedWidget,item_name, list)    


class PurchaseFoodController:
    def __init__(self):
        self.food_model = FnB()

    def get_food_data(self):
        return self.food_model.get_food_data()

    def save_food_order(self, user_id, ticket_id, order_list):
        self.food_model.save_food_order(user_id, ticket_id, order_list)

    def close_connection(self):
        self.food_model.close_connection()


class viewFBController:
    def viewFBC(self, stackedWidget, fbList):
        self.stackedWidget = stackedWidget
        self.fbList = fbList
        selected_item = self.fbList.currentItem()
        # If an item is selected, display its name
        if selected_item is not None:
            item_name = selected_item.text()
            text, itemname = FnB().viewFB(self.stackedWidget,item_name)
            return text, itemname
        else:
            text=None
            itemname = None
            return text, itemname