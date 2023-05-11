#GUI imports
from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton,QGridLayout, QListWidget, QAbstractItemView, QDialog, QMessageBox, QVBoxLayout
from PyQt5 import QtGui
from PyQt5.QtCore import QStringListModel, Qt, QTimer
import sqlite3
#Import links to different scripts in Controller
import sys 
sys.path.append('./Controller')
from delMoviesController import delMoviesController
from delTicTypeController import delTicTypeController
from delHallsController import delHallsController
from delFBController import delFBController

from addTicTypeController import addTicTypeController
from addFBController import addFBController
from addHallController import addHallController

from listTicTypeController import listTicTypeController
from listFBController import listFBController
from listHallController import listHallController

from editTicTypeController import editTicTypeController
from editFBController import editFBController
from editHallController import editHallController

#Create new account GUI
class managerUI(QWidget):
    def __init__(self, stackedWidget):
        super().__init__()

        self.stackedWidget = stackedWidget
        
        self.setWindowTitle('Manager')
        font = QtGui.QFont()
        font.setPointSize(20)

        # layout for manage Accounts -----------------------------------
        layout = QGridLayout()

        self.label1 = QLabel("Manage")
        self.label1.setFixedSize(150,70)
        self.label1.adjustSize()
        self.label1.setFont(font)

        self.label2 =QLabel()
        self.label2.setFixedSize(150,60)
        self.label2.adjustSize()
        
        self.moviesButton = QPushButton("Movies")
        self.moviesButton.setFixedSize(150,50)
        self.ticketsButton = QPushButton("Tickets")
        self.ticketsButton.setFixedSize(150,50)
        self.hallButton = QPushButton("Hall")
        self.hallButton.setFixedSize(150,50)
        self.fbButton = QPushButton("F&&B")
        self.fbButton.setFixedSize(150,50)
        self.logoutButton = QPushButton("Logout")
        self.logoutButton.setFixedSize(150,30)

        layout.addWidget(self.label1, 0, 2)
        layout.addWidget(self.moviesButton, 1,1)
        layout.addWidget(self.ticketsButton, 1,3)
        #layout.addWidget(self.label2, 0,2)
        layout.addWidget(self.hallButton, 3,1)
        layout.addWidget(self.fbButton, 3, 3)
        layout.addWidget(self.logoutButton, 7, 3)

        self.moviesButton.clicked.connect(self.goMovie)
        self.hallButton.clicked.connect(self.goHalls)
        self.fbButton.clicked.connect(self.goFB)
        self.ticketsButton.clicked.connect(self.goTicket)

        self.setLayout(layout)

    def goMovie(self):
        self.stackedWidget.setCurrentIndex(10)
    
    def goHalls(self):
        self.stackedWidget.setCurrentIndex(11)

    def goFB(self):
        self.stackedWidget.setCurrentIndex(12)
    
    def goTicket(self):
        self.stackedWidget.setCurrentIndex(13)

