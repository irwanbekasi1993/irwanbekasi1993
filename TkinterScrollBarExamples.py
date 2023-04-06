from tkinter import *
from tkinter.ttk import *

root = Tk()
root.title('Scroll Bar Example')
root.geometry('150x200')

w = Label(root, text = 'Scroll Bar',font=50)
w.pack()

scrollBar=Scrollbar(root)
scrollBar.pack(side=RIGHT,fill=Y)

myList=Listbox(root,yscrollcommand=scrollBar.set)

for line in range(1,26):
    myList.insert(END,'huruf: '+str(line))

myList.pack(side=LEFT,fill=BOTH)
scrollBar.config(command=myList.yview)

root.mainloop()