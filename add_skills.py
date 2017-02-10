import sqlite3

conn = sqlite3.connect('my.db')
print "Opened database successfully";


cursor = conn.execute("SELECT id, name, address, salary  from my")
for row in cursor:
   if row[1] == 'Paul':
		print "you've studied ", row[2]
print "Operation done successfully";
conn.close()