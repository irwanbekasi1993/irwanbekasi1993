from tkinter import *
from tkinter import colorchooser

root = Tk()
root.title('Color Chooser Example')
root.geometry('300x300')

def chooseColor():
    colorCode= colorchooser.askcolor(title='Choose Color')
    print(colorCode)

btn = Button(root,text='Select Color',command=chooseColor)
btn.pack()

root.mainloop()