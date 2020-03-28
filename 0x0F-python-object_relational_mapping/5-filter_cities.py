#!/usr/bin/python3
"""
takes in the name of a state as an argument and lists all cities of that state
"""
if __name__ == '__main__':
    import MySQLdb
    import sys

    agmt = sys.argv[4]

    db = MySQLdb.connect(host='localhost', port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])

    cursor = db.cursor()
    cursor.execute("SELECT cities.name FROM cities JOIN states ON states.id ="
                   " cities.state_id WHERE states.name= %s COLLATE "
                   "Latin1_General_cs ORDER BY cities.id ASC", (agmt,))
    result = cursor.fetchall()

    print(', '.join(i[0] for i in result))

    cursor.close()
    db.close()
