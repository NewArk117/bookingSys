import sqlite3

# Connect to the database
conn = sqlite3.connect('SilverVillageUserAcc.db')

# Get a cursor object
cursor = conn.cursor()

# Create a new table in the database
#admin
cursor.execute('''CREATE TABLE IF NOT EXISTS admin 
                 (userID TEXT PRIMARY KEY,
                  userName TEXT,
                  password TEXT)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS customer 
                 (userID TEXT PRIMARY KEY,
                  userName TEXT,
                  password TEXT)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS userProfile 
                 (userID TEXT PRIMARY KEY,
                  name TEXT,
                  DOB TEXT,
                  accType TEXT)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS movies 
                 (movieID TEXT PRIMARY KEY,
                  movieName TEXT,
                  timeSlot TEXT)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS food 
                 (foodName TEXT PRIMARY KEY,
                  price DECIMAL,
                  quantity INT)''')


# Commit the transaction
conn.commit()

# Close the database connection
conn.close()