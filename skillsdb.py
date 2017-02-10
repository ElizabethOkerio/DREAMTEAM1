import sqlite3
conn = sqlite3.connect('skills.db')

conn.execute("INSERT INTO skills(id,skill_name,skill_status) VALUES(10, 'PYTHON', 'STUDIED')");

conn.execute("INSERT INTO skills(id,skill_name,skill_status) VALUES(11, 'JAVA', 'NOTSTUDIED')");

conn.execute("INSERT INTO skills(id,skill_name,skill_status) VALUES(12, 'RUBY', 'STUDIED')");

conn.execute("INSERT INTO skills(id,skill_name,skill_status) VALUES(13, 'AJAX', 'NOTSTUDIED')");

conn.execute("INSERT INTO skills(id,skill_name,skill_status) VALUES(14, 'PHP', 'STUDIED')");

conn.close()