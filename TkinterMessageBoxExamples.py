from tkinter import *
from tkinter import messagebox

root = Tk()
root.title('Message Box Example')
root.geometry('150x120')

def showMessageBox():
    messagebox.showinfo('showInfo','Information')
    messagebox.showerror('showError','Information')
    messagebox.showwarning('showWarning','Information')
    messagebox.askquestion('askQuestion','Information')
    messagebox.askokcancel('askOkCancel','Information')
    messagebox.askyesno('askYesNo','Information')
    messagebox.askretrycancel('askRetryCancel','Information')

btn= Button(root,text='Show Messagebox',command=showMessageBox)

btn.pack()

root.mainloop()