#Create ticket GUi
class manageTicTypeUI(QWidget):
    def __init__(self, stackedWidget):
        super().__init__()

        self.stackedWidget = stackedWidget
        
        self.setWindowTitle('Manage Ticket Type')
        
        font = QtGui.QFont()
        font.setPointSize(20)

        # layout for manage Accounts -----------------------------------
        layout = QGridLayout()
        
        self.label1 = QLabel("Manage Ticket Type")
        ticket_string = '{:<20}\t{:<30}'.format("Ticket type", "Price")
        #self.label2 = QLabel(ticket_string)
        self.ticketList = QListWidget()
        self.listTics()
        self.ticketList.setSelectionMode(QAbstractItemView.SingleSelection)
        self.addButton = QPushButton("Add")
        self.delButton = QPushButton("Delete")
        self.editButton = QPushButton("Edit")
        self.backButton = QPushButton("Back")
        
        layout.addWidget(self.label1, 0, 0)
        #layout.addWidget(self.label2, 1, 0)
        layout.addWidget(self.ticketList, 1, 0, 4, 1)
        layout.addWidget(self.addButton, 1, 1)
        layout.addWidget(self.delButton, 1, 2)
        layout.addWidget(self.editButton, 2, 1)
        layout.addWidget(self.backButton, 7, 2)

        self.backButton.clicked.connect(self.goBack)
        self.addButton.clicked.connect(self.addTic)
        self.delButton.clicked.connect(self.delTics)
        self.editButton.clicked.connect(self.editTics)

        #self.timer = QTimer()
        #self.timer.setInterval(1000)
        #self.timer.timeout.connect(self.listTics)
        #self.timer.start()

        self.setLayout(layout)
        self.stackedWidget.currentChanged.connect(self.listTics)
        

    def goBack(self):
        self.stackedWidget.setCurrentIndex(9)

    def addTic(self):
        self.stackedWidget.setCurrentIndex(15)
        self.listTics()

    def delTics(self):
        delTicTypeController.delTicTypeC(self, self.stackedWidget, self.ticketList)
        self.listTics()

    def editTics1(self, dialog, name, price, name2, price2 ):
        editTicTypeController.editTicTypeC(self, dialog, self.stackedWidget, name, price, name2, price2 )
        self.listTics()

    def listTics(self):
        listTicTypeController.listTicTypeC(self, self.stackedWidget, self.ticketList )
    
    def editTics(self):
        self.dialog = QDialog(self)
        self.dialog.setWindowTitle("My Dialog")

        font = QtGui.QFont()
        font.setPointSize(20)

        #self.getOldTicket()
        try:
            items = self.ticketList.currentItem()
            if items:
                name = items.text().split()[0]
                price = items.text().split()[1]

                layout = QGridLayout(self.dialog)
                self.name1_label = QLabel('Old Name:')
                self.name1_edit = QLabel(name)
            

                self.price1_label = QLabel('Old Price:')
                self.price1_edit = QLabel(price)


                self.name2_label = QLabel('New Name:')
                self.name2_edit = QLineEdit()
                #self.name2_edit.setPlaceholderText(self.oldname)
                

                self.price2_label = QLabel('New Price:')
                self.price2_edit = QLineEdit()
                #self.price2_edit.setPlaceholderText(self.oldprice)
                
                self.backButton = QPushButton("Back")
                self.submitButton = QPushButton("Submit")

                layout.addWidget(self.name1_label,0,0)
                layout.addWidget(self.name1_edit,0,1)
                layout.addWidget(self.price1_label, 1, 0)
                layout.addWidget(self.price1_edit, 1, 1)

                layout.addWidget(self.name2_label,2,0)
                layout.addWidget(self.name2_edit,2,1)
                layout.addWidget(self.price2_label, 3, 0)
                layout.addWidget(self.price2_edit, 3, 1)

                layout.addWidget(self.backButton,5, 0 )
                layout.addWidget(self.submitButton,5 ,2)

                self.backButton.clicked.connect(self.dialog.reject)
                self.submitButton.clicked.connect(lambda: (self.editTics1(self.dialog, name, price,self.name2_edit.text(), self.price2_edit.text() )))

                self.dialog.exec_()
            else:
                raise ValueError("No type selected")
        except ValueError as e:
            QMessageBox.warning(self.stackedWidget, 'Error', str(e))

#Create movies GUI
class manageMoviesUI(QWidget):
    def __init__(self, stackedWidget):
        super().__init__()

        self.stackedWidget = stackedWidget
        
        self.setWindowTitle('Manage Movies')
        
        font = QtGui.QFont()
        font.setPointSize(20)

        # layout for manage Accounts -----------------------------------
        layout = QGridLayout()

        self.label1 = QLabel("Manage Movies")
        self.moviesList = QListWidget()
        self.addButton = QPushButton("Add")
        self.delButton = QPushButton("Delete")
        self.editButton = QPushButton("Edit")
        self.backButton = QPushButton("Back")
        
        layout.addWidget(self.label1, 0, 0)
        layout.addWidget(self.moviesList, 1, 0, 4, 1)
        layout.addWidget(self.addButton, 1 , 1)
        layout.addWidget(self.delButton, 1, 2)
        layout.addWidget(self.editButton, 2, 1)
        layout.addWidget(self.backButton, 7, 2)

        self.backButton.clicked.connect(self.goBack)
        self.addButton.clicked.connect(self.addMov)
        self.delButton.clicked.connect(self.deleteMovie)

        self.setLayout(layout)

    def goBack(self):
        self.stackedWidget.setCurrentIndex(9)

    def addMov(self):
        self.stackedWidget.setCurrentIndex(14)

    def deleteMovie(self):
        delMoviesController.delMoviesC(self,self.stackedWidget, self.moviesList)

    
