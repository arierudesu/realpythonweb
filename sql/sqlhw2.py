__author__ = 'ariel'

# import sqlite3 library
import sqlite3

# generate connection to the db
with sqlite3.connect("cars.db") as connection:
    c = connection.cursor()

    # Create new table
    try:
        c.execute("""create table orders(make TEXT,
                                         model TEXT,
                                         order_date text )""")
    except sqlite3.OperationalError:
        print "Ya existe la tabla"
        print

    # Insert new data
    info = [
        ('Ford', 'Mustang', '2014-01-15'),
        ('Ford', 'Mustang', '2014-01-16'),
        ('Ford', 'Falcon', '2014-01-20'),
        ('Ford', 'Falcon', '2014-01-25'),
        ('Ford', 'Fiesta', '2014-03-21'),
        ('Ford', 'Fiesta', '2014-04-27'),
        ('Ford', 'Fiesta', '2014-05-29'),
        ('Ford', 'Fiesta', '2014-06-04'),
        ('Honda', 'Civic', '2014-01-18'),
        ('Honda', 'Civic', '2014-03-13'),
        ('Honda', 'Civic', '2014-04-05'),
        ('Honda', 'Jazz', '2014-04-05'),
        ('Honda', 'Jazz', '2013-11-05'),
        ('Honda', 'Jazz', '2013-12-10'),
        ('Ford', 'Fiesta', '2013-11-25')
    ]
    try:
        c.executemany("insert into orders values(?, ?, ?)", info)
        connection.commit()
    except sqlite3.OperationalError:
        print "No se pudo ingresar nueva data en la tabla"
        print

    c.execute("""select distinct inventory.Make,
                                 inventory.Model,
                                 inventory.Quantity,
                                 orders.order_date
                 from inventory, orders
                 where inventory.Make = orders.make
                   and inventory.Model = orders.model
                 order by inventory.Make asc""")

    rows = c.fetchall()

    for r in rows:
        print "Maker: " + r[0] + " | " " Model: " + r[1]
        print "Quantity: " + str(r[2])
        print "Order Date: " + r[3]
        print


