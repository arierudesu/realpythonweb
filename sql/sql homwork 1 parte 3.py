__author__ = 'ariel'

import sqlite3

with sqlite3.connect("cars.db") as connection:
    c = connection.cursor()

    # select only ford models
    c.execute("select * from inventory where Make = 'Ford'")
    ford = c.fetchall()

    for l in ford:
        print l[0], l[1], l[2]
