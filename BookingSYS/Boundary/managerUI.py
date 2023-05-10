#GUI imports
from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton,QGridLayout, QListWidget, QAbstractItemView, QDialog, QMessageBox
from PyQt5 import QtGui
from PyQt5.QtCore import QStringListModel, Qt, QTimer
import sqlite3
#Import links to different scripts in Controller
import sys 
sys.path.append('./Controller')
from delMoviesController import delMoviesController
from delTicsController import delTicsController
from delHallsController import delHallsController
from delFBController import delFBController

from addTicController import addTicController
from addFBController import addFBController

from listTicketController import listTicketController
from listFBController import listFBController

from editTicsController import editTicsController
from editFBController import editFBController

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
        delTicsController.delTicsC(self, self.stackedWidget, self.ticketList)
        self.listTics()

    def editTics1(self, dialog, name, price, name2, price2 ):
        editTicsController.editTicsC(self, dialog, self.stackedWidget, name, price, name2, price2 )
        self.listTics()

    def listTics(self):
        listTicketController.listTicC(self, self.stackedWidget, self.ticketList )
    
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

        self.setLayout(layout)

    def goBack(self):
        self.stackedWidget.setCurrentIndex(9)

    def addHall(self):
        self.stackedWidget.setCurrentIndex(17)

    def delHall(self):
        delHallsController.delHallsC(self, self.stackedWidget, self.hallList)

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