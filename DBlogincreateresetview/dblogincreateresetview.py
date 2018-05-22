
def login_db():
##login code using account.tbl in mydb.db
    c=conn.execute('select usid,pw from account')
    for row in c:
        row[0]
        row[1]

    a=input('enter the username: ')
    b=input('enter the password: ')
    if(a==row[0])and(b==row[1]):
        print('\nthe login is successful')
    else:
        print('\nsomething is wrong')
    conn.commit()
    



def reset_db():
##reset the  account.tb in mydb.db
    d=input('enter "reset" to reset: ')

    print('---before reseting---')
    e=conn.execute('select usid,pw from account')
    for row in e:
        print('username: ',row[0],'\npassword: ',row[1])
    

    if (d=='reset') or (d=='RESET'):
        conn.execute('update account set usid= "admin" pw="admin" where null;')
    #conn.commit()
    
    print('---after reseting---')
    e=conn.execute('select usid,pw from account')
    for row in e:
        print('username: ',row[0],'\npassword: ',row[1])
    conn.commit()


def create_db():
##create a new username and password
    conn.execute('delete from account')
    f=input('enter the new username: ')
    g=input('enter the new password: ')
    conn.execute('insert into account(usid,pw) values(?,?)',(f,g))

    h=conn.execute('select usid,pw from account')
    for row in h:
        print('username: ',row[0],'\npassword: ',row[1])
    conn.commit()

def view_db():
##view the contents of the table
    w=conn.execute('select usid,pw from account')
    for row in w:
        print('username: ',row[0],'\npassword: ',row[1])
    conn.commit()





    
import sqlite3
conn=sqlite3.connect('mydb.db')

z=1
while(z==1):
    x=input('\ndo you want to 1.login 2.reset 3.create new 4.view table :  ')
    if(x == 'reset')or(x == '2'):
        reset_db()
    elif(x == 'login')or(x == '1'):
        login_db()
    elif(x == 'create')or(x == 'create new')or(x =='3'):
        create_db()
    elif(x == 'view')or(x == '4'):
        view_db()
    y=input('\ndo you want to continue: y or n:')
    if(y=='y'):
        z=1
    else:
        z=0
