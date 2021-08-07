#!/usr/bin/python3
"""
This script takes in arguments and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument.
But this time, this is safe from MySQL injections!
"""
import MySQLdb
from sys import argv


if __name__ == "__main__":
    db = MySQLdb.connect(host='localhost', port=3306,
                         user=argv[1], passwd=argv[2], db=argv[3])
    curs = db.cursor()
    cmd = "SELECT * from states WHERE name like %s ORDER BY `id` ASC"
    curs.execute(cmd, (argv[4],))
    data = curs.fetchall()
    for row in data:
        print(row)
    curs.close()
    db.close()
