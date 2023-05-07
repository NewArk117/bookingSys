#GUI imports
from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton,QGridLayout, QListWidget
from PyQt5 import QtGui

#Import links to different scripts in Controller
import sys 
sys.path.append('./Controller')
from delMoviesController import delMoviesController
from delTicsController import delTicsController
from delHallsController import delHallsController
from delFBController import delFBController

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
        self.ticketList = QListWidget()
        self.addButton = QPushButton("Add")
        self.delButton = QPushButton("Delete")
        self.editButton = QPushButton("Edit")
        self.backButton = QPushButton("Back")
        
        layout.addWidget(self.label1, 0, 0)
        layout.addWidget(self.ticketList, 1, 0, 4, 1)
        layout.addWidget(self.addButton, 1 , 1)
        layout.addWidget(self.delButton, 1, 2)
        layout.addWidget(self.editButton, 2, 1)
        layout.addWidget(self.backButton, 7, 2)

        self.backButton.clicked.connect(self.goBack)
        self.addButton.clicked.connect(self.addTic)
        self.delButton.clicked.connect(self.delTics)

        self.setLayout(layout)

    def goBack(self):
        self.stackedWidget.setCurrentIndex(9)

    def addTic(self):
        self.stackedWidget.setCurrentIndex(15)

    def delTics(self):
        delTicsController.delTicsC(self, self.stackedWidget, self.ticketList)
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
        self.delButton.clicked.connect(self.delTics)

        self.setLayout(layout)

    def goBack(self):
        self.stackedWidget.setCurrentIndex(9)

    def addFB(self):
        self.stackedWidget.setCurrentIndex(16)

    def delTics(self):
        delFBController.delFBC(self, self.stackedWidget, self.fbList)


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


        self.setLayout(layout)

    def goBack(self):
        self.stackedWidget.setCurrentIndex(12)


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


        self.setLayout(layout)

    def goBack(self):
        self.stackedWidget.setCurrentIndex(13)

#UI for delete =============================================================
class delMovies(QWidget):
    def __init__(self, stackedWidget, moviesList):
        super().__init__()
        
        self.moviesList = moviesList
        self.stackedWidget = stackedWidget
        
        self.setWindowTitle('Delete Movies')
        
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

    def deleteMovie(self):
        delMoviesController.delMoviesC(self,self.stackedWidget, self.moviesList)

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
    def __init__(self, stackedWidget, ticList):
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