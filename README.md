[![SQLite3](https://img.shields.io/badge/SQLite3-blue)](https://www.sqlite.org/index.html)
[![Python](https://img.shields.io/badge/Python-3-blue)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green)](https://opensource.org/licenses/MIT)

[![Issues](https://img.shields.io/github/issues/umairabbasDev/SQLite3)](https://github.com/umairabbasDev/SQLite3/issues)
[![Pull Requests](https://img.shields.io/github/issues-pr/umairabbasDev/SQLite3)](https://github.com/umairabbasDev/SQLite3/pulls)
[![Contributors](https://img.shields.io/github/contributors/umairabbasDev/SQLite3)](https://github.com/umairabbasDev/SQLite3/graphs/contributors)
[![Last Commit](https://img.shields.io/github/last-commit/umairabbasDev/SQLite3)](https://github.com/umairabbasDev/SQLite3/commits/master)

# Python SQLite3 Tutorial for Beginners

This tutorial provides a brief introduction to SQLite3 using Python for beginners. SQLite3 is a lightweight, self-contained, open-source, and serverless relational database management system (RDBMS). It is widely used in applications that require a small and efficient database engine. SQLite3 is also the most widely deployed database engine in the world.

## Installation
SQLite3 is a built-in module in Python, which means you don't need to install anything to use it. It's included in the Python standard library.

## Creating a Database
To create a new database in SQLite3 using Python, you need to create a connection to the database using the `sqlite3.connect()` method. For example, to create a new database named `mydb.db`, use the following code:

```python
import sqlite3

# create a new database
conn = sqlite3.connect('mydb.db')
```

This will create a new database file named mydb.db in the current directory.

## Creating a Table
Once you have created a database connection, you can create a table in it using the conn.execute() method. To create a table, you need to specify the table schema, which includes the column names and data types. For example, to create a table named users with columns id, name, and email, where id is an integer, name is a string, and email is a string, use the following code:

```python
# create a new table
conn.execute('''CREATE TABLE users (id INTEGER, name TEXT, email TEXT)''')
```

This will create a new table named users with the specified columns.

##Inserting Data
After creating a table, you can insert data into it using the conn.execute() method. For example, to insert a new record into the users table, use the following code:

```python
# insert data
conn.execute('''INSERT INTO users (id, name, email) VALUES (1, 'John Smith', 'john@example.com')''')
```
This will insert a new record with id 1, name 'John Smith', and email 'john@example.com' into the users table.


## Querying Data
To query data from a table, use the conn.execute() method with a SELECT statement. For example, to retrieve all records from the users table, use the following code:

```python
# query data
cursor = conn.execute('''SELECT * FROM users''')
for row in cursor:
    print(row)
```
This will print all the records in the users table

## Updating Data
To update data in a table, use the conn.execute() method with an UPDATE statement. For example, to update the name of the record with id 1 in the users table to 'Jane Doe', use the following code:

```python
# update data
conn.execute('''UPDATE users SET name='Jane Doe' WHERE id=1''')
```
This will update the name of the record with id 1 to 'Jane Doe'.

## Deleting Data
To delete data from a table, use the conn.execute() method with a DELETE statement. For example, to delete the record with id 1 from the users table, use the following code:

```python

# delete data
conn.execute('''DELETE FROM users WHERE id=1''')
```
This will delete the record with id 1 from the users table.

---
