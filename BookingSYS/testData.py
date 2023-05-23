#Necessary imports for database
import sqlite3
import random
import string
import datetime

#Generate random customer username
def randomCust():
    random_names = []
    random_numbers = []
    for i in range(100):
        random_numbers.append(str(random.randrange(1, 1000)).zfill(3))
    
    for i in range(100):
        random_string = ''.join(random.choice(string.ascii_lowercase) for _ in range(random.randint(5, 8)))
        random_names.append(random_string)
    
    combined_list = [str(elem1) + elem2 for elem1, elem2 in zip(random_names, random_numbers)]

    return combined_list

#Generate random customer password
def randomCustPassword():
    random_password = []
    for i in range(100):
        chars = string.ascii_letters + string.digits
        password = ''.join(random.choice(chars) for i in range(8))
        random_password.append(password)
    return random_password

#Generate random staff username
def randomStaff():
    random_names = []
    random_numbers = []
    for i in range(10):
        random_numbers.append(str(random.randrange(1, 1000)).zfill(3))
    
    for i in range(15):
        random_string = ''.join(random.choice(string.ascii_lowercase) for _ in range(random.randint(5, 8)))
        random_names.append(random_string)
    
    combined_list = [str(elem1) + elem2 for elem1, elem2 in zip(random_names, random_numbers)]

    return combined_list

#Generate random staff password
def randomStaffPassword():
    random_password = []
    for i in range(10):
        chars = string.ascii_letters + string.digits
        password = ''.join(random.choice(chars) for i in range(8))
        random_password.append(password)
    return random_password

#Generate movie data
def movieData():
    timeSlot = ["0930","1245","1600","1915","2130","0045"]
    movieName = ["The Shawshank Redemption", "300BC", "Avatar", "Smile", "Truth or Dare"]
    combine = []
    for i in range(len(movieName)):
        for j in range(len(timeSlot)):
            combine.append((movieName[i],timeSlot[j]))
    return combine

#Generate random DOB for customer profile
def randomDateCust():
    integers = []
    for _ in range(100):
        integer = random.randint(20, 70)
        integers.append(integer)
    return integers


#Generate random DOB for staff profile
def randomDateStaff():
    integers = []
    for _ in range(10):
        integer = random.randint(20, 70)
        integers.append(integer)
    return integers

#Generate random name for customer profile
def randomNameCust():
    nameList = []
    first_names = ['Alice', 'Bob', 'Charlie', 'David', 'Emily', 'Frank', 'Grace', 
                   'Hannah', 'Isabelle', 'Jack', 'Kate', 'Liam', 'Mia', 'Nathan', 
                   'Olivia', 'Parker', 'Quinn', 'Rachel', 'Sophia', 'Thomas', 'Ursula', 
                   'Victoria', 'William', 'Xander', 'Yara', 'Zachary']
    last_names = ['Smith', 'Johnson', 'Brown', 'Jones', 'Garcia', 'Miller', 'Davis', 'Martinez',
                   'Hernandez', 'Lopez', 'Gonzalez', 'Perez', 'Taylor', 'Anderson', 'Wilson', 'Moore',
                     'Jackson', 'Martin', 'Lee', 'Rodriguez', 'Walker', 'Allen', 'King', 'Wright', 'Scott']
    for i in range(100):
        first_name = random.choice(first_names)
        last_name = random.choice(last_names)
        combineName = first_name + " " + last_name
        nameList.append(combineName)
    return nameList

#GENERATE DATABASE STARTS HERE--------------------------------------------------------------------
# Connect to the database
conn = sqlite3.connect('SilverVillageUserAcc.db')

#Get a cursor object
cursor = conn.cursor()

#Insert 15 staff into the "account" table
someStaff = randomStaff()
someStaffPassword = randomStaffPassword()
sql = "INSERT INTO account (userID, password, accType, suspend) VALUES (?, ?, ?, ?)"
for i in range(10):  
    if i == 0:
        data = ("owner", "password","cinemaOwner", True)
        cursor.execute(sql, data) 
    elif i == 1:
        data = ("manager", "password", "cinemaManager", True)
        cursor.execute(sql, data) 
    elif i == 2:
        data = ("admin", "password", "sysAdmin", True)
        cursor.execute(sql, data) 
    elif i == 3:
        data = ("customer", "password", "customer", True)
        cursor.execute(sql, data) 
    elif i == 4 or i == 5 or i == 6 or i == 7 or i == 8:
        data = ("manager"+ str(i-2), someStaffPassword[i], "cinemaManager", True)
        cursor.execute(sql, data) 
    else:
        data = ("admin"+ str(i-7), someStaffPassword[i],"sysAdmin", True)
        cursor.execute(sql, data) 

    
