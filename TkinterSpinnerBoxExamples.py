from tkinter import *
from tkinter.ttk import *

root = Tk()
root.title('Spinner Box Example')
root.geometry('300x200')

w = Label(root, text = 'Spinner Box',font=50)
w.pack()

sp = Spinbox(root, from_=0,to=100)
sp.pack()

root.mainloop()