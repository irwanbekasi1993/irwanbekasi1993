from tkinter import *
from tkinter.ttk import *

root = Tk()
root.title('Label Frame Example')
root.geometry("300x300")

label_frame = LabelFrame(root,text='This Is Label Frame')
label_frame.pack(expand='yes',fill='both')

label1 = Label(root, text = '1. This Is First Label')
label1.place(x=0,y=15)

label2 = Label(root, text = '2. This Is Second Label')
label2.place(x=0,y=35)

label3 = Label(root, text = '3. This Is Third Label')
label3.place(x=0,y=55)

btn1 = Button(root, text = 'Button 1')
btn1.place(x=0, y=75)

btn2 = Button(root, text = 'Button 2')
btn2.place(x=0, y=105)

btn1 = Checkbutton(root, text = 'CheckButton 1')
btn1.place(x=0, y=135)

btn2 = Checkbutton(root, text = 'CheckButton 2')
btn2.place(x=0, y=155)

root.mainloop()