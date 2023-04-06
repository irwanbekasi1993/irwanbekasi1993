from tkinter import *
from tkinter.ttk import *

root = Tk()
root.title('Binding Function In ListBox')
root.geometry('250x275')

def action(event):
    cs=lb.curselection()
    w.config(text=lb.get(cs))
    for list in cs:
        if list == 0:
            root.configure(background='red')
        elif list == 1:
            root.configure(background='green')
        elif list == 2:
            root.configure(background='yellow')
        elif list == 3:
            root.configure(background='white')

lb = Listbox(root,height=6)
lb.insert(0,'red')
lb.insert(1,'green')
lb.insert(2,'yellow')
lb.insert(3,'white')

lb.bind('<Double-1>',action)
lb.pack()

w=Label(root,text='default')
w.pack()

root.mainloop()