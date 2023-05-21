import sys 
sys.path.append( './Entity' )
from PyQt5.QtWidgets import QMessageBox
#sys.path.append('C:/Users/USER/Desktop/BookingSys/bookingSys/BookingSYS/Entity')
from ticketType import ticketType

#18. Cinema Manager Controller
class addTicTypeController:
    def addTicTypeC(self, stackedWidget, name , price):
        self.stackedWidget = stackedWidget
        if price.isnumeric():
            #18. Cinema Manager Entity
            ticketType().addTicType(self.stackedWidget, name ,price)
        


#21. Cinema Manager Controller
class susTicTypeController:
    def susTicTypeC(self, stackedWidget, ticList):
        self.stackedWidget = stackedWidget
        self.ticList = ticList  
        items = self.ticList.currentItem()
        if items:
            #21. Cinema Manager Entity
            ticketType().susTicType(self.stackedWidget, self.ticList)
        

#20. Cinema Manager Controller
class editTicTypeController:
    def editTicTypeC(self,dialog, stackedwidget, ticketList, newname, newprice,avail2):
        self.ticketList = ticketList
        items = self.ticketList.currentItem()
        if items:
            name = items.text().split()[0].strip()
            ticType = ticketType()
            typename, price, avail = ticType.getData(name)
            #print(typename, newprice, avail)
            #20. Cinema Manager Entity
            ticketType().editTicType(dialog, stackedwidget, typename, price,avail , newname, newprice,avail2)
            
#19. Cinema Manager Controller
class listTicTypeController:
    def listTicTypeC(self, stackedWidget,list):
        self.stackedWidget = stackedWidget
        #19. Cinema Manager Entity (ticketType.py)
        ticketType().listTicType(self.stackedWidget, list)

class searchTicTypeController:
    def searchTicTypeC(self, stackedWidget, item_name, list):
        self.stackedWidget = stackedWidget
        ticketType().searchTicType(self.stackedWidget,item_name, list) 


class viewTicTypeController:
    def viewTicTypeC(self, stackedWidget, ticketList):
        self.stackedWidget = stackedWidget
        self.ticketList = ticketList
        selected_item = self.ticketList.currentItem()
        # If an item is selected, display its name
        if selected_item is not None:
            item_name = selected_item.text()
            text, type = ticketType().viewTicType(self.stackedWidget,item_name)

            return text, type

        else:
            text=None
            type = None
            return text, type