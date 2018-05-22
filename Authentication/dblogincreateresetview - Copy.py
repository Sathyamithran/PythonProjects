
def login_db():
##login code using account.tbl in mydb.db
    c=conn.execute('select usid,pw from account')
    for row in c:
        row[0]
        row[1]

    a=input('\nenter the username: ')
    b=input('enter the password: ')
    if(a==row[0])and(b==row[1]):
        from SrchEgnOptmstion import webpageparser
    else:
        print('\n\nsomething is wrong')
    conn.commit()
    



def reset_db():
##reset the  account.tb in mydb.db
    d=input('\nenter "reset" to reset: ')

    print('\n---before reseting---')
    e=conn.execute('select usid,pw from account')
    for row in e:
        print('\nusername: ',row[0],'\npassword: ',row[1])
    

    if (d=='reset') or (d=='RESET'):
        conn.execute('drop table account')
        conn.execute('create table account(usid text not null,pw text not null)')
        conn.execute('insert into account(usid,pw) values("admin","admin")')
        #conn.commit()
    
    print('\n---after reseting---')
    e=conn.execute('select usid,pw from account')
    for row in e:
        print('\nusername: ',row[0],'\npassword: ',row[1])
    conn.commit()





import random,urllib.request

def create_db():
##create a new username and password
    c=conn.execute('select usid,pw from account')
    for row in c:
        row[0]
        row[1]

    a=input('\nenter the username: ')
    b=input('enter the password: ')
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
                
            
        print('Go to Login after Creating the a new username password.......')
            
        


def view_db():
##view the contents of the table
    w=conn.execute('select usid,pw from account')
    for row in w:
        print('\nusername: ',row[0],'\npassword: ',row[1])
    conn.commit()





    
import sqlite3
conn=sqlite3.connect('mydb.db')

z=1
while(z==1):
    x=input('\ndo you want to 1.login 2.reset 3.create new :  ')
    if(x == 'reset')or(x == '2'):
        reset_db()
    elif(x == 'login')or(x == '1'):
        login_db()
    elif(x == 'create')or(x == 'create new')or(x =='3'):
        create_db()
    elif(x == 'view')or(x == '4'):
        view_db()
    y=input('\ndo you want to continue: y or n: ')
    if(y=='y'):
        z=1
    else:
        z=0
