#GUI imports
from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton,QGridLayout, QListWidget, QAbstractItemView, QDialog, QMessageBox, QHBoxLayout, QDateEdit
from PyQt5 import QtGui
from PyQt5.QtCore import QStringListModel, Qt, QTimer, QDate
import sqlite3
#Import links to different scripts in Controller
import sys 
import calendar
import datetime
sys.path.append('./Controller')
sys.path.append('./Entity')
from FBController import susFBController, addFBController ,listFBController, editFBController, searchFBController, viewFBController
from movieController import susMovieController, addMovieController, listMovieController, editMovieController, searchMovieController, viewMovieController
from ticTypeController import susTicTypeController, addTicTypeController, listTicTypeController, editTicTypeController, searchTicTypeController, viewTicTypeController
from cinemaHallController import susHallsController, addHallController , listHallController , editHallController, searchHallController, viewHallController
from logOutController import logOutController
from ticketType import ticketType
from cinemaHall import cinemaHall
from movie import movie
from fnb import FnB


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
        self.logoutButton.clicked.connect(self.logOut)

        self.setLayout(layout)

    def goMovie(self):
        self.stackedWidget.setCurrentIndex(10)
    
    def goHalls(self):
        self.stackedWidget.setCurrentIndex(11)

    def goFB(self):
        self.stackedWidget.setCurrentIndex(12)
    
    def goTicket(self):
        self.stackedWidget.setCurrentIndex(13)

    def logOut(self):
        reply = QMessageBox.question(self, 'Confirm logout',
                                    'Are you sure you want to logout?',
                                     QMessageBox.Yes | QMessageBox.No)
        
        if reply == QMessageBox.Yes:
            #Call the controlller
            logout = logOutController.loggingOut(self)

            if logout == True:
                self.stackedWidget.setCurrentIndex(0)

