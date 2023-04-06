from tkinter import *
from tkinter.ttk import *

root = Tk()
root.title('Opening New Window')
root.geometry('200x200')

def openWindow():
    newWindow = Toplevel(root)
    newWindow.title('New Window')
    newWindow.geometry('200x200')
    Label(newWindow,text='This is New Window').pack()

label = Label(root,text='This Is main Window')
label.pack(pady=10)

btn = Button(root,text='Click here',command=openWindow)
btn.pack(pady=10)

root.mainloop()