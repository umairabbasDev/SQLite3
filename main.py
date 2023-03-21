import sqlite3

# create a new database
conn = sqlite3.connect('mydb.db')

# create a new table
conn.execute('''CREATE TABLE users (id INTEGER, name TEXT, email TEXT)''')

# insert data
conn.execute('''INSERT INTO users (id, name, email) VALUES (1, 'John Smith', 'john@example.com')''')
conn.execute('''INSERT INTO users (id, name, email) VALUES (2, 'Jane Doe', 'jane@example.com')''')

# query data
cursor = conn.execute('''SELECT * FROM users''')
for row in cursor:
    print(row)

# update data
conn.execute('''UPDATE users SET name='Jack Smith' WHERE id=1''')

# delete data
conn.execute('''DELETE FROM users WHERE id=2''')

# commit changes
conn.commit()

# close the connection
conn.close()
