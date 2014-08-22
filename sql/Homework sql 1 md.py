__author__ = 'ariel'

import sqlite3

with sqlite3.connect("cars.db") as connection:
    c = connection.cursor()

# Select all data from the db
    c.execute('select * from inventory')
    full_list = c.fetchall()

# Print data in screen
    for f in full_list:
        print f[0], f[1], f[2]

    print "\n UPDATED DATA \n"
# Update values
try:
    c.execute("update inventory set Quantity = 50 where Model = 'Falcon'")
    c.execute("update inventory set Quantity = 5 where Model = 'Jazz'")
except sqlite3.OperationalError:
     print "Error al actualizar la base de datos"

 # Get new data
c.execute('select * from inventory')
updated_list = c.fetchall()

# Print new data
for u in updated_list:
    print u[0], u[1], u[2]

connection.commit()
connection.close()