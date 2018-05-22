import random,urllib.request
import sqlite3
conn=sqlite3.connect('mydb.db')

def create_db():
##create a new username and password
    c=conn.execute('select usid,pw from account')
    for row in c:
        row[0]
        row[1]

    a=input('\nenter current username: ')
    b=input('enter current password: ')
    if(a==row[0])and(b==row[1]):
        conn.execute('delete from account')
        f=input('\nenter the new username: ')
        g=input('enter the new password: ')
        conn.execute('insert into account(usid,pw) values(?,?)',(f,g))

        h=conn.execute('select usid,pw from account')
        print('\nthe new username and password is changed to....')
        for row in h:
            print('\nusername: ',row[0],'password: ',row[1])
        conn.commit()
    else:
        print('\nSomething is not right')
        print('\n--------------------------------\n')
        print('Did you forget password: ')
        i=input('\ntype y for yes and n for no: ')
        if i=='y':
            import random,urllib.request

            b=input('\nenter the number to send the OTP: ')
            s=str(random.randint(1000,9999))
            url = 'https://smsapi.engineeringtgr.com/send/?Mobile=9489241119&Password=sonofsun&Message='+s+'&To='+b+'&Key=vssat1E54aYbznLePoUIj'
            #print(s)
            f=urllib.request.urlopen(url)
            print(f.read())
            j=input('\nenter the OTP: ')
            if(s==str(j)):
                conn.execute('delete from account')
                f=input('\nenter the new username: ')
                g=input('\nenter the new password: ')
                conn.execute('insert into account(usid,pw) values(?,?)',(f,g))

                h=conn.execute('select usid,pw from account')
                for row in h:
                    print('username: ',row[0],'\npassword: ',row[1])
                conn.commit()
                
            
create_db()
