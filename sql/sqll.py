__author__ = 'ariel'

# Import sqlite3 library
import sqlite3

# Generate connection to the db
with sqlite3.connect("new.db") as connection:
    c = connection.cursor()

    # Joining data from multiple tables
    c.execute("""select distinct population.city,
                                 population.population,
                                 regions.region
                 from population,
                      regions
                 where population.city = regions.city
                 order by population.city asc""")

    rows = c.fetchall()

    for r in rows:
        print "City: " + r[0]
        print "Population: " + str(r[1])
        print "Region: " + r[2]
        print