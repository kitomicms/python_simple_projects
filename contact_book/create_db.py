# create a database
import sqlite3

conn = sqlite3.connect("contact.db")
c = conn.cursor()
c.execute('''CREATE TABLE CONTACT (ID INTEGER PRIMARY KEY AUTOINCREMENT,NAME TEXT NOT NULL,
ADDRESS TEXT NOT NULL);''')
conn.commit()
print("Table created successfully")
