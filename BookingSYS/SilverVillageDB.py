import sqlite3

# Connect to the database
conn = sqlite3.connect('SilverVillageUserAcc.db')

# Get a cursor object
cursor = conn.cursor()

# Create a new table in the database
cursor.execute('''CREATE TABLE IF NOT EXISTS account 
                 (userID TEXT PRIMARY KEY,
                  password TEXT,
                  accType TEXT,
                  suspend BOOLEAN)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS userProfile 
                 (userID TEXT,
                  name TEXT,
                  DOB INT,
                  accType TEXT,
                  suspend BOOLEAN,
                  FOREIGN KEY(userID) REFERENCES account(userID))''')

cursor.execute('''CREATE TABLE IF NOT EXISTS movies 
                 (movieID TEXT PRIMARY KEY,
                  movieName TEXT,
                  timeSlot TEXT)''')


cursor.execute('''CREATE TABLE IF NOT EXISTS hall 
                 (hallName TEXT PRIMARY KEY,
                 rows INT,
                 columns INT,
                capacity INT,
                isAvailable BOOLEAN)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS hallshowtime 
                (hallName TEXT,
                showtime INT,
                isAvailable BOOLEAN,
                date DATE,
                PRIMARY KEY(hallName, showtime, date),
                FOREIGN KEY(hallName) REFERENCES hall(hallName))''')
#manager test
cursor.execute('''CREATE TABLE IF NOT EXISTS movie
                 (movieName TEXT,
                  genre TEXT,
                  showtime INT,
                  hallName TEXT,
                  startdate DATE,
                  enddate DATE,
                  isAvailable BOOLEAN,
                  PRIMARY KEY(movieName, showtime),
                  FOREIGN KEY(hallName) REFERENCES hallshowtime(hallName),
                  FOREIGN KEY(showtime) REFERENCES hallshowtime(showtime)
                  )''')

cursor.execute('''CREATE TABLE IF NOT EXISTS seat 
                (seat_No TEXT,
                hallName TEXT,
                showtime INT,
                date DATE,
                isAvailable BOOLEAN,
                PRIMARY KEY (seat_No, hallName, showtime, date)
                FOREIGN KEY (hallName) REFERENCES hall(hallName),
                FOREIGN KEY (showtime, date) REFERENCES hall(showtime, date))''')

cursor.execute('''CREATE TABLE IF NOT EXISTS food 
                 (foodName TEXT PRIMARY KEY,
                  price DECIMAL,
                  quantity INT,
                  isAvailable BOOLEAN)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS ticketType 
                 (type TEXT PRIMARY KEY,
                  price DECIMAL,
                 isAvailable BOOLEAN)''')



cursor.execute('''CREATE TABLE IF NOT EXISTS report 
                 (seat_ID INT PRIMARY KEY,
                  hall_ID INT
                  seatNumber TEXT,
                  isAvailable BOOLEAN)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS ticket 
                 (ticket_ID INTEGER PRIMARY KEY AUTOINCREMENT,
                  userID TEXT,
                  movieName TEXT,
                  hallName TEXT,
                  seat_No TEXT,
                  showtime INT,
                  date DATE,
                  type TEXT,
                  price DECIMAL,
                  FOREIGN KEY(userID) REFERENCES hallshowtime(userID),
                  FOREIGN KEY(movieName) REFERENCES movie(movieName),
                  FOREIGN KEY (hallName) REFERENCES hall(hallName),
                  FOREIGN KEY (seat_No) REFERENCES seat(seat_No),
                  FOREIGN KEY(showtime) REFERENCES hallshowtime(showtime),
                  FOREIGN KEY(type) REFERENCES ticketType(type))''')

cursor.execute('''CREATE TABLE IF NOT EXISTS food_orders (
               order_id INTEGER PRIMARY KEY AUTOINCREMENT,
               user_id TEXT,
               ticket_id INTEGER,
               FOREIGN KEY (user_id) REFERENCES account (userID)
               )''')

cursor.execute('''CREATE TABLE IF NOT EXISTS food_order_items (
               order_item_id INTEGER PRIMARY KEY AUTOINCREMENT,
               order_id INTEGER,
               food_name TEXT,
               quantity INTEGER,
               FOREIGN KEY (order_id) REFERENCES food_orders (order_id),
               FOREIGN KEY (food_name) REFERENCES food (foodName)
               )''')





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
                (movieName TEXT PRIMARY KEY,
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
                FOREIGN KEY (seat_ID, date) REFERENCES seat(seat_ID, date),
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
