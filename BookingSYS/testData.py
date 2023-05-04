import sqlite3
import random
import string

def randomUser():
    random_names = []
    random_numbers = []
    for i in range(100):
        random_numbers.append(str(random.randrange(1, 1000)).zfill(3))
    
    for i in range(100):
        random_string = ''.join(random.choice(string.ascii_lowercase) for _ in range(random.randint(5, 8)))
        random_names.append(random_string)
    
    combined_list = [str(elem1) + elem2 for elem1, elem2 in zip(random_names, random_numbers)]

    return combined_list

def randomPassword():
    random_password = []
    for i in range(100):
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
sql = "INSERT INTO admin (userID, userName, password) VALUES (?, ?, ?)"
data = ("000001", "admin", "password")
cursor.execute(sql, data)

# Insert a 100 record into the "customers" table
someUser = randomUser()
somePassword = randomPassword()
sql = "INSERT INTO customer (userID, userName, password) VALUES (?, ?, ?)"
for i in range(100):  
    data = (i, someUser[i], somePassword[i])

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
