Python 3.6.3 (v3.6.3:2c5fed8, Oct  3 2017, 17:26:49) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
==== RESTART: F:/Python projects/Digital Image Processing/matplotdemo.py ====
>>> import glob
>>> glob.glob('./[0-9].*')['./1.gif','./2.txt']
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    glob.glob('./[0-9].*')['./1.gif','./2.txt']
TypeError: list indices must be integers or slices, not tuple
>>> glob.glob('./[0-9].*')
[]
>>> glob.glob('*.gif')
[]
>>> import glob
>>> glob.glob('F:\\Python projects\\Digital Image Processing','*')







exit()


