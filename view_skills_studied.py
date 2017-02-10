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

cursor = db.cursor()
skill_name = var = raw_input("Enter Skill: ")
skill_status = ""



cursor.execute('''INSERT INTO skills(skill_name, skill_status)

                  VALUES(?,?)''', (skill_name, skill_status))

cursor.execute('''SELECT id, skill_name, skill_status FROM skills''')
user1 = cursor.fetchone() 
print user1

skill_status = var = raw_input("Enter Status(Whether Studied or Not Studied): ")


cursor.execute('''UPDATE skills SET skill_status = ? WHERE skill_name = ? ''',
 (skill_status, skill_name))

cursor.execute('''SELECT id, skill_name, skill_status FROM skills''')
user2 = cursor.fetchone()
print user2






