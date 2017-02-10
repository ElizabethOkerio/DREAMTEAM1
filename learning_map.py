import sqlite3


"""db = sqlite3.connect('skills.db')
cursor = db.cursor()
cursor.execute('''
    CREATE TABLE skills(id INTEGER PRIMARY KEY, skill_name TEXT,
                       skill_status TEXT)
''')
db.commit()
db.close()
cursor = db.cursor()
skill_name = 'Coding'
skill_status= 'skilled'"""
db = sqlite3.connect('skills.db')
skill_name = var = raw_input("Enter Skill: ")
skill_status = ""
cursor = db.cursor()
cursor.execute('''INSERT INTO skills(skill_name, skill_status)
                  VALUES(?,?)''', (skill_name, skill_status))

skill_name = var = raw_input("Press enter to view skills: ")


db1 = cursor.execute('''SELECT id, skill_name FROM skills''')
for row in cursor:
   print ("ID = ", row[0])
   print ("SKILL NAME = ", row[1])
   

"""db1 = cursor.execute("SELECT id, skill_name,skill_status from skills")
for row in db1:
   print ("ID = ", row[0])
   print ("SKILL NAME = ", row[1])
   print ("SKILL STATUS = ", row[2])"""

skill_status = var = raw_input("Enter Status(Whether Studied or Not Studied): ")


db1 = cursor.execute('''UPDATE skills SET skill_status = ? WHERE skill_name = ? ''',
 (skill_status, skill_name))

skill_name = var = raw_input("Press enter to view skills with their status: ")

db1 = cursor.execute('''SELECT id, skill_name, skill_status FROM skills''')
for row in cursor:
   print ("ID = ", row[0])
   print ("SKILL NAME = ", row[1])
   print ("SKILL STATUS = ", row[2])

skill_name = var = raw_input("Press enter to view if skills are studied or not studied: ")

db1 = cursor.execute("SELECT id, skill_name, skill_status  from skills")
for row in cursor:
    if row[2] == 'studied':
        print "you've studied ", row[1]
    else:
        print "You've not studied", row[1]            
   
           

db.close()
