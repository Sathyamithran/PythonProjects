import sqlite3
conn=sqlite3.connect('chatDB.db')
conn.execute("drop table student")
conn.execute('create table student (dbname text not null,dbhobbies text,dblikes text,dbf_name text not null,dbm_name text not null,dbs text not null,dbs_count int,dbs_name text,dbfav_no int not null)')

name=input('Hi..... whats your name?.... ')
print('\nits nice to meet you '+name)


hobbies=input('\nTell me about your hobbies?.... ')
print('\nso you like '+hobbies)


likes=input('\nOhhh....so what else do you like?.... ')
print('\n:O I didnt know that you like '+likes+' A man of taste....')


f_name=input('\nSo '+name+'...whats your father name.... ')


m_name=input('\nAnd your mother name.... ')



fav_number=input('\nSay your favourite number... ')



odd = {'1','3','5','7','9'}
even = {'2','4','6','8'}
if fav_number in odd:
    print('\n....thats mine too...')
elif fav_number in even:
    print('\n...thats your lucky number haaan...')
elif fav_number == '0':
    print('\nn....thats strange lucky number i have ever seen')

    
siblings=input('\ndo you have any siblings Mr.'+name+'?.... ')

if 'yes' in siblings:
    s_count=input('\nhow many siblings do you have?... ')
    
    
    s_name=input('\ncan i know your '+s_count+' siblings names.... ')
    
    
    
elif 'no' in siblings:
    print('\nso you have all of your parents affection....')
    
conn.execute('insert into student (dbname,dbhobbies,dblikes,dbf_name,dbm_name,dbs,dbfav_no) values(?,?,?,?,?,?,?)',(name,hobbies,likes,f_name,m_name,siblings,fav_number))
conn.commit()

a=conn.execute('select dbname,dbhobbies,dblikes,dbf_name,dbm_name,dbs,dbfav_no from student')
for d in a:
    print(list(d))
    #print('my name is '+d[0],d[1,d[2]],d[3],d[4],d[5],d[6],d[7])
conn.commit()
conn.close()
