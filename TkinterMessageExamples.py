from tkinter import *
from tkinter.ttk import *

root = Tk()
root.title('Tkinter Message Examples')

root.geometry('300x200')

u = Label(root, text = 'Sample Message', font=50)
u.pack()

msg = Message(root,text='A Simple Message')

msg.pack()

root.mainloop()