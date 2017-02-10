import sqlite3

conn = sqlite3.connect('skills.db')

cursor = conn.execute("SELECT id, skill_name, skill_status  from skills")
for row in cursor:
	if row[2] == 'studied':
		print "you've studied ", row[1];
	else: 
		print "You've not studied", row[1];
		
conn.close()
