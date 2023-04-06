from tkinter import *
from tkinter.ttk import *
from tkinter.scrolledtext import *

root = Tk()
root.title('Scrolled Text Example')

Label(root, text = 'Scrolled Text',font=('Times New Roman',15),
      background='green',foreground='white').grid(column=0,row=0)

textArea = ScrolledText(root,width=30,height=8,font=('Times New Roman',15))
textArea.grid(column=0,padx=10,pady=10)
textArea.insert(INSERT,'''
a
b
c
d
e
f
g
h
i
j
''')

textArea.configure(state=DISABLED)

root.mainloop()