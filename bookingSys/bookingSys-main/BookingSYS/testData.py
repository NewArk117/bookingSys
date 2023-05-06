import sqlite3
import random
import string

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

def randomCustPassword():
    random_password = []
    for i in range(100):
         # Define the possible characters to use in the password
        chars = string.ascii_letters + string.digits
        
        # Generate an 8-digit password
        password = ''.join(random.choice(chars) for i in range(8))
        random_password.append(password)
    return random_password

def randomStaff():
    random_names = []
    random_numbers = []
    for i in range(15):
        random_numbers.append(str(random.randrange(1, 1000)).zfill(3))
    
    for i in range(15):
        random_string = ''.join(random.choice(string.ascii_lowercase) for _ in range(random.randint(5, 8)))
        random_names.append(random_string)
    
    combined_list = [str(elem1) + elem2 for elem1, elem2 in zip(random_names, random_numbers)]

    return combined_list

def randomStaffPassword():
    random_password = []
    for i in range(15):
         # Define the possible characters to use in the password
        chars = string.ascii_letters + string.digits
        
        # Generate an 8-digit password
        password = ''.join(random.choice(chars) for i in range(8))
        random_password.append(password)
    return random_password

def movieData():
    timeSlot = ["0930","1245","1600","1915","2130","0045"]
    movieName = ["The Shawshank Redemption", "300BC", "Avatar", "Smile", "Truth or Dare"]
    combine = []
    for i in range(len(movieName)):
        for j in range(len(timeSlot)):
            combine.append((movieName[i],timeSlot[j]))
    return combine

# Connect to the database
conn = sqlite3.connect('SilverVillageUserAcc.db')

# Get a cursor object
cursor = conn.cursor()

# Insert a new record into the "admin" table

someStaff = randomStaff()
someStaffPassword = randomStaffPassword()
sql = "INSERT INTO account (userID, userName, password,permission) VALUES (?, ?, ?, ?)"
for i in range(15):  
    data = ("staff"+str(i), someStaff[i], someStaffPassword[i],"staff")

    cursor.execute(sql, data)

sql = "INSERT INTO account (userID, userName, password, permission) VALUES (?, ?, ?, ?)"
data = ("admin1", "admin", "password", "sysAdmin")
cursor.execute(sql, data)

sql = "INSERT INTO account (userID, userName, password, permission) VALUES (?, ?, ?, ?)"
data = ("manager1", "manager", "password", "cinemaManager")
cursor.execute(sql, data)

sql = "INSERT INTO account (userID, userName, password, permission) VALUES (?, ?, ?, ?)"
data = ("owner1", "owner", "password", "cinemaOwner")
cursor.execute(sql, data)

# Insert a 100 record into the "customers" table
someCust = randomCust()
someCustPassword = randomCustPassword()
sql = "INSERT INTO account (userID, userName, password,permission) VALUES (?, ?, ?, ?)"
for i in range(100):  
    data = ("cust"+str(i), someCust[i], someCustPassword[i],"customer")

    cursor.execute(sql, data)

# Insert random profiles into the "User profile"
sql = "INSERT INTO userProfile (userID, name, DOB, accType) VALUES (?, ?, ?, ?)"
data = ("staff1", "Sasuke Uchiha", "11121314", "DonkeyKong")
cursor.execute(sql, data)

# Insert a new record into the "movie" table
someMovie = movieData()
sql = "INSERT INTO movies (movieID, movieName, timeSlot) VALUES (?, ?, ?)"
for i in range(len(someMovie)):  
    data = (i, someMovie[i][0], someMovie[i][1])
    cursor.execute(sql, data)

# Commit the transaction
conn.commit()

# Close the database connection
conn.close()
