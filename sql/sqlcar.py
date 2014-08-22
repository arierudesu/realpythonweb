__author__ = 'ariel'

# import the sqlite3 library
import sqlite3

# Create a new database if the database doesn't already exist
conn = sqlite3.connect("cars.db")

# get a cursor object used to execute SQL commands
cursor = conn.cursor()

# Create a table
cursor.execute("""CREATE TABLE inventory
                (Make TEXT, Model TEXT, Quantity INT)
                """)

# Close database connection
conn.close()
