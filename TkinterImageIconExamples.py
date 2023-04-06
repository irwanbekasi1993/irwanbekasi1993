from tkinter import *
from tkinter.ttk import *

root = Tk()
root.title('image as icon example')

p1 = PhotoImage(file='HTML5_badge.png')
root.iconphoto(False,p1)

b=Button(root,text='Click Here')
b.pack(side=TOP)

root.mainloop()