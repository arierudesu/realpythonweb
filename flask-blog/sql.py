__author__ = 'ariel'

import sqlite3

# create a new database if doesn't exist
with sqlite3.connect("blog.db") as connection:
    c = connection.cursor()

    # create table
    c.execute("create table posts(title text, post text)")

    # insert dummy data
    c.execute('insert into posts values("Good", "I\'m good")')
    c.execute('insert into posts values("Well", "I\'m well")')
    c.execute('insert into posts values("Excellent", "I\'m Excelent")')
    c.execute('insert into posts values("Okay", "I\'m okay")')
