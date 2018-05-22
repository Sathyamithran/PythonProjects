f1=open('Bio.doc','w')

name=input('Hi..... whats your name?.... ')
print('\nits nice to meet you '+name)
f1.write('My name is '+name+'.')

hobbies=input('\nTell me about your hobbies?.... ')
print('\nso you like '+hobbies)
f1.write('\nI would like to go on '+hobbies+' in my free time.')

likes=input('\nOhhh....so what else do you like?.... ')
print('\n:O I didnt know that you like '+likes+' A man of taste....')
f1.write('\nAnd I also like '+likes+' too.')

f_name=input('\nSo '+name+'...whats your father name.... ')
f1.write('\nAnd about my family... my father name is '+f_name+'.')

m_name=input('\nAnd your mother name.... ')
f1.write('\nAnd my mother name is '+m_name+'.')

siblings=input('\ndo you have any siblings Mr.'+name+'?.... ')
if 'yes' in siblings:
    s_count=input('\nhow many siblings do you have?... ')
    f1.write('\nI have '+s_count+' siblings ')
    s_name=input('\ncan i know your '+s_count+' siblings names.... ')
    f1.write('and their names are '+s_name+'.')
elif 'no' in siblings:
    print('\nso you have all of your parents affection....')
    f1.write('\n I dont have any siblings...so I m lone lion.')

fav_number=input('\nSay your favourite number... ')
odd = {'1','3','5','7','9'}
even = {'2','4','6','8'}
if fav_number in odd:
    print('\n....thats mine too...')
elif fav_number in even:
    print('\n...thats your lucky number haaan...')
elif fav_number == '0':
    print('\nn....thats strange lucky number i have ever seen')
f1.write('\nMy favourite number is '+fav_number)

f1.close()
