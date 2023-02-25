import sqlite3

db = sqlite3.connect('sqlite_database')  # creates the database file if not created and then connects to it

cursor = db.cursor()  # Get a cursor object

# creates a table called python programming with the fields id, name, and grade
cursor.execute('''
    CREATE TABLE python_programming(id INTEGER PRIMARY KEY, name TEXT, grade INTEGER)
''')

db.commit()

# Create Values to insert into the table and then insert it. After that, commit it to the database
id1 = 55
name1 = "Carl Davis"
grade1 = 61
cursor.execute('''INSERT INTO python_programming(id, name, grade) VALUES(?,?,?)''', (id1, name1, grade1))

id2 = 66
name2 = "Dennis Fredrickson"
grade2 = 88
cursor.execute('''INSERT INTO python_programming(id, name, grade) VALUES(?,?,?)''', (id2, name2, grade2))

id3 = 77
name3 = "Jane Richards"
grade3 = 78
cursor.execute('''INSERT INTO python_programming(id, name, grade) VALUES(?,?,?)''', (id3, name3, grade3))

id4 = 12
name4 = "Peyton Sawyer"
grade4 = 45
cursor.execute('''INSERT INTO python_programming(id, name, grade) VALUES(?,?,?)''', (id4, name4, grade4))

id5 = 2
name5 = "Lucas Brooke"
grade5 = 99
cursor.execute('''INSERT INTO python_programming(id, name, grade) VALUES(?,?,?)''', (id5, name5, grade5))
# commit all these changes at once instead of doing it for each insert
db.commit()

# this gets all the students from the table where their grade is between 60 and 80 and then prints it
cursor.execute('''SELECT * FROM python_programming WHERE grade BETWEEN 60 AND 80''')
students = cursor.fetchall()
print(students)

# this changes the grade field for carl davis to 65 and then selects his row by selecting a row with his name
# and then printing the data given to make sure it has changed
cursor.execute('''UPDATE python_programming SET grade=65 WHERE name="Carl Davis"''')
cursor.execute('''SELECT * FROM python_programming WHERE name="Carl Davis"''')
print(cursor.fetchone())
db.commit()

# this deletes the record for Dennis Fredrickson by searching for all records that contain his name
cursor.execute('''DELETE FROM python_programming WHERE name="Dennis Fredrickson"''')
db.commit()

# this updates all the users grades that initially had a grade of lower than 55 to a grade of 40
cursor.execute('''UPDATE python_programming SET grade=40 WHERE id<55''')
db.commit()

cursor.execute('''SELECT * FROM python_programming''')
print(cursor.fetchall())

# The below drops the python_programming table so i could re-run this code for testing purposes'
cursor.execute('''DROP TABLE python_programming''')
db.commit()
