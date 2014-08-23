__author__ = 'ariel'

# Import sqlite3 library
import sqlite3

# Open connection to db
with sqlite3.connect("new.db") as connection:
    c = connection.cursor()

    # Retrieve data
    c.execute("""select  population.city,
                         population.population,
                         regions.region
                 from population,
                      regions
                 where population.city = regions.city""")

    rows = c.fetchall()

    # show data in screen
    for r in rows:
        print r[0], r[1], r[2]