# Insert 100 customer into the "account" table
someCust = randomCust()
someCustPassword = randomCustPassword()
sql = "INSERT INTO account (userID, password,accType,suspend) VALUES (?, ?, ?, ?)"
for i in range(100):  
    data = ("cust"+str(i), someCustPassword[i],"customer", True)

    cursor.execute(sql, data)

# Insert random profiles for staff into the "User profile"
someDates1 = randomDateStaff()
staffName = ["Gianna Hess", "Ryan Velasquez", "Alexander OlsenMoses", "FlowersGiada",
             "Vincent Gregory", "Velazquez Sydnee", "Nelson Isabell", "Murphy Ashly", "Pruitt Kelsey",
             "Long Antony", "Hester Carla", "Woods Tess", "Davidson Tanya", "Rogers Mohammad", "Kerr Jackson"]
sql = "INSERT INTO userProfile (userID, name, DOB, accType, suspend) VALUES (?, ?, ?, ?, ?)"
for i in range(10):  
    if i == 0:
        data = ("owner", staffName[i], someDates1[i],"cinemaOwner", True)
        cursor.execute(sql, data) 
    elif i == 1:
        data = ("manager", staffName[i], someDates1[i], "cinemaManager", True)
        cursor.execute(sql, data) 
    elif i == 2:
        data = ("admin", staffName[i], someDates1[i], "sysAdmin", True)
        cursor.execute(sql, data) 
    elif i == 3:
        data = ("customer", staffName[i], someDates1[i], "customer", True)
        cursor.execute(sql, data) 
    elif i == 4 or i == 5 or i == 6 or i == 7 or i == 8:
        data = ("manager"+ str(i-2), staffName[i], someDates1[i], "cinemaManager", True)
        cursor.execute(sql, data) 
    else:
        data = ("admin"+ str(i-7), staffName[i],someDates1[i],"sysAdmin", True)
        cursor.execute(sql, data) 

# Insert random profiles for customer into the "User profile"
someDates2 = randomDateCust()
custName = randomNameCust()
sql = "INSERT INTO userProfile (userID, name, DOB, accType, suspend) VALUES (?, ?, ?, ?,?)"
for i in range(100):  
    data = ("cust"+str(i), custName[i], someDates2[i],"customer", True)

    cursor.execute(sql, data)


# Insert records into the "movie" table
someMovie = movieData()
sql = "INSERT INTO movies (movieID, movieName, timeSlot) VALUES (?, ?, ?)"
for i in range(len(someMovie)):  
    data = (i, someMovie[i][0], someMovie[i][1])
    cursor.execute(sql, data)

#Insert hall data sample
def addHall(name, rows, columns, cursor):
    row_labels = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    rows = int(rows)
    columns = int(columns)

    datelist = []
    showtimes = ["1330", "1530", "1730", "1930", "2130"]
    startDate = datetime.date(2023, 5, 1)
    #startDate = date.today()
    delta = datetime.timedelta(days=1)
    endDate = datetime.date(2023, 11 , 30)
    currentDate = startDate

    while currentDate <= endDate:
        datelist.append(currentDate)
        currentDate += delta

    for date1 in datelist:
        for time in showtimes:
            for rowx in range(rows):
                for col in range(columns):
                    seatNo = "" + row_labels[rowx] + "-" + str(col+1)
                    sql = "INSERT INTO seat (seat_No, hallName, showtime, date ,isAvailable) VALUES (?, ? , ?, ? , ?)"
                    data =(seatNo, name, time, date1, 1)
                    cursor.execute(sql, data)
            sql1 = "INSERT INTO hallshowtime (hallName, showtime, date, isAvailable) VALUES (?, ?, ?, ?)"
            data1 = (name,time,date1, 1)
            cursor.execute(sql1, data1)

    sql2 = "INSERT INTO hall (hallName, rows, columns, capacity, isAvailable) VALUES (?, ?, ?, ? ,?)"
    capacity = rows * columns
    data2 = (name, rows, columns, capacity, 1)
    cursor.execute(sql2, data2)

