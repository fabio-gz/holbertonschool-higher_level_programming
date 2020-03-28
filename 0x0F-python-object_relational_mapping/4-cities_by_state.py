#!/usr/bin/python3
"""
lists all cities from the database hbtn_0e_4_usa
"""
if __name__ == '__main__':
    import MySQLdb
    import sys

    db = MySQLdb.connect(host='localhost', port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])

    cursor = db.cursor()
    cursor.execute("SELECT cities.id, cities.name, states.name FROM cities"
                   " JOIN states ON states.id=cities.state_id COLLATE "
                   "Latin1_General_cs ORDER BY cities.id ASC")
    result = cursor.fetchall()

    for i in result:
        print(i)

    cursor.close()
    db.close()
