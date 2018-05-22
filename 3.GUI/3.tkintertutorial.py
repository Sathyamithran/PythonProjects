from tkinter import *

root = Tk()# main window

#.......label....
one = Label(root, text='one', bg='red', fg='white')#label 1 args(to display on window, name of the label, backgroud colour, foreground colour)
one.pack()#display the label 

two =  Label(root, text='two', bg='green', fg='black')
two.pack(fill=X)# display with filling x-axis

three =  Label(root, text='three', bg='blue', fg='black')
three.pack(side=LEFT, fill=Y)# display with left side and  filling y-axis

root.mainloop()#loop to keep it on display
