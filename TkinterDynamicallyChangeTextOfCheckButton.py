from tkinter import *
from tkinter.ttk import *
from tkinter.messagebox import _show

root = Tk()
root.title('Dynamically Change Text Of Check Button')
root.geometry('200x100')

text1=StringVar()
text2=StringVar()

text1.set('OFF')
text2.set('OFF')

def show(event):
    string=event.get()
    _show('Message','You Select: '+string)

chkbtn1=Checkbutton(root,textvariable=text1,variable=text1,offvalue='Not Selected',onvalue='Selected',command=lambda:show(text1))
chkbtn1.pack(side=TOP,pady=10)

chkbtn2 = Checkbutton(root,textvariable=text2,variable=text2,offvalue='Average',onvalue='Good',command=lambda:show(text2))
chkbtn2.pack(side=TOP,pady=10)


root.mainloop()