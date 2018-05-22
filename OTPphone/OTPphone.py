import random,urllib.request

b=input('enter the number to send the OTP: ')
r='the_OTP_is:_'
s=str(random.randint(1000,9999))
t=str(r+s)
print(t)

url = 'https://smsapi.engineeringtgr.com/send/?Mobile=9489241119&Password=sonofsun&Message='+t+'&To='+b+'&Key=vssat1E54aYbznLePoUIj'

f=urllib.request.urlopen(url)
print(f.read())