#Create ticket GUi
#19. Cinema Manager Boundary
#20. Cinema Manager Boundary
#21. Cinema Manager Boundary
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
        self.delButton = QPushButton("Suspend")
        self.editButton = QPushButton("Edit")
        self.backButton = QPushButton("Back")
        self.viewButton = QPushButton("View")
        layout.addWidget(self.viewButton, 3,2)

        layoutSearch = QHBoxLayout()
        self.searchLabel = QLabel("Search: ")
        self.searchEdit = QLineEdit()
        self.searchBtn = QPushButton("Search")
        layoutSearch.addWidget(self.searchBtn)
        layoutSearch.addWidget(self.searchLabel)
        layoutSearch.addWidget(self.searchEdit)
        
        layout.addWidget(self.label1, 0, 0)
        #layout.addWidget(self.label2, 1, 0)
        layout.addLayout(layoutSearch, 1, 0)
        layout.addWidget(self.ticketList, 2, 0, 4, 1)
        layout.addWidget(self.addButton, 2, 1)
        layout.addWidget(self.delButton, 2, 2)
        layout.addWidget(self.editButton, 3, 1)
        layout.addWidget(self.backButton, 7, 2)

        self.backButton.clicked.connect(self.goBack)
        self.addButton.clicked.connect(self.addTic)
        self.delButton.clicked.connect(self.susTics)
        self.editButton.clicked.connect(self.editTicsUI)
        self.searchBtn.clicked.connect(self.searchTicType)
        self.viewButton.clicked.connect(self.viewTicType)

        #self.timer = QTimer()
        #self.timer.setInterval(1000)
        #self.timer.timeout.connect(self.listTics)
        #self.timer.start()

        self.setLayout(layout)
        self.stackedWidget.currentChanged.connect(self.listTics)

    
    def viewTicType(self):
        text, typename = viewTicTypeController.viewTicTypeC(self, self.stackedWidget, self.ticketList)
        msgBox = QMessageBox()
        msgBox.setText(text)
        msgBox.setWindowTitle(typename)
        msgBox.exec_()
        
    def goBack(self):
        self.stackedWidget.setCurrentIndex(9)

    def addTic(self):
        self.stackedWidget.setCurrentIndex(15)
        self.listTics()

    def susTics(self):
        susTicTypeController.susTicTypeC(self, self.stackedWidget, self.ticketList)
        self.listTics()
        


    def editTics(self, dialog, ticketList, name2, price2, avail2):
        #20. Cinema Manager Controller (ticTypeController.py)
        editTicTypeController.editTicTypeC(self, dialog, self.stackedWidget,ticketList, name2, price2, avail2 )
        self.listTics()

    def listTics(self):
        #19. Cinema Manager Controller
        listTicTypeController.listTicTypeC(self, self.stackedWidget, self.ticketList )
    
    def searchTicType(self):
        item_name = self.searchEdit.text()
        list = searchTicTypeController.searchTicTypeC(self, self.stackedWidget, item_name, self.ticketList)
    
    def editTicsUI(self):
        self.dialog = QDialog(self)
        self.dialog.setWindowTitle("Edit Type")

        font = QtGui.QFont()
        font.setPointSize(20)

        layout = QGridLayout(self.dialog)
        self.name1_label = QLabel('Name:')
        self.name1_edit = QLineEdit()
        #self.name1_edit.setPlaceholderText(typename)

        self.price1_label = QLabel('Price:')
        self.price1_edit = QLineEdit()
        #self.price1_edit.setPlaceholderText(price)

        self.avail_label = QLabel('Availabilty:')
        self.avail_edit = QLineEdit()
        #self.avail_edit.setPlaceholderText(avail)
        
        self.backButton = QPushButton("Back")
        self.submitButton = QPushButton("Submit")

        layout.addWidget(self.name1_label,0,0)
        layout.addWidget(self.name1_edit,0,1)
        layout.addWidget(self.price1_label, 1, 0)
        layout.addWidget(self.price1_edit, 1, 1)

        layout.addWidget(self.avail_label,2,0)
        layout.addWidget(self.avail_edit,2,1)

        layout.addWidget(self.backButton,5, 0 )
        layout.addWidget(self.submitButton,5 ,2)

        self.backButton.clicked.connect(self.dialog.reject)
        self.submitButton.clicked.connect(lambda: (self.editTics(self.dialog,self.ticketList, self.name1_edit.text(), self.price1_edit.text(), self.avail_edit.text())))

        self.dialog.exec_()