#Create hall GUI
class manageHallsUI(QWidget):
    def __init__(self, stackedWidget):
        super().__init__()

        self.stackedWidget = stackedWidget
        
        self.setWindowTitle('Manage Hall')
        
        font = QtGui.QFont()
        font.setPointSize(20)

        # layout for manage Accounts -----------------------------------
        layout = QGridLayout()

        self.label1 = QLabel("Manage Halls")
        self.hallList = QListWidget()
        self.listHalls()
        self.addButton = QPushButton("Add")
        self.delButton = QPushButton("Suspend")
        self.editButton = QPushButton("Edit")
        self.backButton = QPushButton("Back")
        
        layout.addWidget(self.label1, 0, 0)
        layout.addWidget(self.hallList, 1, 0, 4, 1)
        layout.addWidget(self.addButton, 1 , 1)
        layout.addWidget(self.delButton, 1, 2)
        layout.addWidget(self.editButton, 2, 1)
        layout.addWidget(self.backButton, 7, 2)

        self.backButton.clicked.connect(self.goBack)
        self.addButton.clicked.connect(self.addHall)
        self.delButton.clicked.connect(self.delHall)
        self.editButton.clicked.connect(self.editHallUI)

        self.setLayout(layout)
        self.stackedWidget.currentChanged.connect(self.listHalls)
    def goBack(self):
        self.stackedWidget.setCurrentIndex(9)

    def addHall(self):
        self.stackedWidget.setCurrentIndex(17)

    def delHall(self):
        delHallsController.delHallsC(self, self.stackedWidget, self.hallList)
    
    def listHalls(self):
        listHallController.listHallC(self, self.stackedWidget, self.hallList )

    def editHall(self,  dialog ,name , row, column, avail, name2, rows2, columns2, avail2):
        x = editHallController.editHallC(self,self.stackedWidget, dialog ,name , row, column, avail, name2, rows2, columns2, avail2)
        if x:
            self.listHalls()
        #print(name2)
        #print(rows2)
        #print(columns2)
        #print(avail2)
    def editHallUI(self):
        self.dialog = QDialog(self)
        self.dialog.setWindowTitle("Edit Hall")

        font = QtGui.QFont()
        font.setPointSize(20)

        layout = QGridLayout(self.dialog)
        #self.getOldTicket()
        try:
            items = self.hallList.currentItem()
            if items:
                name = items.text().split()[0]
                rows = items.text().split()[1]
                columns = items.text().split()[2]
                capacity = items.text().split()[3]
                avail = items.text().split()[4]

                self.name_label = QLabel('Hall Name:')
                self.name_edit = QLineEdit()
                self.name_edit.setPlaceholderText(name)

                self.rows_label = QLabel('Number of rows:')
                self.rows_edit = QLineEdit()
                self.rows_edit.setPlaceholderText(rows)

                self.column_label = QLabel('Number of columns:')
                self.column_edit = QLineEdit()
                self.column_edit.setPlaceholderText(columns)

                self.avail_label = QLabel('Availability:')
                self.avail_edit = QLineEdit()
                self.avail_edit.setPlaceholderText(avail)

                #print (name + rows + columns + capacity + availString)

                self.backButton = QPushButton("Back")
                self.submitButton = QPushButton("Submit")

                layout.addWidget(self.name_label,0,0)
                layout.addWidget(self.name_edit,0,1)

                layout.addWidget(self.rows_label, 1, 0)
                layout.addWidget(self.rows_edit, 1, 1)

                layout.addWidget(self.column_label,2,0)
                layout.addWidget(self.column_edit,2,1)

                layout.addWidget(self.avail_label, 3, 0)
                layout.addWidget(self.avail_edit, 3, 1)


                layout.addWidget(self.backButton,5, 0 )
                layout.addWidget(self.submitButton,5 ,2)
                
                self.backButton.clicked.connect(self.dialog.reject)
                self.submitButton.clicked.connect(lambda: (self.editHall(self.dialog, name, rows, columns , avail ,self.name_edit.text(), self.rows_edit.text(),self.column_edit.text(), self.avail_edit.text())))

                self.dialog.exec_()
            else:
                raise ValueError("No hall selected")
        except ValueError as e:
            QMessageBox.warning(self.stackedWidget, 'Error', str(e))


