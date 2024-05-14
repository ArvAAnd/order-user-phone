import sqlite3

conn = sqlite3.connect('database.db')

cursor = conn.cursor()
cursor.execute('CREATE TABLE users ('
               'id INTEGER PRIMARY KEY, '
               'name TEXT, '
               'phone TEXT, '
               'order_name TEXT)')
cursor.close()
conn.close()