__author__ = 'ariel'

# import sqlite3 library
import sqlite3

# Generate the connection to the db
with sqlite3.connect("new.db") as connection:
    c = connection.cursor()

    try:
        # Create a new table
        c.execute("""create table regions(city TEXT, region text)""")

        # Fill the new db with data
        cities = [
                ('New York City', 'Northeast'),
                ('San Francisco', 'West'),
                ('Chicago', 'Midwest'),
                ('Houston', 'South'),
                ('Phoenix', 'West'),
                ('Boston', 'Northeast'),
                ('Los Angeles', 'West'),
                ('Houston', 'South'),
                ('Philadelphia', 'Northeast'),
                ('San Antonio', 'South'),
                ('San Diego', 'West'),
                ('Dallas', 'South'),
                ('San Jose', 'West'),
                ('Jacksonville', 'South'),
                ('Indianapolis', 'Midwest'),
                ('Austin', 'South'),
                ('Detroit', 'Midwest')
                ]

        c.executemany("insert into regions values(?, ?)", cities)

    except sqlite3.OperationalError:
        print "Ya existen la tabla con datos"
        print "\n"

    # Select all data from new table
    c.execute("select * from regions order by region asc")
    rows = c.fetchall()

    # Show all data in screen
    for r in rows:
        print r[0], r[1]

