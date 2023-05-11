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
for i in range(15):  
    data = ("staff"+str(i), staffName[i], someDates1[i],"staff")

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