class manageFBUI(QWidget):
    def __init__(self, stackedWidget):
        super().__init__()

        self.stackedWidget = stackedWidget
        
        self.setWindowTitle('Manage F&B')
        
        font = QtGui.QFont()
        font.setPointSize(20)

        # layout for manage Accounts -----------------------------------
        layout = QGridLayout()

        self.label1 = QLabel("Manage F&B")
        self.fbList = QListWidget()
        self.listFB()
        self.addButton = QPushButton("Add")
        self.delButton = QPushButton("Delete")
        self.editButton = QPushButton("Edit")
        self.backButton = QPushButton("Back")
        
        layout.addWidget(self.label1, 0, 0)
        layout.addWidget(self.fbList, 1, 0, 4, 1)
        layout.addWidget(self.addButton, 1 , 1)
        layout.addWidget(self.delButton, 1, 2)
        layout.addWidget(self.editButton, 2, 1)
        layout.addWidget(self.backButton, 7, 2)

        self.backButton.clicked.connect(self.goBack)
        self.addButton.clicked.connect(self.addFB)
        self.delButton.clicked.connect(self.delFB)
        self.editButton.clicked.connect(self.editFB)

        self.setLayout(layout)
        self.stackedWidget.currentChanged.connect(self.listFB)
    def goBack(self):
        self.stackedWidget.setCurrentIndex(9)

    def addFB(self):
        self.stackedWidget.setCurrentIndex(16)
        self.listFB()

    def delFB(self):
        delFBController.delFBC(self, self.stackedWidget, self.fbList)
        self.listFB()

    def listFB(self):
        listFBController.listFBC(self, self.stackedWidget, self.fbList)

    def editFB1(self, dialog, name, price, name2, price2 ):
        editFBController.editFBC(self, dialog, self.stackedWidget, name, price, name2, price2 )
        self.listFB()


    def editFB(self):
        self.dialog = QDialog(self)
        self.dialog.setWindowTitle("Edit F&B")

        font = QtGui.QFont()
        font.setPointSize(20)

        #self.getOldTicket()
        try:
            items = self.fbList.currentItem()
            if items:
                name = items.text().split()[0]
                price = items.text().split()[1]

                layout = QGridLayout(self.dialog)
                self.name1_label = QLabel('Old Item:')
                self.name1_edit = QLabel(name)
            

                self.price1_label = QLabel('Old Price:')
                self.price1_edit = QLabel(price)


                self.name2_label = QLabel('New Name:')
                self.name2_edit = QLineEdit()
                #self.name2_edit.setPlaceholderText(self.oldname)
                

                self.price2_label = QLabel('New Price:')
                self.price2_edit = QLineEdit()
                #self.price2_edit.setPlaceholderText(self.oldprice)
                
                self.backButton = QPushButton("Back")
                self.submitButton = QPushButton("Submit")

                layout.addWidget(self.name1_label,0,0)
                layout.addWidget(self.name1_edit,0,1)
                layout.addWidget(self.price1_label, 1, 0)
                layout.addWidget(self.price1_edit, 1, 1)

                layout.addWidget(self.name2_label,2,0)
                layout.addWidget(self.name2_edit,2,1)
                layout.addWidget(self.price2_label, 3, 0)
                layout.addWidget(self.price2_edit, 3, 1)

                layout.addWidget(self.backButton,5, 0 )
                layout.addWidget(self.submitButton,5 ,2)

                self.backButton.clicked.connect(self.dialog.reject)
                self.submitButton.clicked.connect(lambda: (self.editFB1(self.dialog, name, price,self.name2_edit.text(), self.price2_edit.text() )))

                self.dialog.exec_()
            else:
                raise ValueError("No item selected")
        except ValueError as e:
            QMessageBox.warning(self.stackedWidget, 'Error', str(e))


