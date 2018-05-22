import random,smtplib
server = smtplib.SMTP('smtp.gmail.com',587)
server.ehlo()
server.starttls()
server.login('vssathyamithran1@gmail.com','sonofsun')

m=input('enter the mail address to send OTP: ')

s=random.randint(1000,9999)
r=str(s)
print(r)    

server.sendmail('vssathyamithran1@gmail.com',m,r)
