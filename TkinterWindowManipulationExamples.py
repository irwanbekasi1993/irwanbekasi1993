from tkinter import *
from tkinter.ttk import *

root = Tk()
root.title('window manipulation')

#maximize
root.maxsize(500,500)
#minimize
root.minsize(150,100)
#resizeable
root.resizable(True,True)

Label(root, text = 'Maximize It',font=('Verdana',15)).pack(
    side='top',pady=10
)
Button(root, text = 'Maximize It').pack(side='top')
root.mainloop()