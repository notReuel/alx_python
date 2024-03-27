import MySQLdb
from sys import argv

mysql_username = argv[1]
mysql_password = argv[2]
mysql_database = argv[3]
stateName = argv[4] 

dbconnect = MySQLdb.connect(host='localhost', port=3306, user=mysql_username, passwd=mysql_password, db=mysql_database)

cursor = dbconnect.cursor()

cursor.execute('SELECT * FROM states WHERE BINARY name LIKE %s '.format(stateName + '%'))
states = cursor.fetchall()

for state in states:
    print(state)

cursor.close()

dbconnect.close()