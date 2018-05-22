import random,urllib.request
import sqlite3
conn=sqlite3.connect('mydb.db')

def login_db():
##login code using account.tbl in mydb.db
    c=conn.execute('select usid,pw from account')
    for row in c:
        row[0]
        row[1]
    d=row[0]
    e=row[1]
    
    a=input('\nenter the username: ')
    b=input('enter the password: ')
    if(a==row[0])and(b==row[1]):
        print('\n\nthe login is successful')
    elif(a==row[0]):
        print('\n\nsomething is wrong')
        print('---Did you forgot password---')
        

        s=input('\nenter the number ---Mr.'+d+'--- to send the password: ')
        url = 'https://smsapi.engineeringtgr.com/send/?Mobile=9489241119&Password=sonofsun&Message='+e+'&To='+s+'&Key=vssat1E54aYbznLePoUIj'
        f=urllib.request.urlopen(url)
        #print(f.read())

        c=input('enter the password now : ')
        if(b==c):
            print('\nlogin is successfull')
    else:
        print('you are totally wrong')
    conn.commit()
    



login_db()

   
