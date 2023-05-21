import sqlite3
import datetime
#GUI Imports
from PyQt5.QtWidgets import QMessageBox, QListWidgetItem, QGridLayout, QWidget, QLabel, QTextEdit
from PyQt5.QtCore import Qt
#Import links to different scripts in Boundary
from datetime import datetime, timedelta
import sys 
sys.path.append('./Boundary')

class owner:
    def viewHourlyTic(self)->str:
        text = "This is hourly tic"
        itemname = "Hourly Number of Ticket"
        # Connect to the database
        conn = sqlite3.connect('SilverVillageUserAcc.db')
        cursor = conn.cursor()

        # Available hours
        available_hours = [1330, 1530, 1730, 1930, 2130]

        # Initialize a dictionary to store the ticket counts
        ticket_counts = {hour: 0 for hour in available_hours}

        # Query the database to get the ticket counts
        for hour in available_hours:
            cursor.execute('''SELECT COUNT(*) FROM ticket WHERE showtime = ?''', (hour,))
            result = cursor.fetchone()
            ticket_counts[hour] = result[0]

        # Generate the report string
        report = "Number of tickets sold by the hour:\n===============================\n"
        for hour, count in ticket_counts.items():
            report += f"{hour}: {count}\n"

        conn.close()

        return report, itemname
    
    def viewHourlyRev(self)->str:
        text = "This is hourly rev"
        itemname = "Hourly Revenue"
        # Connect to the database
        conn = sqlite3.connect('SilverVillageUserAcc.db')
        cursor = conn.cursor()

        # Define the showtimes
        showtimes = [1330, 1530, 1730, 1930, 2130]

        # Query the database to get the revenue for each showtime from ticket sales
        ticket_revenue_query = '''SELECT showtime, SUM(price) FROM ticket
                                WHERE showtime IN (?, ?, ?, ?, ?)
                                GROUP BY showtime'''
        cursor.execute(ticket_revenue_query, showtimes)
        ticket_results = cursor.fetchall()

        # Query the database to get the revenue for each showtime from food orders
        food_revenue_query = '''SELECT t.showtime, SUM(f.price * foi.quantity) FROM ticket t
                                JOIN food_orders fo ON t.ticket_ID = fo.ticket_id
                                JOIN food_order_items foi ON fo.order_id = foi.order_id
                                JOIN food f ON foi.food_name = f.foodName
                                WHERE t.showtime IN (?, ?, ?, ?, ?)
                                GROUP BY t.showtime'''
        cursor.execute(food_revenue_query, showtimes)
        food_results = cursor.fetchall()

        # Generate the report string
        report = "Hourly Revenue Report:\n"
        for showtime in showtimes:
            ticket_revenue = next((revenue for time, revenue in ticket_results if time == showtime), 0)
            food_revenue = next((revenue for time, revenue in food_results if time == showtime), 0)
            total_revenue = ticket_revenue + food_revenue
            report += f"{showtime}: Revenue - ${total_revenue}\n"
        
        return report, itemname
    
    def viewDailyTic(self)->str:
        text = "This is Daily tic"
        itemname = "Daily Number of Ticket"
        # Connect to the database
        conn = sqlite3.connect('SilverVillageUserAcc.db')
        cursor = conn.cursor()

        # Query the database to get the ticket counts by date
        cursor.execute('''SELECT date, COUNT(*) FROM ticket GROUP BY date''')
        results = cursor.fetchall()

        # Generate the report string
        report = "Number of tickets sold each day:\n===============================\n"
        for row in results:
            date = row[0]
            count = row[1]
            report += f"{date}: {count}\n"
        return report, itemname
    
    def viewDailyRev(self)->str:
        text = "This is Daily rev"
        itemname = "Daily Revenue"
        # Connect to the database
        conn = sqlite3.connect('SilverVillageUserAcc.db')
        cursor = conn.cursor()

        # Define the showtimes
        showtimes = [1330, 1530, 1730, 1930, 2130]

        # Query the database to get the revenue for each date from ticket sales
        ticket_revenue_query = '''SELECT date, SUM(price) FROM ticket
                                WHERE showtime IN (?, ?, ?, ?, ?)
                                GROUP BY date'''
        cursor.execute(ticket_revenue_query, showtimes)
        ticket_results = cursor.fetchall()

        # Query the database to get the revenue for each date from food orders
        food_revenue_query = '''SELECT t.date, SUM(f.price * foi.quantity) FROM ticket t
                                JOIN food_orders fo ON t.ticket_ID = fo.ticket_id
                                JOIN food_order_items foi ON fo.order_id = foi.order_id
                                JOIN food f ON foi.food_name = f.foodName
                                WHERE t.showtime IN (?, ?, ?, ?, ?)
                                GROUP BY t.date'''
        cursor.execute(food_revenue_query, showtimes)
        food_results = cursor.fetchall()

        # Generate the report string
        report = "Daily Revenue Report:\n"
        for row in ticket_results:
            date = row[0]
            ticket_revenue = row[1]
            food_revenue = next((revenue for date_, revenue in food_results if date_ == date), 0)
            total_revenue = ticket_revenue + food_revenue
            report += f"Date {date}: Revenue - ${total_revenue}\n"
        return report, itemname
    
    def viewWeeklyTic(self)->str:
        text = "This is Weekly tic"
        itemname = "Weekly Number of Ticket"

        # Connect to the database
        conn = sqlite3.connect('SilverVillageUserAcc.db')
        cursor = conn.cursor()

        # Find the hall with the latest date and the hall with the earliest start date
        cursor.execute('''SELECT MAX(enddate), MIN(startdate) FROM movie''')
        latest_date, earliest_start_date = cursor.fetchone()

        # Calculate the start and end dates for the report period
        end_date = datetime.strptime(latest_date, '%Y-%m-%d').date()
        start_date = datetime.strptime(earliest_start_date, '%Y-%m-%d').date()

        # Query the database to get the ticket counts by week
        cursor.execute('''SELECT strftime('%Y-%W', date), COUNT(*) FROM ticket
                        WHERE date >= ? AND date <= ?
                        GROUP BY strftime('%Y-%W', date)''',
                    (start_date, end_date))
        results = cursor.fetchall()

        # Generate the report string
        report = "Ticket Sales Report - Number of tickets sold each week:\n"
        for row in results:
            week = row[0]
            count = row[1]
            # Get the start and end dates of the week based on the week number
            year, week = week.split('-')
            start_of_week = datetime.strptime(year + '-' + week + '-1', '%Y-%W-%w').date()
            end_of_week = start_of_week + timedelta(days=6)

            # Append the week number and date range to the report
            report += f"Week {week} ({start_of_week} to {end_of_week}): {count} tickets\n"

        return report, itemname
    

    def viewWeeklyRev(self) -> str:
        text = "This is Weekly rev"
        itemname = "Weekly Revenue"

        conn = sqlite3.connect('SilverVillageUserAcc.db')
        cursor = conn.cursor()

        # Find the hall with the latest date and the hall with the earliest start date
        latest_date_query = '''SELECT MAX(date) FROM hallshowtime'''
        cursor.execute(latest_date_query)
        latest_date = cursor.fetchone()[0]

        earliest_start_date_query = '''SELECT MIN(startdate) FROM movie'''
        cursor.execute(earliest_start_date_query)
        earliest_start_date = cursor.fetchone()[0]

        # Query the database to get the revenue for each week from ticket sales
        ticket_revenue_query = '''SELECT strftime('%Y-%W', date), SUM(price) FROM ticket
                                WHERE date >= ? AND date <= ?
                                GROUP BY strftime('%Y-%W', date)'''
        cursor.execute(ticket_revenue_query, (earliest_start_date, latest_date))
        ticket_results = cursor.fetchall()

        # Query the database to get the revenue for each week from food orders
        food_revenue_query = '''SELECT strftime('%Y-%W', t.date), SUM(f.price * foi.quantity) FROM ticket t
                                JOIN food_orders fo ON t.ticket_ID = fo.ticket_id
                                JOIN food_order_items foi ON fo.order_id = foi.order_id
                                JOIN food f ON foi.food_name = f.foodName
                                WHERE t.date >= ? AND t.date <= ?
                                GROUP BY strftime('%Y-%W', t.date)'''
        cursor.execute(food_revenue_query, (earliest_start_date, latest_date))
        food_results = cursor.fetchall()

        # Generate the report string
        report = "Weekly Revenue Report:\n"
        for row in ticket_results:
            week = row[0]
            ticket_revenue = row[1]
            food_revenue = next((revenue for week_, revenue in food_results if week_ == week), 0)
            total_revenue = ticket_revenue + food_revenue

            # Calculate the date range for the week
            year, week_num = map(int, week.split('-'))
            start_date = datetime.strptime(f'{year}-W{week_num-1}-1', "%Y-W%W-%w").date() + timedelta(days=1)
            end_date = start_date + timedelta(days=6)

            report += f"Week {week} ({start_date} - {end_date}): Revenue - ${total_revenue}\n"

        return report, itemname

