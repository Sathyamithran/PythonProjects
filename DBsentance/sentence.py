import sqlite3
conn=sqlite3.connect('sentence.db')

##tables sentence and neglect are created
'''conn.execute('create table sentence(text not null);')
conn.execute('create table neglect(text not null);')'''

a=input('sentence: ')
b=input('neglecting words: ')
c=a.split(' ')
d=b.split(' ')
e=conn.execute('insert into sentence(text) value(?)',(a))
f=conn.execute('insert into neglect(text) value(?)',(b))

for row,col in c,d:
    print(row,col)

conn.commit()
conn.close()
