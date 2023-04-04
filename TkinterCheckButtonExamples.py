from tkinter import *
from tkinter.ttk import *

root = Tk()
root.title('Check Button Examples')
root.geometry('300x200')

w = Label(root, text = 'Check Button Sample',font="50")
w.pack()

Checkbutton1 = IntVar()
Checkbutton2 = IntVar()
Checkbutton3 = IntVar()

chk1 = Checkbutton(root, text = 'Tutorial',
              variable=Checkbutton1,
              onvalue=1,
              offvalue=0,
              width=10)

chk2 = Checkbutton(root, text = 'Student',
              variable=Checkbutton2,
              onvalue=1,
              offvalue=0,
              width=10)

chk3 = Checkbutton(root, text = 'Course',
              variable=Checkbutton3,
              onvalue=1,
              offvalue=0,
              width=10)

chk1.pack()
chk2.pack()
chk3.pack()

root.mainloop()