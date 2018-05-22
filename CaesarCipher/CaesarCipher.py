def enc():
    a=input('enter data to be encrypted: ')
    e=''
    for b in a:
        c=int(ord(b))+3
        d=chr(c)

        e=e+str(d)
    print(e)




j=1
while(j==1):
    print('\n\n')

    enc()
    print('\nDo you want to continue:')
    g=input('Yes type y ; No type n: ')
    if(g=='y'):
        j=1
    else:
        j=0