#Create movies GUI
#9. Cinema Manager Boundary
#10. Cinema Manager Boundary
#11. Cinema Manager Boundary
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
        self.delButton = QPushButton("Suspend")
        self.editButton = QPushButton("Edit")
        self.backButton = QPushButton("Back")
        self.viewButton = QPushButton("View")
        layout.addWidget(self.viewButton, 3,2)
        
        layoutSearch = QHBoxLayout()
        self.searchLabel = QLabel("Search: ")
        self.searchEdit = QLineEdit()
        self.searchBtn = QPushButton("Search")
        layoutSearch.addWidget(self.searchBtn)
        layoutSearch.addWidget(self.searchLabel)
        layoutSearch.addWidget(self.searchEdit)

        layout.addWidget(self.label1, 0, 0)
        layout.addLayout(layoutSearch, 1, 0)
        layout.addWidget(self.moviesList, 2, 0, 4, 1)
        layout.addWidget(self.addButton, 2 , 1)
        layout.addWidget(self.delButton, 2, 2)
        layout.addWidget(self.editButton, 3, 1)
        layout.addWidget(self.backButton, 7, 2)

        self.backButton.clicked.connect(self.goBack)
        self.addButton.clicked.connect(self.addMov)
        self.delButton.clicked.connect(self.susMovie)
        self.editButton.clicked.connect(self.editMovieUI)
        self.searchBtn.clicked.connect(self.searchMovie)
        self.viewButton.clicked.connect(self.viewMovie)

        self.setLayout(layout)
        self.stackedWidget.currentChanged.connect(self.listMovie)

    def viewMovie(self):
        text, moviename = viewMovieController.viewMovieC(self, self.stackedWidget, self.moviesList)

        msgBox = QMessageBox()
        msgBox.setText(text)
        msgBox.setWindowTitle(moviename)
        msgBox.exec_()


    def goBack(self):
        self.stackedWidget.setCurrentIndex(9)

    def addMov(self):
        self.stackedWidget.setCurrentIndex(14)

    def susMovie(self):
        #11. Cinema Manager COntroller
        susMovieController.susMovieC(self,self.stackedWidget, self.moviesList)

    def listMovie(self):
        #9. Cinema Manager Controller
        listMovieController.listMovieC(self, self.stackedWidget, self.moviesList, 1)

    def searchMovie(self):
        item_name = self.searchEdit.text()
        list = searchMovieController.searchMovieC(self, self.stackedWidget, item_name, self.moviesList)


    def editMovie(self,  dialog , name2, genre2, avail2):
        #10. Cinema Manager Controller
        editMovieController.editMovieC(self,self.stackedWidget,dialog,self.moviesList, name2, genre2, avail2)
        self.listMovie()

    #10. Cinema Manager Boundary
    def editMovieUI(self):
        self.dialog = QDialog(self)
        self.dialog.setWindowTitle("Edit Hall")

        font = QtGui.QFont()
        font.setPointSize(20)

        layout = QGridLayout(self.dialog)
        #self.getOldTicket()
        
        self.name_label = QLabel('Movie Name:')
        self.name_edit = QLineEdit()
        #self.name_edit.setPlaceholderText(moviename)

        self.genre_label = QLabel('Genre:')
        self.genre_edit = QLineEdit()
        #self.genre_edit.setPlaceholderText(genre)

        self.avail_label = QLabel('Availabilty:')
        self.avail_edit = QLineEdit()
        #self.avail_edit.setPlaceholderText(avail)

        self.backButton = QPushButton("Back")
        self.submitButton = QPushButton("Submit")

        layout.addWidget(self.name_label,0,0)
        layout.addWidget(self.name_edit,0,1)

        layout.addWidget(self.genre_label, 1, 0)
        layout.addWidget(self.genre_edit, 1, 1)

        layout.addWidget(self.avail_label,2,0)
        layout.addWidget(self.avail_edit,2,1)

        layout.addWidget(self.backButton,5, 0 )
        layout.addWidget(self.submitButton,5 ,2)
        
        self.backButton.clicked.connect(self.dialog.reject)
        self.submitButton.clicked.connect(lambda: (self.editMovie(self.dialog, self.name_edit.text(), self.genre_edit.text(), self.avail_edit.text())))

        self.dialog.exec_()

#Create hall GUI

