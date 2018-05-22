from tkinter import *

root = Tk()# main window

tf = Frame(root)#it is frame border on top
tf.pack()#to display it in window....without it it will not display

bf = Frame(root)#  ''
bf.pack(side=BOTTOM)#  ''

button1 = Button(tf, text = 'button 1', fg= 'red')#button..args(where to appear, text to be displayed in button, color of button)
button1.pack(side=LEFT)#display button1 and where  to display

button2 = Button(tf, text = 'button 2', fg= 'blue')#button..args(where to appear, text to be displayed in button, color of button)
button2.pack(side=LEFT)#display button2

button3 = Button(tf, text = 'button 3', fg= 'green')#button..args(where to appear, text to be displayed in button, color of button)
button3.pack(side=LEFT)#display button3

button4 = Button(bf, text = 'button 4', fg= 'yellow')#button..args(where to appear, text to be displayed in button, color of button)
button4.pack(side=BOTTOM)#display button4

root.mainloop()#loop to keep it on display