def addMovie(name, genre, hallname,cursor):
    datelist = []
    showtimes = ["1330", "1530", "1730", "1930", "2130"]
    startDate = datetime.date(2023, 5, 1)
    #startDate = date.today()
    delta = datetime.timedelta(days=1)
    endDate = datetime.date(2023, 6 , 30)
    currentDate = startDate

    while currentDate <= endDate:
        datelist.append(currentDate)
        currentDate += delta

    list =[]
    for x in showtimes:
        list.append([x, hallname])

    for x in list:
        time = int(x[0])
        hall = str(x[1])
        #print("This is time " + str(time) + " This is hall " + hall)
        sql2 = "INSERT INTO movie (movieName, genre, showtime, hallName, startdate, enddate, isAvailable) VALUES (?, ?, ?,?, ? ,?, ?)"
        data2 = (name, genre, time, hall, startDate, endDate, 1)
        cursor.execute(sql2, data2)
        for date in datelist:
            sql3 = "UPDATE hallshowtime SET isAvailable = ? WHERE hallName = ? AND showtime = ? AND date = ?"
            data3 = (0, hall, time, date)
            cursor.execute(sql3, data3)

hallList = ["Hall-1", "Hall-2", "Hall-3", "Hall-4", "Hall-5", "Hall-6", "Hall-7", "Hall-8", "Hall-9", "Hall-10"]
movieList = [["Saw", "Thriller","Hall-1"], ["James Bond","Action","Hall-2" ],["Toy Story", "Family", "Hall-3"], ["Jumanji", "Adventure", "Hall-4"],  ["Avengers", "Action", "Hall-5"], ["Spiderman", "Action", "Hall-6"], ["Titanic", "Love", "Hall-7"], ["Transformers", "Sci-Fi","Hall-8"], ["E.T.", "Sci-Fi","Hall-9"], ["Romeo","Love","Hall-10"]]

for x in hallList:
    addHall(x, 5, 6, cursor)    

for x in movieList:
    addMovie(x[0], x[1], x[2], cursor)


#add food
def addFood( name, price, quantity, cursor):
    # Insert a new record into the food table
    sql = "INSERT INTO food (foodName, price, quantity, isAvailable) VALUES (?, ?, ?, ?)"
    data = (name, price, quantity , 1)
    cursor.execute(sql, data)

addFood("Burger", 5.2, 10 , cursor)
addFood("Coke", 2.5, 10, cursor)
addFood("Popcorn", 7.0, 10, cursor)
addFood("HotDog", 8.0, 10, cursor)
addFood("Cake", 9.0, 10, cursor)
addFood("Fries", 8.0, 10, cursor)
addFood("Candy", 7.0, 10, cursor)
addFood("Chocolate", 6.0, 10, cursor)
addFood("Sprite", 7.0, 10, cursor)
addFood("Nachos", 8.0, 10, cursor)


def addTicketType(name, price, cursor):
    sql = "INSERT INTO ticketType (type, price, isAvailable) VALUES (?, ?, ?)"
    data = (name, price, 1)
    cursor.execute(sql, data)

addTicketType("Adult", 12.0,cursor)
addTicketType("Child", 10.0, cursor)
addTicketType("Senior", 9.0, cursor)

#Insert ticket data
def purchaseTic( movieName, genre, hallName, selectedDate, selectedTime,ticCount,seatList, totalCost, userID, cursor):
        #print(movieName, genre, hallName, selectedDate, selectedTime,ticCount, seatList, totalCost, userID)
        for x in seatList:
            sql = "UPDATE seat SET isAvailable = ? WHERE seat_No = ? AND hallName = ? AND showtime = ? AND date = ?"
            data = (0, x[0] , hallName, selectedTime, selectedDate )
            cursor.execute(sql, data)
            sql2 = "INSERT INTO ticket (userID ,movieName , hallName , seat_No ,showtime,date, type, price) VALUES (?, ?,?, ?,? ,?, ?, ?)"
            data2 = (userID, movieName, hallName, x[0], selectedTime, selectedDate, x[1], x[2])
            cursor.execute(sql2, data2)