#4. Cinema Manager Boundary
#5. Cinema Manager Boundary
#6. Cinema Manager Boundary
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
        self.viewButton = QPushButton("View")
        layout.addWidget(self.viewButton, 3,2)

        layoutSearch = QHBoxLayout()
        self.searchLabel = QLabel("Search: ")
        self.searchEdit = QLineEdit()
        self.searchBtn = QPushButton("Search")
        layoutSearch.addWidget(self.searchBtn)
        layoutSearch.addWidget(self.searchLabel)
        layoutSearch.addWidget(self.searchEdit)
        
        layout.addWidget(self.label1, 0, 0)
        layout.addLayout(layoutSearch, 1, 0)
        layout.addWidget(self.hallList, 2, 0, 4, 1)
        layout.addWidget(self.addButton, 2 , 1)
        layout.addWidget(self.delButton, 2, 2)
        layout.addWidget(self.editButton, 3, 1)
        layout.addWidget(self.backButton, 7, 2)

        self.backButton.clicked.connect(self.goBack)
        self.addButton.clicked.connect(self.addHall)
        self.delButton.clicked.connect(self.susHall)
        self.editButton.clicked.connect(self.editHallUI)
        self.searchBtn.clicked.connect(self.searchHall)
        self.viewButton.clicked.connect(self.viewHall)

        self.setLayout(layout)
        self.stackedWidget.currentChanged.connect(self.listHalls)

    def viewHall(self):
            text, hallname = viewHallController.viewHallC(self, self.stackedWidget, self.hallList)

            msgBox = QMessageBox()
            msgBox.setText(text)
            msgBox.setWindowTitle(hallname)
            msgBox.exec_()

       
    def goBack(self):
        self.stackedWidget.setCurrentIndex(9)

    def addHall(self):
        self.stackedWidget.setCurrentIndex(17)

    def susHall(self):
        #6. Cinema Manager Controller (same)
        susHallsController.susHallsC(self, self.stackedWidget, self.hallList)

    
    def listHalls(self):
        #4. Cinema Manager Controller (hallcontroller.py)
        listHallController.listHallC(self, self.stackedWidget, self.hallList )

    def searchHall(self):
        item_name = self.searchEdit.text()
        list = searchHallController.searchHallC(self, self.stackedWidget, item_name, self.hallList)


    def editHall(self,  dialog, name2, avail2):
        #5. Cinema Manager Controller (hallcontroller.py)
        #editHallController.editHallC(self,self.stackedWidget, dialog ,name , avail, name2, avail2)
        editHallController.editHallC(self,self.stackedWidget, dialog ,self.hallList, name2, avail2)
        self.listHalls()
      
    def editHallUI(self):
        self.dialog = QDialog(self)
        self.dialog.setWindowTitle("Edit Hall")

        font = QtGui.QFont()
        font.setPointSize(20)

        layout = QGridLayout(self.dialog)
        #self.getOldTicket()
    
        self.name_label = QLabel('Hall Name:')
        self.name_edit = QLineEdit()
        #self.name_edit.setPlaceholderText(hallname)

        self.avail_label = QLabel('Availability:')
        self.avail_edit = QLineEdit()
        #self.avail_edit.setPlaceholderText(avail)

        #print (name + rows + columns + capacity + availString)

        self.backButton = QPushButton("Back")
        self.submitButton = QPushButton("Submit")

        layout.addWidget(self.name_label,0,0)
        layout.addWidget(self.name_edit,0,1)

        layout.addWidget(self.avail_label, 3, 0)
        layout.addWidget(self.avail_edit, 3, 1)


        layout.addWidget(self.backButton,5, 0 )
        layout.addWidget(self.submitButton,5 ,2)
        
        self.backButton.clicked.connect(self.dialog.reject)
        self.submitButton.clicked.connect(lambda: (self.editHall(self.dialog,self.name_edit.text(), self.avail_edit.text())))

        self.dialog.exec_()


