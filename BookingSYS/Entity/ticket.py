import sqlite3

#GUI Imports
from PyQt5.QtWidgets import QMessageBox, QLineEdit, QGridLayout, QWidget, QLabel, QTextEdit, QComboBox, QListWidget, QVBoxLayout
from PyQt5.QtCore import Qt
#Import links to different scripts in Boundary
import sys 
sys.path.append('./Boundary')

class ticket:

    def purchaseTic(self, stackedwidget , list):
        self.stackedWidget = stackedwidget
        self.movieList = list
        try:

            items = self.movieList.currentItem()
            if items:
                name = items.text()[:20].strip() 
                genre = items.text()[21:51].strip()
                time = items.text()[51:].strip()
                print(name + " " + genre + " " + time)  
            else:
                raise ValueError("No movies selected")
        except ValueError as e:
                QMessageBox.warning(self.stackedWidget, 'Error', str(e))
                print(str(e))

    def getTic(self, number):
        conn = sqlite3.connect('SilverVillageUserAcc.db')
        cursor = conn.cursor()

        self.number = int(number)
        self.ticketsList = QListWidget
        self.tictype = QComboBox

        sql = "SELECT * FROM ticketType"
        cursor.execute(sql)
        type_data = cursor.fetchall()
        type_box = []
        for row in type_data:
            type_string = row[0]
            type_box.append(type_string)
        self.tictype.addItems(type_box)
        list = []

        layout = QVBoxLayout

        for x in range(number):
             ticket = QLabel("Ticket " + (number+1))
        
        conn.commit()

        conn.close()

        

           