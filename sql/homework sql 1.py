__author__ = 'ariel'

import sqlite3

# Generate database connection
with sqlite3.connect("cars.db") as connection:
    c = connection.cursor()

    # Fill the tuple with data
    cars = [
        ('Ford', 'Mustang', 2),
        ('Ford', 'Falcon', 5),
        ('Ford', 'Fiesta', 10),
        ('Honda', 'Civic', 4),
        ('Honda', 'Jazz', 23)
    ]

    # Insert the data in the database
    try:
        c.executemany('INSERT into inventory values(?, ?, ?)', cars)
    except sqlite3.OperationalError:
        print 'Error al insertar datos'