#14. Cinema Manager Boundary
#15. Cinema Manager BOundary
#16. Cinema Manager Boundary
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
        self.delButton = QPushButton("Suspend")
        self.editButton = QPushButton("Edit")
        self.backButton = QPushButton("Back")
        self.viewButton = QPushButton("View")
        layout.addWidget(self.viewButton, 3,2)
        
        layoutSearch = QHBoxLayout()
        self.searchLabel = QLabel("Search: ")
        self.searchEdit = QLineEdit()
        self.searchBtn = QPushButton("Search")
        layoutSearch.addWidget(self.searchBtn)
        layoutSearch.addWidget(self.searchLabel)
        layoutSearch.addWidget(self.searchEdit)

        layout.addWidget(self.label1, 0, 0)
        layout.addLayout(layoutSearch, 1,0)
        layout.addWidget(self.fbList, 2, 0, 4, 1)
        layout.addWidget(self.addButton, 2 , 1)
        layout.addWidget(self.delButton, 2, 2)
        layout.addWidget(self.editButton, 3, 1)
        layout.addWidget(self.backButton, 7, 2)

        self.backButton.clicked.connect(self.goBack)
        self.addButton.clicked.connect(self.addFB)
        self.delButton.clicked.connect(self.susFB)
        self.editButton.clicked.connect(self.editFBUI)
        self.searchBtn.clicked.connect(self.searchFB)
        self.viewButton.clicked.connect(self.viewFB)

        self.setLayout(layout)
        self.stackedWidget.currentChanged.connect(self.listFB)

        
    def viewFB(self):
        text, itemname = viewFBController.viewFBC(self, self.stackedWidget, self.fbList)
        msgBox = QMessageBox()
        msgBox.setText(text)
        msgBox.setWindowTitle(itemname)
        msgBox.exec_()
    
    def goBack(self):
        self.stackedWidget.setCurrentIndex(9)

    def addFB(self):
        self.stackedWidget.setCurrentIndex(16)
        self.listFB()
    
    def susFB(self):
        #16. Cinema Manager Controller
        susFBController.susFBC(self, self.stackedWidget, self.fbList)
        self.listFB()

    def listFB(self):
        #14. Cinema Manager Controller (look for fnbcontroller.py)
        listFBController.listFBC(self, self.stackedWidget, self.fbList)

    def editFB(self, dialog, fbList, name2, price2 , quantity2, avail2):
        #15. Cinema Manager Controller
        editFBController.editFBC(self, dialog, self.stackedWidget, fbList,name2, price2, quantity2,avail2 )
        self.listFB()

    def searchFB(self):
        item_name = self.searchEdit.text()
        list = searchFBController.searchFBC(self, self.stackedWidget, item_name, self.fbList)

    #15. Cinema Manager Boundary
    def editFBUI(self):
        self.dialog = QDialog(self)
        self.dialog.setWindowTitle("Edit F&B")

        font = QtGui.QFont()
        font.setPointSize(20)


        self.name_label = QLabel('Item Name:')
        self.name_edit = QLineEdit()
        #self.name_edit.setPlaceholderText(itemname)

        self.price_label = QLabel('Price:')
        self.price_edit = QLineEdit()
        #self.price_edit.setPlaceholderText(price)

        self.quantity_label = QLabel('Quantity:')
        self.quantity_edit = QLineEdit()
        #self.quantity_edit.setPlaceholderText(quantity)

        self.avail_label = QLabel('Availability:')
        self.avail_edit = QLineEdit()
        #self.avail_edit.setPlaceholderText(avail)

        layout = QGridLayout(self.dialog)
        #print (name + rows + columns + capacity + availString)

        self.backButton = QPushButton("Back")
        self.submitButton = QPushButton("Submit")

        layout.addWidget(self.name_label,0,0)
        layout.addWidget(self.name_edit,0,1)

        layout.addWidget(self.price_label, 1, 0)
        layout.addWidget(self.price_edit, 1, 1)

        layout.addWidget(self.quantity_label,2,0)
        layout.addWidget(self.quantity_edit,2,1)

        layout.addWidget(self.avail_label, 3, 0)
        layout.addWidget(self.avail_edit, 3, 1)

        layout.addWidget(self.backButton,5, 0 )
        layout.addWidget(self.submitButton,5 ,2)

        self.backButton.clicked.connect(self.dialog.reject)
        self.submitButton.clicked.connect(lambda: (self.editFB(self.dialog, self.fbList, self.name_edit.text(), self.price_edit.text(), self.quantity_edit.text(), self.avail_edit.text() )))

        self.dialog.exec_()

