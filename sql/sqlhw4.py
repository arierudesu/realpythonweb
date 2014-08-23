__author__ = 'ariel'

import sqlite3

with sqlite3.connect("cars.db") as connection:
    c = connection.cursor()

    c.execute("select * from inventory")

    rows = c.fetchall()

    for r in rows:

        print r[0], r[1], "\n", r[2]

        c.execute("select count(order_date) from orders where make = ? and model = ?",
                  (r[0], r[1]))

        oc = c.fetchone()[0]

        print oc