purchaseTic("Saw", "Thriller" ,"Hall-1" ,"2023-05-01", 1330 ,7,[['B-4', 'Adult', 12], ['C-4', 'Adult', 12], ['D-4', 'Adult', 12], ['D-5', 'Adult', 12], ['C-6', 'Adult', 12], ['C-3', 'Adult', 12], ['B-3', 'Adult', 12]] ,84 ,"customer", cursor)
purchaseTic("James Bond" ,"Action", "Hall-2",  "2023-06-20", 1730, 7, [['B-4', 'Adult', 12], ['C-4', 'Child', 10], ['C-2', 'Adult', 12], ['B-2', 'Adult', 12], ['B-3', 'Child', 10], ['D-3', 'Child', 10], ['E-4', 'Senior', 9]], 75 ,"customer",cursor)

def generate_random_transactions(cursor):
    customers = [f"cust{i}" for i in range(100)]
    
    for _ in range(100):
        start_date = datetime.date(2023, 5, 1)
        #startDate = date.today()
        delta = datetime.timedelta(days=1)
        end_date = datetime.date(2023, 6 , 30)
        #currentDate = startDate
        showtimes = ["1330", "1530", "1730", "1930", "2130"]
        customer_id = random.choice(customers)
        movie = random.choice(movieList)
        movie_name, genre, hall_name = movie
        
        selected_date = start_date + datetime.timedelta(days=random.randint(0, (end_date - start_date).days))
        selected_time = int(random.choice(showtimes))
        
        tic_count = random.randint(1, 5)
        seat_list = []
        for _ in range(tic_count):
            hall = random.choice(hallList)
            seat_row = random.choice(["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"])
            seat_col = random.randint(1, 6)
            seat = f"{seat_row}-{seat_col}"
            seat_type = random.choice(["Adult", "Child"])
            seat_price = random.randint(10, 20)
            seat_list.append([seat, seat_type, seat_price])
        
        total_cost = sum([seat[2] for seat in seat_list])
        
        purchaseTic(movie_name, genre, hall_name, selected_date, selected_time, tic_count, seat_list, total_cost, customer_id, cursor)

generate_random_transactions(cursor)


foodList = [
    ("Burger", 5.2, 10),
    ("Coke", 2.5, 10),
    ("Popcorn", 7.0, 10),
    ("HotDog", 8.0, 10),
    ("Cake", 9.0, 10),
    ("Fries", 8.0, 10),
    ("Candy", 7.0, 10),
    ("Chocolate", 6.0, 10),
    ("Sprite", 7.0, 10),
    ("Nachos", 8.0, 10)
]

def populate_food_orders(cursor):
    order_count = 100
    customer_count = 100
    ticket_count = 100
    
    for _ in range(order_count):
        order_id = None  # Auto-incremented primary key
        
        # Select a random customer
        user_id = f"cust{random.randint(0, customer_count-1)}"
        
        # Select a random ticket
        ticket_id = random.randint(1, ticket_count)
        
        # Insert the record into food_orders table
        cursor.execute("INSERT INTO food_orders (user_id, ticket_id) VALUES (?, ?)", (user_id, ticket_id))
        
        # Get the auto-generated order_id
        order_id = cursor.lastrowid
        
        # Randomly generate the number of food items for the order
        num_items = random.randint(1, 5)
        
        # Select random food items and quantities
        food_items = random.sample(foodList, num_items)
        quantities = [random.randint(1, 5) for _ in range(num_items)]
        
        # Insert the food order items into food_order_items table
        for i in range(num_items):
            food_name, _, _ = food_items[i]
            quantity = quantities[i]
            
            cursor.execute("INSERT INTO food_order_items (order_id, food_name, quantity) VALUES (?, ?, ?)",
                           (order_id, food_name, quantity))

populate_food_orders(cursor)


# Populating food_orders and food_order_items tables

#sql = "INSERT INTO hall (capacity, isAccessible) VALUES (?, ?)"
#data = (150,0)
#cursor.execute(sql, data)

#sql = "INSERT INTO hall (capacity, isAccessible) VALUES (?, ?)"
#data = (150,1)
#cursor.execute(sql, data)
# Commit the transaction
conn.commit()

# Close the database connection
conn.close()
