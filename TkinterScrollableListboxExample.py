from tkinter import *
from tkinter.ttk import *

root = Tk()
root.title('Scrollable Listbox')

listBox = Listbox(root)
listBox.pack(side=LEFT,fill=BOTH)

scrollBar=Scrollbar(root)
scrollBar.pack(side=RIGHT,fill=BOTH)

for values in range(101):
    listBox.insert(END,values)

listBox.config(yscrollcommand=scrollBar.set)
scrollBar.config(command=listBox.yview)

root.mainloop()