from tkinter import *
from tkinter.ttk import *

root = Tk()
root.title('Tkinter Radio Button Example')
root.geometry('175x175')

v=StringVar(root,"1")

style = Style(root)
style.configure('TRadiobutton',background='light green',
                foreground='red',font=('arial',10,'bold'))

values={'Radiobutton 1':'1',
        'Radiobutton 2':'2',
        'Radiobutton 3':'3',
        'Radiobutton 4':'4',
        'Radiobutton 5':'5',}

for(text,value) in values.items():
    Radiobutton(root,text=text,variable=v,value=value).pack(side='top',ipady=5)

root.mainloop()