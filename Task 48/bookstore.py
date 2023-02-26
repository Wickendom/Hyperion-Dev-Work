import sqlite3

# this creates our database if it is not created and then connects to it
db = sqlite3.connect('book_store_db')

# this gets our cursor object so we can communicat with the database
cursor = db.cursor()
# create the table within the database called ebookstore
cursor.execute('''CREATE TABLE ebookstore(id INTEGER PRIMARY KEY, title TEXT, author TEXT, qty INTEGER)''')
db.commit()


# This section is for inserting the data into the database
id = 3001
title = "A Tale of Two Cities"
author = "Charles Dickens"
qty = 30

cursor.execute('''INSERT INTO ebookstore(id,title,author,qty) VALUES(?,?,?,?)''', (id,title,author,qty))

id += 1
title = "Harry Potter and the Philosophers Stone"
author = "J. K. Rowling"
qty = 40

cursor.execute('''INSERT INTO ebookstore(id,title,author,qty) VALUES(?,?,?,?)''', (id,title,author,qty))

id += 1
title = "The Lion, the Witch and the Wardrobe"
author = "C. S. Lewis"
qty = 25

cursor.execute('''INSERT INTO ebookstore(id,title,author,qty) VALUES(?,?,?,?)''', (id,title,author,qty))

id += 1
title = "The Lord of the Rings"
author = "J R R Tolkien"
qty = 37

cursor.execute('''INSERT INTO ebookstore(id,title,author,qty) VALUES(?,?,?,?)''', (id,title,author,qty))

id += 1
title = "Alice in Wonderland"
author = "Lewis Carroll"
qty = 30

cursor.execute('''INSERT INTO ebookstore(id,title,author,qty) VALUES(?,?,?,?)''', (id,title,author,qty))
# finally commit all of these chanes and inserts them into the table
db.commit()

# this is the menu system, it checks to see what the user has input. it keeps checking until they enter "Exit"
selection = ""

while selection != "exit":
    selection = input("Please enter one of the following values, Enter, Update, Delete, Search, Exit ").lower()
    if selection == "enter":
        # increment the book id instead of setting it so as many books as you want can be input
        id += 1
        title = input("Please enter the title of the book ")
        author = input("Please enter the author of the book ")
        qty = int(input("Please enter the quantity of these books you have "))

        # this inserts the new book into the table
        cursor.execute('''INSERT INTO ebookstore(id,title,author,qty) VALUES(?,?,?,?)''', (id,title,author,qty))
        db.commit()

    elif selection == "update":
        title = input("Please enter the title of the book you wish to update the quantity of ")
        qty = int(input("Please enter the new quantity of this book "))

        # here we try to update the book with a new quantity, if it cannot find the book. it shows an error message
        try:
            cursor.execute('''UPDATE ebookstore SET qty = ? WHERE title = ?''', (qty, title))
        except:
            print(f"Unable to find book with title {title}, Please try again")

    elif selection == "delete":
        title = input("Please enter the title of the book you wish to delete ")

        # here we try to delete a book from the table. if it is unable to find it, it then throws an error
        try:
            cursor.execute('''DELETE FROM ebookstore WHERE title = ?''', (title,))
        except:
            print(f"A book with the title {title} was not found, please try again")

    elif selection == "search":
        title = input("Please enter the tile of the book you wish to search for ")

        # this retrieves the data from the table and then prints the line given
        cursor.execute('''SELECT * FROM ebookstore WHERE title = ?''', (title,))
        print(cursor.fetchone())
    elif selection == "exit":
        break
    else:
        print("Invalid selection, please enter a correct value")


# the following code drops the table. This is so this code can be run multiple times and not create
# duplicate tables. this would not exist in a production environment
cursor.execute('''DROP TABLE ebookstore''')
db.commit()
