#!/usr/bin/python3
"""
This script takes in the name of a state as an argument and lists all
cities of that state, using the database hbtn_0e_4_usa.
"""


import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host='localhost', port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])
    curs = db.cursor()
    cmd = "SELECT cities.id, cities.name, states.name FROM cities \
    INNER JOIN states ON cities.state_id = states.id \
    WHERE states.name = %s \
    ORDER BY `id` ASC"
    curs.execute(cmd, (argv[4],))
    data = curs.fetchall()
    cities = []
    for row in data:
        cities.append(row[1])
    print(", ".join(cities))
    curs.close()
    db.close()