#UI for create========================================
class addMovies(QWidget):
    def __init__(self, stackedWidget):
        super().__init__()

        self.stackedWidget = stackedWidget
        
        self.setWindowTitle('Add Movies')
        
        font = QtGui.QFont()
        font.setPointSize(20)

        layout = QGridLayout()

        self.name_label = QLabel('Name:')
        self.name_edit = QLineEdit()

        self.userID_label = QLabel('Account ID:')
        self.userID_edit = QLineEdit()

        self.startDate_label = QLabel('Start Date(DD/MM/YYYY):')
        self.startDate_edit = QLineEdit()

        self.endDate_label = QLabel('End Date(DD/MM/YYYY):')
        self.endDate_edit = QLineEdit()

        self.showtime_label = QLabel('Showtimes')
        self.showtime_list = QListWidget()

        self.backButton = QPushButton("Back")
        self.submitButton = QPushButton("Submit")

        layout.addWidget(self.name_label,0,0)
        layout.addWidget(self.name_edit,0,1)
        layout.addWidget(self.userID_label, 1, 0)
        layout.addWidget(self.userID_edit, 1, 1)
        layout.addWidget(self.startDate_label, 2, 0)
        layout.addWidget(self.startDate_edit, 2, 1)
        layout.addWidget(self.endDate_label, 3, 0)
        layout.addWidget(self.endDate_edit, 3, 1)
        layout.addWidget(self.showtime_label, 4,0)
        layout.addWidget(self.showtime_list, 5,0, 3,1)
        layout.addWidget(self.backButton,9, 0 )
        layout.addWidget(self.submitButton,9 ,2)

        self.backButton.clicked.connect(self.goBack)

        # layout for manage Accounts -----------------------------------
        self.setLayout(layout)

    def goBack(self):
        self.stackedWidget.setCurrentIndex(10)

class addHalls(QWidget):
    def __init__(self, stackedWidget):
        super().__init__()

        self.stackedWidget = stackedWidget
        
        self.setWindowTitle('Add Hall')
        
        font = QtGui.QFont()
        font.setPointSize(20)

        layout = QGridLayout()

        self.name_label = QLabel('Hall Name:')
        self.name_edit = QLineEdit()

        self.rows_label = QLabel('Number of rows:')
        self.rows_edit = QLineEdit()

        self.column_label = QLabel('Number of columns:')
        self.column_edit = QLineEdit()


        self.backButton = QPushButton("Back")
        self.submitButton = QPushButton("Submit")

        layout.addWidget(self.name_label,0,0)
        layout.addWidget(self.name_edit,0,1)
        layout.addWidget(self.rows_label,2,0)
        layout.addWidget(self.rows_edit,2,1)
        layout.addWidget(self.column_label, 3, 0)
        layout.addWidget(self.column_edit, 3, 1)

        layout.addWidget(self.backButton,7, 0 )
        layout.addWidget(self.submitButton,7 ,2)

        self.backButton.clicked.connect(self.goBack)
        self.submitButton.clicked.connect(self.addHall)

        self.setLayout(layout)

    def goBack(self):
        self.stackedWidget.setCurrentIndex(11)

    def addHall(self):
        name = self.name_edit.text()
        rows = self.rows_edit.text()
        column = self.column_edit.text()
        
        addHallController.addHallC(self, self.stackedWidget, name, rows, column)

