from tkinter import *
from tkinter.ttk import *

root = Tk()
root.title('Top Level Widget Example')
root.geometry('450x300')

label1=Label(root,text='Root Window')

def openTopLevel2():
    top2 = Toplevel()
    top2.title('Top Level 2')
    top2.geometry('200x100')

    label=Label(top2,text='Top Level2 Window')

    button=Button(top2,text='exit',command=top2.destroy)

    label.pack()
    button.pack()
    top2.mainloop()

def openTopLevel1():
    top1 = Toplevel(root)
    top1.title('Top Level 1')
    top1.geometry('200x200')
    label=Label(top1,text='Top Level2 Window')

    button1=Button(top1,text='Exit',command=top1.destroy)
    button2=Button(top1,text='Open Top Level 2',command=openTopLevel2)

    label.pack()
    button1.pack()
    button2.pack()
    top1.mainloop()

button = Button(root,text='Open Top Level 1',command=openTopLevel1)

button.place(x=155,y=50)

label1.pack()

root.mainloop()