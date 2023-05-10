import sqlite3

# Connect to the database
conn = sqlite3.connect('SilverVillageUserAcc.db')

# Get a cursor object
cursor = conn.cursor()

# Create a new table in the database
cursor.execute('''CREATE TABLE IF NOT EXISTS account 
                 (userID TEXT PRIMARY KEY,
                  userName TEXT,
                  password TEXT,
                  permission TEXT)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS userProfile 
                 (userID TEXT PRIMARY KEY,
                  name TEXT,
                  DOB TEXT,
                  accType TEXT)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS movies 
                 (movieID TEXT PRIMARY KEY,
                  movieName TEXT,
                  timeSlot TEXT)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS hall 
                 (hallName TEXT PRIMARY KEY,
                 rows INT,
                 columns INT,
                  capacity INT,
                  isAccessible BOOLEAN)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS seat 
                (seat_No TEXT PRIMARY KEY,
                hallName TEXT,
                isAvailable BOOLEAN,
                FOREIGN KEY (hallName) REFERENCES hall(hallName))''')

cursor.execute('''CREATE TABLE IF NOT EXISTS food 
                 (foodName TEXT PRIMARY KEY,
                  price DECIMAL,
                  quantity INT)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS ticketType 
                 (type TEXT PRIMARY KEY,
                  price DECIMAL)''')



cursor.execute('''CREATE TABLE IF NOT EXISTS report 
                 (seat_ID INT PRIMARY KEY,
                  hall_ID INT
                  seatNumber TEXT,
                  isAvailable BOOLEAN)''')




# Commit the transaction
conn.commit()

# Close the database connection
conn.close()

"""
cursor.execute('''CREATE TABLE IF NOT EXISTS hall 
                (hall_ID INT,
                capacity INT,
                isAccessible BOOLEAN)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS movie
                (movieName TEXT PRIMARY KEY AUTOINCREMENT,
                genre TEXT)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS ticketType 
                (type TEXT PRIMARY KEY AUTOINCREMENT,
                price DECIMAL)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS fb
                (itemName TEXT PRIMARY KEY,
                price DECIMAL,
                quantity INT)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS seat 
                (seat_ID INT PRIMARY KEY,
                hall_ID INTEGER,
                isAvailable BOOLEAN,
                FOREIGN KEY (hall_ID) REFERENCES hall(hall_ID))''')

cursor.execute('''CREATE TABLE IF NOT EXISTS showtime 
                (showtime_ID INTEGER PRIMARY KEY AUTOINCREMENT,
                hall_ID INTEGER,
                movieName TEXT,
                startTime TEXT,
                endTime TEXT,
                date DATE,
                FOREIGN KEY (hall_ID) REFERENCES hall(hall_ID),
                FOREIGN KEY (movieName) REFERENCES movie(movieName))''')


cursor.execute('''CREATE TABLE IF NOT EXISTS ticket 
                (ticket_ID INTEGER PRIMARY KEY AUTOINCREMENT,
                movieName TEXT,
                hall_ID INTEGER,
                seat_ID INTEGER,
                showtime_ID INTEGER,
                type TEXT,
                FOREIGN KEY (hall_ID) REFERENCES hall(hall_ID),
                FOREIGN KEY (movieName) REFERENCES movie(movieName),
                FOREIGN KEY (seat_ID) REFERENCES seat(seat_ID),
                FOREIGN KEY (showtime_ID) REFERENCES showtime(showtime_ID),
                FOREIGN KEY (type) REFERENCES ticketType(type))''')

cursor.execute('''CREATE TABLE IF NOT EXISTS purchases 
                (purchases_ID INTEGER PRIMARY KEY AUTOINCREMENT,
                user_ID INTEGER,
                itemName TEXT,
                ticket_ID INTEGER,
                totalCost DECIMAL,
                FOREIGN KEY (user_ID) REFERENCES account(user_ID),
                FOREIGN KEY (itemName) REFERENCES fb(itemName),
                FOREIGN KEY (ticket_ID) REFERENCES ticket(ticket_ID))''')


cursor.execute('''CREATE TABLE IF NOT EXISTS report 
                (report_ID INTEGER PRIMARY KEY AUTOINCREMENT,
                purchases_ID INTEGER,
                total DECIMAL,
                FOREIGN KEY (purchases_ID) REFERENCES purchases(purchases_ID)    )''')

cursor.execute('''CREATE TABLE IF NOT EXISTS account 
                (user_ID INTEGER PRIMARY KEY AUTOINCREMENT,
                profile_ID INTEGER,
                userName TEXT,
                password TEXT,
                permission TEXT,
                FOREIGN KEY (profile_ID) REFERENCES userProfile(profile_ID))''')

cursor.execute('''CREATE TABLE IF NOT EXISTS userProfile 
                (profile_ID TEXT PRIMARY KEY,
                name TEXT,
                DOB TEXT,
                accType TEXT)''')                 

"""