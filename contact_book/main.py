# create a database with sqlite

import sqlite3
import pandas as pd

print('Welcome to the contact book')
# user_input = input('please select action: display/insert/edit/delete')
conn = sqlite3.connect('contact.db')
print("Database connected successfully")

def insert_records(conn):
  name = input("Insert contact name: ")
  address = input("Insert contact address: ")
  # in the setup you need to set the primary key is AUTOINCREMENT
  sql = "INSERT INTO CONTACT(NAME,ADDRESS) VALUES(?,?)"
  cur = conn.cursor()
  cur.execute(sql,(name,address))
  conn.commit()

def delete_records(conn):
  id_ = input("which record would you like to delete?")
  sql = 'DELETE FROM CONTACT WHERE ID=?'
  cur = conn.cursor()
  cur.execute(sql,(id_,))
  conn.commit()
def list_records(conn):
  df = pd.read_sql_query("SELECT * FROM CONTACT", conn)
  return df

n = "Y"
while n == "Y":
  # check input
  user_request = input("what do you like to do? insert/delete/list ")
  print(eval(user_request+"_records(conn)"))

  n = input("Any more requests? Y/N ")

#c.execute('''CREATE TABLE CONTACT (ID INT PRIMARY KEY NOT NULL,
#NAME TEXT NOT NULL,
#ADDRESS TEXT NOT NULL);''')
#print("Table created successfully")
#conn.commit()
conn.close()
