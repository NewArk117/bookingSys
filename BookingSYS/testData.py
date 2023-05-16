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
    start_date = datetime.date(1975, 1, 1)  # specify the starting date
    end_date = datetime.date(2000, 5, 7)  # specify the ending date
    dobList = []
    for i in range(100):
        delta = end_date - start_date  # calculate the time delta between the start and end dates
        random_day = random.randrange(delta.days)  # generate a random number of days
        random_date = start_date + datetime.timedelta(days=random_day)  # add the random number of days to the start date
        dobList.append(random_date)

    return dobList

#Generate random DOB for staff profile
def randomDateStaff():
    start_date = datetime.date(1975, 1, 1)  # specify the starting date
    end_date = datetime.date(2000, 5, 7)  # specify the ending date
    dobList = []
    for i in range(15):
        delta = end_date - start_date  # calculate the time delta between the start and end dates
        random_day = random.randrange(delta.days)  # generate a random number of days
        random_date = start_date + datetime.timedelta(days=random_day)  # add the random number of days to the start date
        dobList.append(random_date)

    return dobList

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
sql = "INSERT INTO account (userID, userName, password,permission) VALUES (?, ?, ?, ?)"
for i in range(10):  
    if i == 0:
        data = ("owner1", "owner", "password","cinemaOwner")
        cursor.execute(sql, data) 
    elif i == 1:
        data = ("manager1", "manager", "password", "cinemaManager")
        cursor.execute(sql, data) 
    elif i == 2:
        data = ("admin1", "admin", "password", "sysAdmin")
        cursor.execute(sql, data) 
    elif i == 3:
        data = ("customerTest", "customer", "password", "customer")
        cursor.execute(sql, data) 
    elif i == 4 or i == 5 or i == 6 or i == 7 or i == 8:
        data = ("manager"+ str(i-2), someStaff[i], someStaffPassword[i], "cinemaManager")
        cursor.execute(sql, data) 
    else:
        data = ("admin"+ str(i-7), someStaff[i],someStaffPassword[i],"sysAdmin")
        cursor.execute(sql, data) 

    
# Insert 100 customer into the "account" table
someCust = randomCust()
someCustPassword = randomCustPassword()
sql = "INSERT INTO account (userID, userName, password,permission) VALUES (?, ?, ?, ?)"
for i in range(100):  
    data = ("cust"+str(i), someCust[i], someCustPassword[i],"customer")

    cursor.execute(sql, data)

# Insert random profiles for staff into the "User profile"
someDates1 = randomDateStaff()
staffName = ["Gianna Hess", "Ryan Velasquez", "Alexander OlsenMoses", "FlowersGiada",
             "Vincent Gregory", "Velazquez Sydnee", "Nelson Isabell", "Murphy Ashly", "Pruitt Kelsey",
             "Long Antony", "Hester Carla", "Woods Tess", "Davidson Tanya", "Rogers Mohammad", "Kerr Jackson"]
sql = "INSERT INTO userProfile (userID, name, DOB, accType) VALUES (?, ?, ?, ?)"
for i in range(10):  
    if i == 0:
        data = ("owner1", staffName[i], someDates1[i],"cinemaOwner")
        cursor.execute(sql, data) 
    elif i == 1:
        data = ("manager1", staffName[i], someDates1[i], "cinemaManager")
        cursor.execute(sql, data) 
    elif i == 2:
        data = ("admin1", staffName[i], someDates1[i], "sysAdmin")
        cursor.execute(sql, data) 
    elif i == 3:
        data = ("customerTest", staffName[i], someDates1[i], "customer")
        cursor.execute(sql, data) 
    elif i == 4 or i == 5 or i == 6 or i == 7 or i == 8:
        data = ("manager"+ str(i-2), staffName[i], someDates1[i], "cinemaManager")
        cursor.execute(sql, data) 
    else:
        data = ("admin"+ str(i-7), staffName[i],someDates1[i],"sysAdmin")
        cursor.execute(sql, data) 

# Insert random profiles for customer into the "User profile"
someDates2 = randomDateCust()
custName = randomNameCust()
sql = "INSERT INTO userProfile (userID, name, DOB, accType) VALUES (?, ?, ?, ?)"
for i in range(100):  
    data = ("cust"+str(i), custName[i], someDates2[i],"customer")

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
        sql2 = "INSERT INTO movie (movieName, genre, showtime, hallName, startdate, enddate) VALUES (?, ?, ?,?, ? ,?)"
        data2 = (name, genre, time, hall, startDate, endDate)
        cursor.execute(sql2, data2)
        for date in datelist:
            sql3 = "UPDATE hallshowtime SET isAvailable = ? WHERE hallName = ? AND showtime = ? AND date = ?"
            data3 = (0, hall, time, date)
            cursor.execute(sql3, data3)

hallList = ["Hall-1", "Hall-2", "Hall-3", "Hall-4", "Hall-5"]
movieList = [["Saw", "Thriller","Hall-1"], ["James Bond","Action","Hall-2" ],["Toy Story", "Family", "Hall-3"], ["Jumanji", "Adventure", "Hall-4"],  ["Avengers", "Action", "Hall-5"]]

for x in hallList:
    addHall(x, 5, 6, cursor)    

for x in movieList:
    addMovie(x[0], x[1], x[2], cursor)


#add food
def addFood( name, price, quantity, cursor):
    # Insert a new record into the account table
    sql = "INSERT INTO food (foodName, price, quantity) VALUES (?, ?, ?)"
    data = (name, price, quantity)
    cursor.execute(sql, data)

addFood("Burger", 5.2, 10 , cursor)
addFood("Coke", 2.5, 10, cursor)
addFood("Popcorn", 6.0, 10, cursor)

def addTicketType(name, price, cursor):
    sql = "INSERT INTO ticketType (type, price) VALUES (?, ?)"
    data = (name, price)
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

purchaseTic("Saw ", "Thriller" ,"Hall-1" ,"2023-05-01", 1330 ,7,[['B-4', 'Adult', 12], ['C-4', 'Adult', 12], ['D-4', 'Adult', 12], ['D-5', 'Adult', 12], ['C-6', 'Adult', 12], ['C-3', 'Adult', 12], ['B-3', 'Adult', 12]] ,84 ,"customerTest", cursor)
purchaseTic("James Bond" ,"Action ", "Hall-2",  "2023-06-20", 1730, 7, [['B-4', 'Adult', 12], ['C-4', 'Child', 10], ['C-2', 'Adult', 12], ['B-2', 'Adult', 12], ['B-3', 'Child', 10], ['D-3', 'Child', 10], ['E-4', 'Senior', 9]], 75 ,"customerTest",cursor)
    #conn.commit()
    #conn.close()

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
