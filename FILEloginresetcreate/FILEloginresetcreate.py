import random,urllib.request

def login():
    
    a=input('enter username: ')
    b=input('enter password: ')
    f1=open('username.txt','w')
    f2=open('password.txt','w')
    f1.write('admin')
    f2.write('admin')
    f1.close()
    f2.close()
    f1=open('username.txt','r')
    f2=open('password.txt','r')
    c=f1.read()
    d=f2.read()
    if(a==c):
        if(b==d):
            print('\n*****login successful*****')
        else:
            print('\n*****password is wrong*****')
    else:
        print('\n*****username is worng*****')

def reset():
    f1=open('username.txt','w')
    f2=open('password.txt','w')
    f1.write('admin')
    f2.write('admin')
    f1.close()
    f2.close()
    print('\n*****the account is RESETED*****')

def create():
    f1=open('username.txt','r+')
    f2=open('password.txt','r+')
    c=f1.read()
    d=f2.read()
    print('-----Hereyou can change the Username & Password-----')
    z=input('\nenter default username: ')
    y=input('enter default password: ')
    if(z==c)and(y==d):
        a=input('\nenter the new username: ')
        b=input('enter the new password: ')
        e=input('confirm new password: ')
        if(b==e):
            f1=open('username.txt','w')
            f2=open('password.txt','w')
            f1.write(a)
            f2.write(b)
            f1.close()
            f2.close()
            print('\n*****new username and password is created*****')
        else:
            print('*****rewrite the password*****')
    else:
        print('\n*****check your default username & password*****')
        g=input('forgot the password: ')
        if(g=='y'):
            print('---enter the mail ID and phone number to send OTP---')
            
            b=input('enter the number to send the OTP: ')
            r='the_OTP_is:_'
            s=str(random.randint(1000,9999))
            t=str(r+s)
            #print(s)

            url = 'https://smsapi.engineeringtgr.com/send/?Mobile=9489241119&Password=sonofsun&Message='+t+'&To='+b+'&Key=vssat1E54aYbznLePoUIj'

            f=urllib.request.urlopen(url)
            

            
            j=input('enter the OTP: ')
            if (s==j):
                a=input('\nenter the new username: ')
                b=input('enter the new password: ')
                e=input('confirm new password: ')
                if(b==e):
                    f1=open('username.txt','w')
                    f2=open('password.txt','w')
                    f1.write(a)
                    f2.write(b)
                    f1.close()
                    f2.close()
                    print('\n*****new username and password is created*****')
            else:
                print('you have entered your OTP wrong')






j=1
while(j==1):
    print('\n\t1. Login')
    print('\t2. Reset')
    print('\t3. Create')
    f=input('what do you want now: ')
    if(f=='reset')or(f=='2')or(f=='Reset'):
        reset()
    elif(f=='login')or(f=='1')or(f=='Login'):
        login()
    elif(f=='create')or(f=='3')or(f=='Create'):
        create()
    else:
        print('*****enter the option correctly*****')
    print('\nDo you want to continue:')
    g=input('Yes type y ; No type n: ')
    if(g=='y'):
        j=1
    else:
        j=0
