from tkinter import *
from tkinter.ttk import *

root = Tk()
root.title('List Box Example')
root.geometry('300x250')

listBox= Listbox(root,height=10,width=15,bg='grey',
                 activestyle='dotbox',font='Helvetica',
                 fg='yellow')

label = Label(root, text = 'Food Items')

listBox.insert(1,'Nachos')
listBox.insert(2,'Sandwich')
listBox.insert(3,'Burger')
listBox.insert(4,'Pizza')
listBox.insert(5,'Burrito')

label.pack()
listBox.pack()

root.mainloop()