#!/usr/bin/python3
"""
This script takes in an argument and displays all values
in the states table of hbtn_0e_0_usa where name matches the argument.
"""
import MySQLdb
from sys import argv


if __name__ == "__main__":
    db = MySQLdb.connect(host='localhost', port=3306,
                         user=argv[1], passwd=argv[2], db=argv[3])
    curs = db.cursor()
    curs.execute("SELECT * from states WHERE name like '{}' ORDER BY `id` ASC".
                 format(argv[4]))
    data = curs.fetchall()
    for row in data:
        if row[1] == argv[4]:
            print(row)
    curs.close()
    db.close()
