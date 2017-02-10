import sqlite3

conn = sqlite3.connect('skills.db')

cursor = conn.execute("SELECT id, skill_name,status from skills")
for row in cursor:
   print ("ID = ", row[0])
   print ("SKILL NAME = ", row[1])
   print ("SKILL STATUS = ", row[2])


conn.close()