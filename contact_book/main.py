# create a database with sqlite

import sqlite3
import pandas as pd

print('Welcome to the contact book')
user_input = input('please select action: display/insert/edit/delete')

while true:
  # check input


  # if pd


# .to_sql(table name,conn,if_exists="replace"/append)

conn = sqlite3.connect('contact.db')
print("Database connected successfully")


c = conn.cursor()
df = pd.read_sql_query("SELECT * FROM CONTACT", conn)
print(df)
#c.execute('''CREATE TABLE CONTACT (ID INT PRIMARY KEY NOT NULL,
#NAME TEXT NOT NULL,
#ADDRESS TEXT NOT NULL);''')
#print("Table created successfully")
#conn.commit()
conn.close()

# func: list out existing


# func: find contact


# func: insert contact
