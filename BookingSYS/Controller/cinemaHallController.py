import sys 
sys.path.append( './Entity' )
from PyQt5.QtWidgets import QMessageBox
#sys.path.append('C:/Users/USER/Desktop/BookingSys/bookingSys/BookingSYS/Entity')
from cinemaHall import cinemaHall

#3. Cinema Manager Controller
class addHallController:
    def addHallC(self, stackedWidget, name , rows, columns):
        self.stackedWidget = stackedWidget
        if rows.isnumeric() and columns.isnumeric():
            if 0 < int(rows) < 9:
                if 0 < int(columns) < 9: 
                    #3. Cinema Manager Entity (go to cinemahall.py)
                    cinemaHall().addHall(self.stackedWidget, name ,rows, columns)
            

#6. Cinema Manager Controller
class susHallsController:
    def susHallsC(self, stackedWidget, hallList):
        self.stackedWidget = stackedWidget
        self.hallList = hallList
        items = self.hallList.currentItem()
        if items:
            #6. Cinema Manager Entity no return
            cinemaHall().susHall(self.stackedWidget, self.hallList)


class editHallController:
    def editHallC(self, stackedwidget,dialog ,hallList, name2, avail2):
        self.hallList = hallList
        try:
            items = self.hallList.currentItem()
            if items:
                name = items.text().split()[0]
                hall1 = cinemaHall()
                hallname,rows,columns,avail = hall1.getData(name)
                print(hallname, rows, columns, avail)
                #5. Cinema Manager Entity got return (cinemahall.py)
                cinemaHall().editHall(stackedwidget, dialog ,hallname , avail, name2, avail2)
        except:
            dialog.reject()

    
#4. Cinema Manager Controller
class listHallController:
    def listHallC(self, stackedWidget,list):
        self.stackedWidget = stackedWidget
        #4. Cinema Manager Entity (cinemahall.py) no return
        cinemaHall().listManagerHall(self.stackedWidget, list)

class searchHallController:
    def searchHallC(self, stackedWidget, item_name, list)->list:
        self.stackedWidget = stackedWidget
        list = cinemaHall().searchHall(self.stackedWidget,item_name, list) 
        return list
class viewHallController:
    def viewHallC(self, stackedWidget, hallList):
        self.stackedWidget = stackedWidget
        self.hallList = hallList
        selected_item = self.hallList.currentItem()
        # If an item is selected, display its name
        if selected_item is not None:
            item_name = selected_item.text()
            text, hallname = cinemaHall().viewHall(self.stackedWidget,item_name)
            return text, hallname
        else:
            text=None
            hallname = None
            return text, hallname

