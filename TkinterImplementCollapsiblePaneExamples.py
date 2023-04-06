from tkinter import *
from tkinter.ttk import *
from CollapsiblePane import CollapsiblePane as cp

root = Tk()
root.title('Implement CollapsiblePane')
root.geometry('200x200')

cpane=cp(root,'Expanded','Collapsed')
cpane.grid(row=0,column=0)

b1 = Button(cpane.frame,text='btn').grid(row=1,column=2,pady=10)
cb1= Checkbutton(cpane.frame,text='chk').grid(row=2,column=3,pady=10)

root.mainloop()