class addFnB(QWidget):
    def __init__(self, stackedWidget):
        super().__init__()

        self.stackedWidget = stackedWidget
        
        self.setWindowTitle('Add F&B')
        
        font = QtGui.QFont()
        font.setPointSize(20)

        layout = QGridLayout()

        self.name_label = QLabel('F&B Name:')
        self.name_edit = QLineEdit()

        self.price_label = QLabel('Item Price:')
        self.price_edit = QLineEdit()

        self.backButton = QPushButton("Back")
        self.submitButton = QPushButton("Submit")

        layout.addWidget(self.name_label,0,0)
        layout.addWidget(self.name_edit,0,1)
        layout.addWidget(self.price_label, 1, 0)
        layout.addWidget(self.price_edit, 1, 1)

        layout.addWidget(self.backButton,7, 0 )
        layout.addWidget(self.submitButton,7 ,2)

        self.backButton.clicked.connect(self.goBack)
        self.submitButton.clicked.connect(self.addFB)

        self.setLayout(layout)

    def goBack(self):
        self.stackedWidget.setCurrentIndex(12)
    
    def addFB(self):
        name = self.name_edit.text()
        price = self.price_edit.text()
        addFBController.addFBC(self, self.stackedWidget, name ,price)

        self.name_edit.clear()
        self.price_edit.clear()


class addTic(QWidget):
    def __init__(self, stackedWidget):
        super().__init__()

        self.stackedWidget = stackedWidget
        
        self.setWindowTitle('Add Ticket')
        
        font = QtGui.QFont()
        font.setPointSize(20)

        layout = QGridLayout()

        self.name_label = QLabel('Type Name:')
        self.name_edit = QLineEdit()

        self.price_label = QLabel('Ticket Price:')
        self.price_edit = QLineEdit()

        self.backButton = QPushButton("Back")
        self.submitButton = QPushButton("Submit")

        layout.addWidget(self.name_label,0,0)
        layout.addWidget(self.name_edit,0,1)
        layout.addWidget(self.price_label, 1, 0)
        layout.addWidget(self.price_edit, 1, 1)

        layout.addWidget(self.backButton,7, 0 )
        layout.addWidget(self.submitButton,7 ,2)

        self.backButton.clicked.connect(self.goBack)
        self.submitButton.clicked.connect(self.addTic)

        self.setLayout(layout)

    def goBack(self):
        self.stackedWidget.setCurrentIndex(13)

    def addTic(self):
        name = self.name_edit.text()
        price = self.price_edit.text()
        addTicController.addTicC(self, self.stackedWidget, name ,price)

        self.name_edit.clear()
        self.price_edit.clear()

#UI for delete =============================================================

class delHalls(QWidget):
    def __init__(self, stackedWidget, hallList):
        super().__init__()

        self.stackedWidget = stackedWidget
        
        self.setWindowTitle('Delete Hall')
        
        font = QtGui.QFont()
        font.setPointSize(20)

        layout = QGridLayout()

        self.name_label = QLabel('Type Name:')
        self.name_edit = QLineEdit()

        self.price_label = QLabel('Ticket Price:')
        self.price_edit = QLineEdit()

        self.backButton = QPushButton("Back")
        self.submitButton = QPushButton("Submit")

        layout.addWidget(self.name_label,0,0)
        layout.addWidget(self.name_edit,0,1)
        layout.addWidget(self.price_label, 1, 0)
        layout.addWidget(self.price_edit, 1, 1)

        layout.addWidget(self.backButton,7, 0 )
        layout.addWidget(self.submitButton,7 ,2)

        self.backButton.clicked.connect(self.goBack)


        self.setLayout(layout)

    def goBack(self):
        self.stackedWidget.setCurrentIndex(11)

