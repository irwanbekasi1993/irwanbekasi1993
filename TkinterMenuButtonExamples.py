from tkinter import *
from tkinter.ttk import *

root = Tk()
root.title('Menu Button Example')
root.geometry('300x200')

w = Label(root, text = 'Menu Button Example',font=50)
w.pack()

menuBtn = Menubutton(root,text='Menu')
menuBtn.menu=Menu(menuBtn)
menuBtn['menu']=menuBtn.menu

var1=StringVar()
var2=StringVar()
var3=StringVar()

menuBtn.menu.add_checkbutton(label='Courses',variable=var1)
menuBtn.menu.add_checkbutton(label='Students',variable=var2)
menuBtn.menu.add_checkbutton(label='Career',variable=var3)

menuBtn.pack()

root.mainloop()