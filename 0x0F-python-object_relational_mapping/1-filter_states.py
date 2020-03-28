#!/usr/bin/python3
"""
 lists all states with a name starting with N
"""
if __name__ == '__main__':
    import MySQLdb
    import sys

    db = MySQLdb.connect(host='localhost', port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])

    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")
    result = cursor.fetchall()

    for i in result:
        print(i)

    cursor.close()
    db.close()
