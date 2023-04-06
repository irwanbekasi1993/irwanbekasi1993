from tkinter import *
from tkinter.ttk import *
from tkinter.filedialog import *

root = Tk()
root.title('Ask Save As File Example')

def save():
    files=[('All Files','*.*')]
    file= asksaveasfile(filetypes=files,defaultextension=files)

btn = Button(root,text='Save',command=lambda:save())
btn.pack(side=TOP,pady=20)

root.mainloop()