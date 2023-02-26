import sqlite3

db = sqlite3.connect('book_store_db')

cursor = db.cursor()

cursor.execute('''CREATE TABLE ebookstore(id INTEGER PRIMARY KEY, title TEXT, author TEXT, qty INTEGER)''')
db.commit()

id = 3001
title = "A Tale of Two Cities"
author = "Charles Dickens"
qty = 30

cursor.execute('''INSERT INTO ebookstore(id,title,author,qty) VALUES(?,?,?,?)''', (id,title,author,qty))

id = 3002
title = "Harry Potter and the Philosophers Stone"
author = "J. K. Rowling"
qty = 40

cursor.execute('''INSERT INTO ebookstore(id,title,author,qty) VALUES(?,?,?,?)''', (id,title,author,qty))

id = 3003
title = "The Lion, the Witch and the Wardrobe"
author = "C. S. Lewis"
qty = 25

cursor.execute('''INSERT INTO ebookstore(id,title,author,qty) VALUES(?,?,?,?)''', (id,title,author,qty))

id = 3004
title = "The Lord of the Rings"
author = "J R R Tolkien"
qty = 37

cursor.execute('''INSERT INTO ebookstore(id,title,author,qty) VALUES(?,?,?,?)''', (id,title,author,qty))

id = 3005
title = "Alice in Wonderland"
author = "Lewis Carroll"
qty = 30

cursor.execute('''INSERT INTO ebookstore(id,title,author,qty) VALUES(?,?,?,?)''', (id,title,author,qty))

db.commit()

cursor.execute('''SELECT * FROM ebookstore''')
print(cursor.fetchall())

cursor.execute('''DROP TABLE ebookstore''')
db.commit()
