import sqlite3

#GUI Imports
from PyQt5.QtWidgets import QMessageBox, QListWidgetItem

#Import links to different scripts in Boundary
import sys 
sys.path.append('./Boundary')

class FnB:
    def susFB(self, stackedWidget, fbList):
        self.stackedWidget = stackedWidget
        self.fbList = fbList
        
        items = self.fbList.currentItem()
        foodname = items.text()[:20].strip() 
        #print(foodname)
        
        #insert sql to remove movie here 
        conn = sqlite3.connect('SilverVillageUserAcc.db')
        cursor = conn.cursor()

        sql = "UPDATE food SET isAvailable = ? WHERE foodname = ?"
        data = (0 ,foodname)
        cursor.execute(sql, data)

        conn.commit()
        conn.close()


    def addFB(self, stackedWidget, name , price, quantity):
        self.stackedWidget = stackedWidget
       
        try:   
            conn = sqlite3.connect('SilverVillageUserAcc.db')

            # Get a cursor object
            cursor = conn.cursor()

            # Insert a new record into the account table
            sql = "INSERT INTO food (foodname, price, quantity, isAvailable) VALUES (?, ?, ?, ?)"
            data = (name, price, quantity, 1)
            cursor.execute(sql, data)

            # Commit the transaction
            conn.commit()

            # Close the database connection
            conn.close()
    
            self.stackedWidget.setCurrentIndex(12)

        except ValueError as e:
            self.stackedWidget.setCurrentIndex(12)

    def listManagerFB(self, stackWidget, list):
        self.list = list
        conn = sqlite3.connect('SilverVillageUserAcc.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM food')
        fb_data = cursor.fetchall()
        fb_strings = []
        for row in fb_data:
            #fb_string = '{:<20}\t{:<30}\t{:50}'.format(row[0], row[1], row[2])
            fb_string = '{:<20}'.format(row[0])
            fb_strings.append(fb_string)
        self.list.clear()
        self.list.addItems(fb_strings)
        conn.close()

    def editFB(self, dialog, stackedwidget, name1 , price1,quantity1, avail1, name2, price2, quantity2, avail2):
        self.stackedWidget = stackedwidget
        self.dialog = dialog

        if name2 == "":
            name2 = name1
        if price2 == "":
            price2 = price1
        if quantity2 == "":
            quantity2 = quantity1
        if avail2 == "":
            avail2 = avail1
        
        conn = sqlite3.connect('SilverVillageUserAcc.db')
        cursor = conn.cursor()

        # Update an existing record in the ticketType table
        sql = "UPDATE food SET foodname = ?, price = ?, quantity = ?, isAvailable = ? WHERE foodname = ? AND price = ? AND quantity = ? AND isAvailable = ?"
        data = (name2, price2, quantity2, avail2, name1, price1, quantity1, avail1)
        cursor.execute(sql, data)

        # Commit the transaction
        conn.commit()

        # Close the database connection
        conn.close()

        self.dialog.reject()


    def get_order_items(order_id):
        conn = sqlite3.connect('SilverVillageUserAcc.db')
        cursor = conn.cursor()

        sql = 'SELECT food_name, quantity FROM food_order_items WHERE order_id = ?'
        data = (order_id,)
        cursor.execute(sql, data)

        food_data = cursor.fetchall()

        conn.close()

        return food_data

    def delete_order_item(order_id, food_name, quantity):
        conn = sqlite3.connect('SilverVillageUserAcc.db')
        cursor = conn.cursor()

        sql = '''
        DELETE FROM food_order_items
        WHERE order_id = ? AND food_name = ? AND quantity = ?
        '''

        data = (order_id, food_name, quantity)
        cursor.execute(sql, data)

        conn.commit()
        conn.close()

    def get_food(self):
        conn = sqlite3.connect('SilverVillageUserAcc.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM food')
        food_data = cursor.fetchall()
        conn.close()

        return food_data

    def get_food_data(self):
        conn = sqlite3.connect('SilverVillageUserAcc.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM food')
        food_data = cursor.fetchall()
        conn.close()
        return food_data

    def save_food_order(self, user_id, ticket_id, order_list):
        conn = sqlite3.connect('SilverVillageUserAcc.db')
        cursor = conn.cursor()

        # Insert the order into the food_orders table
        sql = 'INSERT INTO food_orders (user_id, ticket_id) VALUES (?, ?)'
        data = (user_id, ticket_id)
        cursor.execute(sql, data)
        order_id = cursor.lastrowid

        for food_name, quantity in order_list:
            # Insert the food order into the food_order_items table
            sql = 'INSERT INTO food_order_items (order_id, food_name, quantity) VALUES (?, ?, ?)'
            data = (order_id, food_name, quantity)
            cursor.execute(sql, data)

        conn.commit()
        conn.close()

    def searchFB(self, stackedWidget, item_name, list):
        self.stackedWidget = stackedWidget
        self.list = list

        if item_name != "":
            conn = sqlite3.connect('SilverVillageUserAcc.db')
            cursor = conn.cursor()
            list.clear()
            sql = "SELECT * FROM food WHERE foodName = ?"
            value1 = item_name
            cursor.execute(sql, (value1,))
            
            rows = cursor.fetchall()
            # Iterate over the rows and populate the list widget with the data
            for row in rows:
                item = QListWidgetItem(str(row[0]))
                self.list.addItem(item)

            # Close the cursor and the database connection
            cursor.close()
            conn.close()
        else:
            self.list = list
            # Connect to the database
            conn = sqlite3.connect('SilverVillageUserAcc.db')
            
            # Create a cursor object from the connection
            cursor = conn.cursor()
            list.clear()
            # Execute the SQL query to retrieve data from the table
            cursor.execute("SELECT * FROM food")
            
            # Fetch all the rows that match the query
            rows = cursor.fetchall()

            # Iterate over the rows and populate the list widget with the data
            for row in rows:
                item = QListWidgetItem(str(row[0]))
                self.list.addItem(item)

            # Close the cursor and the database connection
            cursor.close()
            conn.close()

    def viewFB(self, stackedWidget, item_name):
            conn = sqlite3.connect('SilverVillageUserAcc.db')
            # Get a cursor object
            cursor = conn.cursor()
            query = "SELECT * FROM food WHERE foodName = ?"
            value1 = item_name.strip()
            # Execute the SQL query to retrieve data from the table
            cursor.execute(query, (value1,))
            # Fetch all the rows that match the query
            rows = cursor.fetchall()
            for row in rows:
                #message_box = QMessageBox()
                text = ("Food Name: " + str(row[0]) + "\n" + "Price: " + str(row[1]) + "\n" + "Quantity: " + str(row[2]) + "\n" + "Availabilty: " + str(row[3]))
                itemname = (str(row[0]))
                #message_box.exec_()
            
            # Close the cursor and the database connection
            cursor.close()
            conn.close()
            return text, itemname
    def getData(self, item_name):
        conn = sqlite3.connect('SilverVillageUserAcc.db')
        # Get a cursor object
        cursor = conn.cursor()
        query = "SELECT * FROM food WHERE foodName = ?"
        value1 = item_name.strip()
        # Execute the SQL query to retrieve data from the table
        cursor.execute(query, (value1,))
        # Fetch all the rows that match the query
        rows = cursor.fetchall()
        for row in rows:
            self.itemname = str(row[0])
            self.price = str(row[1])
            self.quantity = str(row[2])
            self.avail = str(row[3])
        # Close the cursor and the database connection
        cursor.close()
        conn.close()

        return self.itemname, self.price, self.quantity, self.avail

    def get_fnb_records(self, user_id):
        conn = sqlite3.connect('SilverVillageUserAcc.db')
        cursor = conn.cursor()

        sql = '''
            SELECT fo.order_id, t.movieName, t.showtime, t.date, GROUP_CONCAT(foi.food_name || ' (' || foi.quantity || ')'), SUM(foi.quantity), SUM(foi.quantity * food.price)
            FROM food_orders fo
            JOIN ticket t ON fo.ticket_id = t.ticket_ID
            JOIN food_order_items foi ON fo.order_id = foi.order_id
            JOIN food ON foi.food_name = food.foodName
            WHERE fo.user_id = ?
            GROUP BY fo.order_id, t.movieName, t.date, t.showtime
            '''

        data = (user_id,)
        cursor.execute(sql, data)
        fnb_data = cursor.fetchall()

        conn.close()

        return fnb_data
