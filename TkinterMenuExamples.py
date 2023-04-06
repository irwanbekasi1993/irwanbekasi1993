from tkinter import *
from tkinter.ttk import *

root = Tk()
root.title('Menu Widget Example')

menuBar = Menu(root)

file= Menu(menuBar,tearoff=0)
menuBar.add_cascade(label='File', menu=file)
file.add_command(label='New File',menu=None)
file.add_command(label='Open',menu=None)
file.add_command(label='Save',menu=None)
file.add_separator()
file.add_command(label='Exit',command=root.destroy)

edit= Menu(menuBar,tearoff=0)
menuBar.add_cascade(label='Edit', menu=edit)
edit.add_command(label='Cut',menu=None)
edit.add_command(label='Copy',menu=None)
edit.add_command(label='Paste',menu=None)
edit.add_separator()
edit.add_command(label='Find',command=None)
edit.add_command(label='Find Again',command=None)

help= Menu(menuBar,tearoff=0)
menuBar.add_cascade(label='Help', menu=help)
help.add_command(label='Tk Help',menu=None)
help.add_command(label='Demo',menu=None)
help.add_command(label='Paste',menu=None)
help.add_separator()
help.add_command(label='About Tk',command=None)

root.config(menu=menuBar)
root.mainloop()