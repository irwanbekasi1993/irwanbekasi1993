from tkinter import *
from tkinter.ttk import *

root = Tk()
root.title('Entry Widget Example')

root.geometry('600x400')

name_var=StringVar()
pass_var=StringVar()

def submit():
    name = name_var.get()
    password = pass_var.get()

    print('Your Name Is: '+name)
    print('Your Pasword Is: '+password)

    name_var.set('')
    pass_var.set('')

name_label= Label(root,text='Username',font=('calibre',10,'bold'))
name_entry = Entry(root,textvariable=name_var,font=('calibre',10,'normal'))

password_label= Label(root,text='Password',font=('calibre',10,'bold'))
password_entry = Entry(root,textvariable=pass_var,font=('calibre',10,'normal'),show='*')

btnSubmit = Button(root, text = 'Submit', command = submit)

name_label.grid(row=0,column=0)
name_entry.grid(row=0,column=1)

password_label.grid(row=1,column=0)
password_entry.grid(row=1,column=1)

btnSubmit.grid(row=2,column=1)

#read only entry
l1 = Label(root, text = 'Username')
l1.grid(row = 3, column = 0)

l2 = Label(root, text = 'Password')
l2.grid(row = 4, column = 0)

myStr=StringVar()
myStr.set('sample@mail.com')

entry = Entry(root,textvariable=myStr,state=DISABLED).grid(
    row=3,column=1,padx=0,pady=10)

password= Entry().grid(row=4,column=1)


root.mainloop()