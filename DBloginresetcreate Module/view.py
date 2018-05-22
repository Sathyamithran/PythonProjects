import random,urllib.request
import sqlite3
conn=sqlite3.connect('mydb.db')

 
def view_db():
##view the contents of the table
    w=conn.execute('select usid,pw from account')
    for row in w:
        print('\nusername: ',row[0],'\npassword: ',row[1])
    conn.commit()

view_db()
