__author__ = 'ariel'

# import sqlite3 library
import sqlite3

# open db connection
with sqlite3.connect("cars.db") as connection:
    c = connection.cursor()

    # Create sql dictionary
    sql = {
        'mustang count': "select count(make) from orders where model = 'Mustang'",
        'falcon count': "select count(make) from orders where model = 'Falcon'",
        'fiesta count': "select count(make) from orders where model = 'Fiesta'",
        'civic count': "select count(make) from orders where model = 'Civic'",
        'jazz count': "select count(make) from orders where model = 'Jazz'"
    }

    for keys, values in sql.iteritems():

        c.execute(values)

        total = c.fetchone()

        print keys + ":", total[0]