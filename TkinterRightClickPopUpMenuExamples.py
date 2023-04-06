from tkinter import *
from tkinter.ttk import *

root = Tk()
root.title('Right Click To Display Menu')

l = Label(root,text='right click to display menu',width=40)
l.pack()

m= Menu(root,tearoff=0)
m.add_command(label='Cut')
m.add_command(label='Copy')
m.add_command(label='Paste')
m.add_command(label='Reload')
m.add_separator()
m.add_command(label='Rename')

def popUp(event):
    try:
        m.tk_popup(event.x_root,event.y_root)
    finally:
        m.grab_release()

l.bind('<Button-3>',popUp)
root.mainloop()