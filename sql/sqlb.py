__author__ = 'ariel'

# import the sqlite3 library
import sqlite3

# Create a new database if the database doesn't already exist
conn = sqlite3.connect("new.db")

# get a cursor object used to execute SQL commands
cursor = conn.cursor()

# Insert data
cursor.execute("INSERT INTO population VALUES ('New York City', 'NY', 82000000)")
cursor.execute("INSERT INTO population values ('San Francisco', 'CA', 800000)")

# Commit changes
conn.commit()

# Close connection
conn.close()