import sqlite3
conn=sqlite3.connect('mydb.db')

d=input('enter "reset" to reset: ')

print('---before reseting---')
e=conn.execute('select usid,pw from account')
for row in e:
    print('username: ',row[0],'\npassword: ',row[1])
    

if (d=='reset') or (d=='RESET'):
    conn.execute('update account set usid= "admin" pw="admin";')
#conn.commit()
    
print('---after reseting---')
e=conn.execute('select usid,pw from account')
for row in e:
    print('username: ',row[0],'\npassword: ',row[1])
conn.commit()
