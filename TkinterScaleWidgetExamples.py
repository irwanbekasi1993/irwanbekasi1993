from tkinter import *

root = Tk()
root.title('Scale Widget Example')

root.geometry('400x300')

v1 = DoubleVar()
v2 = DoubleVar()

# def show1():
sel='Horizontal Scale Value= '+str(v1.get())
l1 = Label(root)
l1.config(text=sel,font=('Courier',14))
l3 = Label(root,text='Horizontal Scaler')
s1 = Scale(root,variable=v1,from_=1,to=100,orient=HORIZONTAL)
b1 = Button(root,text='Display Horizontal',bg='yellow')

s1.pack(anchor=CENTER)
l3.pack()
b1.pack(anchor=CENTER)
l1.pack()

# def show2():
sel='Vertical Scale Value= '+str(v2.get())
l2 = Label(root)
l2.config(text=sel,font=('Courier',14))

l4 = Label(root, text='Vertical Scaler')
b2 = Button(root,text='Display Vertical', bg='purple',fg='white')

s2 = Scale(root,variable=v2,from_=50,to=1,orient=VERTICAL)

s2.pack(anchor=CENTER)
l4.pack()
b2.pack()
l2.pack()

root.mainloop()