#UI for create========================================
#8. Cinema Manager Boundary
class addMovies(QWidget):
    def __init__(self, stackedWidget):
        super().__init__()

        self.stackedWidget = stackedWidget
        
        self.setWindowTitle('Add Movies')
        
        font = QtGui.QFont()
        font.setPointSize(20)

        layout = QGridLayout()

        self.name_label = QLabel('Movie Name:')
        self.name_edit = QLineEdit()

        self.genre_label = QLabel('Genre:')
        self.genre_edit = QLineEdit()

        today = datetime.date.today()
        default_date = QDate(today)  # May 1st, 2023
        # Set the default date for endDateCal
        #default_date = QDate.currentDate()  # Today's date

        # Set up the date edit widgets
        self.startDate = QLabel("Start date:")
        self.startDateCal = QDateEdit()
        self.startDateCal.setDate(default_date)

        self.endDate = QLabel("End date:")
        self.endDateCal = QDateEdit()
        self.endDateCal.setDate(self.startDateCal.date().addMonths(1))

        self.backButton = QPushButton("Back")
        self.submitButton = QPushButton("Submit")

        layout.addWidget(self.name_label,0,0)
        layout.addWidget(self.name_edit,0,1)
        layout.addWidget(self.genre_label, 1, 0)
        layout.addWidget(self.genre_edit, 1, 1)
        layout.addWidget(self.startDate, 2, 0)
        layout.addWidget(self.startDateCal, 2, 1)
        layout.addWidget(self.endDate, 3, 0)
        layout.addWidget(self.endDateCal, 3, 1)
        layout.addWidget(self.backButton,9, 0 )
        layout.addWidget(self.submitButton,9 ,2)

        self.backButton.clicked.connect(self.goBack)
        self.submitButton.clicked.connect(self.addMovie)

        # layout for manage Accounts -----------------------------------
        self.setLayout(layout)

    def goBack(self):
        self.stackedWidget.setCurrentIndex(10)
    def addMovie(self):
        name = self.name_edit.text()
        genre = self.genre_edit.text()
        start_date = self.startDateCal.date().toPyDate()
        end_date = self.endDateCal.date().toPyDate()
        #8. Cinema Manager Controller (find all controllers in movieController.py)
        addMovieController.addMoviesC(self,self.stackedWidget, name ,genre, start_date, end_date)
        self.name_edit.clear()
        self.genre_edit.clear()
        
#3. Cinema Manager Boundary
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

        self.rows_label = QLabel('Number of rows (1-8):')
        self.rows_edit = QLineEdit()

        self.column_label = QLabel('Number of columns(1-8):')
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
        self.name_edit.clear()
        self.rows_edit.clear()
        self.column_edit.clear()

        #3. Cinema Manager Controller (go to hallcontroller.py)
        addHallController.addHallC(self, self.stackedWidget, name, rows, column)

#13. Cinema Manager Boundary
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

        self.quantity_label = QLabel('Quantity:')
        self.quantity_edit = QLineEdit()

        self.backButton = QPushButton("Back")
        self.submitButton = QPushButton("Submit")

        layout.addWidget(self.name_label,0,0)
        layout.addWidget(self.name_edit,0,1)
        layout.addWidget(self.price_label, 1, 0)
        layout.addWidget(self.price_edit, 1, 1)
        layout.addWidget(self.quantity_label, 2, 0)
        layout.addWidget(self.quantity_edit, 2, 1)

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
        quantity = self.quantity_edit.text()
        #13. Cinema Manager Controller
        addFBController.addFBC(self, self.stackedWidget, name ,price, quantity)

        self.name_edit.clear()
        self.price_edit.clear()
        self.quantity_edit.clear()

#18. Cinema Manager Boundary
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

    #18. Cinema Manager Controller
    def addTic(self):
        name = self.name_edit.text()
        price = self.price_edit.text()

        #18. Cinema Manager Controller (tictypeController.py)
        addTicTypeController.addTicTypeC(self, self.stackedWidget, name ,price)
        
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
                seat.clicked.connect(lambda _, row=row, col=col: self.on_seat_selected(row_labels[row], col))
        
        grid.addWidget(randomBtn, rows + 4, 0)

        self.setLayout(grid)

    def on_seat_selected(self, row, col):
        print(f"Seat {row}-{col+1} selected")

    #def addHall(self,stackedwidget):
