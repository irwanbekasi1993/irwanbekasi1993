from tkinter import *

root = Tk()
root.title('Frame Widget Example')
root.geometry('300x150')

w = Label(root, text = 'Frame Widget',font=50)
w.pack()

frame = Frame(root)
frame.pack()

bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)

btn1= Button(frame,text='btn1',fg='red')
btn1.pack(side=LEFT)

btn2= Button(frame,text='btn2',fg='brown')
btn2.pack(side=LEFT)

btn3= Button(frame,text='btn3',fg='blue')
btn3.pack(side=LEFT)

btn4= Button(bottomFrame,text='btn4',fg='green')
btn4.pack(side=BOTTOM)

btn5= Button(bottomFrame,text='btn5',fg='green')
btn5.pack(side=BOTTOM)

btn6= Button(bottomFrame,text='btn6',fg='green')
btn6.pack(side=BOTTOM)

root.mainloop()