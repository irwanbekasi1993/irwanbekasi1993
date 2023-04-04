from tkinter import *
from tkinter.ttk import *

root = Tk()
root.title('Create button In Tkinter')

root.geometry('100x100')

#styling
style = Style()

style.configure('W.TButton',font=('calibri',10,'bold','underline'),foreground='red')

btn = Button(root, text = 'Click Me', command = root.destroy)
btn.grid(row = 0, column = 3,padx=100)

btn1 = Button(root, text = 'Quit!', command = root.destroy, style='W.TButton')
btn1.grid(row = 1, column = 3,padx=100)

btn2 = Button(root, text = 'Click This', command = None)
btn2.grid(row = 2, column = 3,pady=10,padx=100)

root.mainloop()