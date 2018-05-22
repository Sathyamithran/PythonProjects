import random,urllib.request
import sqlite3

conn=sqlite3.connect('mydb.db')



def reset_db():
##reset the  account.tb in mydb.db
    d=input('\nenter "reset" to reset: ')
    if (d=='reset') or (d=='RESET'):
        c=conn.execute('select usid,pw from account')
        for row in c:
            row[0]
            row[1]
        d=row[0]
        e=row[1]
    
        a=input('\nenter current username: ')
        b=input('enter current password: ')
        if(a==row[0])and(b==row[1]):
            print('\n---before reseting---')
            e=conn.execute('select usid,pw from account')
            for row in e:
                print('\nusername: ',row[0],'\npassword: ',row[1])
            conn.execute('drop table account')
            conn.execute('create table account(usid text not null,pw text not null)')
            conn.execute('insert into account(usid,pw) values("admin","admin")')
            #conn.commit()
    
            print('\n---after reseting---')
            e=conn.execute('select usid,pw from account')
            for row in e:
                print('\nusername: ',row[0],'\npassword: ',row[1])
    conn.commit()

reset_db()
