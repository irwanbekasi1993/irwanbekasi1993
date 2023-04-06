from tkinter import *
from tkinter.ttk import *
from tkinter.filedialog import *

root = Tk()
root.title('Ask Open File Example')
root.geometry('200x100')

def openFile():
    file = askopenfile(mode='r',filetypes=[('Python Files','*.py')])
    if file is not None:
        content = file.read()
        print(content)

btn = Button(root,text='Open File',command=lambda:openFile())
btn.pack(side=TOP,pady=10)

root.mainloop()