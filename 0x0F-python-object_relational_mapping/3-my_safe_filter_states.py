#!/usr/bin/python3
"""
 avoid SQL injection
"""
if __name__ == '__main__':
    import MySQLdb
    import sys

    agmt = sys.argv[4]

    db = MySQLdb.connect(host='localhost', port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])

    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE name= %s COLLATE "
                   "Latin1_General_cs ORDER BY id ASC",(agmt,))
    result = cursor.fetchall()

    for i in result:
        print(i)

    cursor.close()
    db.close()
