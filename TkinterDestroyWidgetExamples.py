from tkinter import *
from tkinter.ttk import *

root = Tk()
root.title('Destroy Widget Example')

btn1= Button(root,text='Button1')
btn1.pack(pady=10)

btn2= Button(root,text='Button2')
btn2.pack(pady=10)

btn1.after(3000,btn1.destroy)
btn2.after(6000,btn2.destroy)

root.mainloop()