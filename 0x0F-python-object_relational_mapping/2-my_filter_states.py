#!/usr/bin/python3
"""takes in an argument and displays all values in the states table"""
if __name__ == '__main__':
    import MySQLdb
    import sys

    agmt = sys.argv[4]

    db = MySQLdb.connect(host='localhost', port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])

    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE name='{}' "
                   " COLLATE Latin1_General_cs ORDER BY states.id ASC"
                   .format(agmt))
    result = cursor.fetchall()

    for i in result:
        print(i)

    cursor.close()
    db.close()
