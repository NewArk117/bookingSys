import sqlite3

#GUI Imports
from PyQt5.QtWidgets import QMessageBox, QLineEdit, QGridLayout, QWidget, QLabel, QTextEdit
from PyQt5.QtCore import Qt
#Import links to different scripts in Boundary
import sys 
sys.path.append('./Boundary')

class FnB:
    def delFB(self, stackedWidget, fbList):
            self.stackedWidget = stackedWidget
            self.fbList = fbList
            
            items = self.fbList.currentItem()
            foodname = items.text()[:20].strip() 
            price = items.text()[21:30].strip()
            quantity = items.text()[31:50].strip()
            print(foodname)
            try:
                if not items:
                    raise ValueError("No F&B selected")
                message = f'Are you sure you want to remove {foodname} ?'     
                confirm = QMessageBox.question(self.stackedWidget, 'Remove F&B', message ,
                                                QMessageBox.Yes | QMessageBox.No)
                if confirm == QMessageBox.Yes:
                    print("ok")
                    #insert sql to remove movie here 
                    conn = sqlite3.connect('SilverVillageUserAcc.db')
                    cursor = conn.cursor()

                    sql = "DELETE FROM food WHERE foodname = ? AND price = ?"
                    data = (foodname, price)
                    cursor.execute(sql, data)

                    conn.commit()
                    conn.close()
                    self.listManagerFB(self.stackedWidget, self.fbList) 
            except ValueError as e:
                QMessageBox.warning(self.stackedWidget, 'Error', str(e))
                print(str(e))

    def addFB(self, stackedWidget, name , price, quantity):
        self.stackedWidget = stackedWidget
        message = f'Add F&B named:{name} \nPrice:{price}\nQuantity{quantity} '
        try:   
            confirm = QMessageBox.question(self.stackedWidget, 'Add F&B', message ,
                                            QMessageBox.Yes | QMessageBox.No)
            if confirm == QMessageBox.Yes:
                conn = sqlite3.connect('SilverVillageUserAcc.db')

                # Get a cursor object
                cursor = conn.cursor()

                # Insert a new record into the account table
                sql = "INSERT INTO food (foodname, price, quantity) VALUES (?, ?, ?)"
                data = (name, price, quantity)
                cursor.execute(sql, data)

                # Commit the transaction
                conn.commit()

                # Close the database connection
                conn.close()
        
                self.stackedWidget.setCurrentIndex(12)

        except ValueError as e:
            QMessageBox.warning(self.stackedWidget, 'Error', str(e))
            print(str(e))

    def listManagerFB(self, stackWidget, list):
        self.list = list
        conn = sqlite3.connect('SilverVillageUserAcc.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM food')
        fb_data = cursor.fetchall()
        fb_strings = []
        for row in fb_data:
            fb_string = '{:<20}\t{:<30}\t{:50}'.format(row[0], row[1], row[2])
            fb_strings.append(fb_string)
        self.list.clear()
        self.list.addItems(fb_strings)
        conn.close()

    def editFB(self, dialog, stackedwidget, name1 , price1,quantity1, name2, price2, quantity2):
        self.stackedWidget = stackedwidget
        self.dialog = dialog
        message = f'Confirm to update(?)\nOld Item:{name1}\nOld Price:{price1}\nOld Quantity:{quantity1}\nTo\nNew Name:{name2}\nNew Price:{price2}\nNew Quantity:{quantity2}'
        try:   
            confirm = QMessageBox.question(self.stackedWidget, 'Update F&B', message ,
                                            QMessageBox.Yes | QMessageBox.No)
            if confirm == QMessageBox.Yes:
                conn = sqlite3.connect('SilverVillageUserAcc.db')
                cursor = conn.cursor()

                # Update an existing record in the ticketType table
                sql = "UPDATE food SET foodname = ?, price = ?, quantity = ? WHERE foodname = ? AND price = ? AND quantity = ?"
                data = (name2, price2, quantity1, name1, price1, quantity2)
                cursor.execute(sql, data)

                # Commit the transaction
                conn.commit()

                # Close the database connection
                conn.close()

                self.dialog.reject()

        except ValueError as e:
            QMessageBox.warning(self.stackedWidget, 'Error', str(e))
            print(str(e))