class delFnB(QWidget):
    def __init__(self, stackedWidget, fbList):
        super().__init__()

        self.stackedWidget = stackedWidget
        
        self.setWindowTitle('Delete F&B')
        
        font = QtGui.QFont()
        font.setPointSize(20)

        layout = QGridLayout()

        self.name_label = QLabel('F&B Name:')
        self.name_edit = QLineEdit()

        self.price_label = QLabel('Item Price:')
        self.price_edit = QLineEdit()

        self.backButton = QPushButton("Back")
        self.submitButton = QPushButton("Submit")

        layout.addWidget(self.name_label,0,0)
        layout.addWidget(self.name_edit,0,1)
        layout.addWidget(self.price_label, 1, 0)
        layout.addWidget(self.price_edit, 1, 1)

        layout.addWidget(self.backButton,7, 0 )
        layout.addWidget(self.submitButton,7 ,2)

        self.backButton.clicked.connect(self.goBack)


        self.setLayout(layout)

    def goBack(self):
        self.stackedWidget.setCurrentIndex(12)


class delTic(QWidget):
    def __init__(self, stackedWidget):
        super().__init__()

        self.stackedWidget = stackedWidget
        
        self.setWindowTitle('Delete Ticket')
        
        font = QtGui.QFont()
        font.setPointSize(20)

        layout = QGridLayout()

        self.name_label = QLabel('Type Name:')
        self.name_edit = QLineEdit()

        self.price_label = QLabel('Ticket Price:')
        self.price_edit = QLineEdit()

        self.backButton = QPushButton("Back")
        self.submitButton = QPushButton("Submit")

        layout.addWidget(self.name_label,0,0)
        layout.addWidget(self.name_edit,0,1)
        layout.addWidget(self.price_label, 1, 0)
        layout.addWidget(self.price_edit, 1, 1)

        layout.addWidget(self.backButton,7, 0 )
        layout.addWidget(self.submitButton,7 ,2)

        self.backButton.clicked.connect(self.goBack)


        self.setLayout(layout)

    def goBack(self):
        self.stackedWidget.setCurrentIndex(13)

class no:
    def nono(self):
        items = [self.selectedcountry.item(i).text() for i in range(self.selectedcountry.count())]
        items_str = ' '.join(items)
        try:
            if not items_str:
                raise ValueError("No countries selected")
            message = f'Are you sure you want to retrieve data from these countries? \nCountries: {items_str}'     
            confirm = QMessageBox.question(self, 'Retrieve Data', message ,
                                            QMessageBox.Yes | QMessageBox.No)
            if confirm == QMessageBox.Yes:
                print("ok")
        except ValueError as e:
            QMessageBox.warning(self, 'Error', str(e))

class cinemaHallUI(QWidget):
    def __init__(self, stackedWidget):
        super().__init__()
        
        # Define the number of rows and columns of seats
        rows = 8
        cols = 8
        
        # Create a grid layout to hold the seats
        grid = QGridLayout()
        hallName = QLabel("Hall 1")
        screen = QLabel("Screen")
        randomBtn = QPushButton("Random")
        grid.addWidget(hallName, 0, 1, 1, cols)
        grid.addWidget(screen, 1 ,1, 1, cols)
        screen.setAlignment(Qt.AlignCenter)
        screen.setFixedSize(cols*100,20)
        hallName.setAlignment(Qt.AlignCenter)
        hallName.setFixedSize(cols*100,20)
        
        # List of alphabets for row labels
        row_labels = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

        
        # Add a label for each row
        for i in range(rows):
            label = QLabel(row_labels[i])
            label.setAlignment(Qt.AlignCenter)
            grid.addWidget(label, i+2, 0)
        
        # Add a button for each seat in the grid
        for row in range(rows):
            for col in range(cols):
                seat = QPushButton(f"Seat {row_labels[row]}-{col+1}")
                grid.addWidget(seat, row+2, col+1)
                seat.clicked.connect(lambda _, row=row, col=col: self.on_seat_selected(row, col))
        
        grid.addWidget(randomBtn, rows + 4, 0)

        self.setLayout(grid)

    def on_seat_selected(self, row, col):
        print(f"Seat {chr(row+65)}-{col+1} selected")

    #def addHall(self,stackedwidget):
