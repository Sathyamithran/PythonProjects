#!C:\Program Files (x86)\Python36-32\pythonw.exe

import cgi,cgitb
import pyodbc
print('Content-Type: text/html')
print()
form = cgi.FieldStorage()
n=form.getvalue('Number')
print(n)
