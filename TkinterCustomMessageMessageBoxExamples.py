from tkinter import *
from tkinter import messagebox

root = Tk()
root.title('Customize Message Box')

def button1():
    messagebox.showinfo('Status','Button-1 Pressed')

def button2():
    messagebox.showinfo('Status','Button-2 Pressed')


root.geometry('100x100')
B1= Button(root,text='Button1',command=button1)
B2= Button(root,text='Button2',command=button2)

B1.pack()
B2.pack()

str_var=StringVar()
str_var.set('Custom Message')
label = Message(root,textvariable=str_var,relief=RAISED)
label.pack()


root.mainloop()