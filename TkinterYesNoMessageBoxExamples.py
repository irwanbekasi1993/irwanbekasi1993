from tkinter import *
from tkinter import messagebox as mb

def call():
    res=mb.askquestion('Exit Application?',
                       'Do You Really Want To Exit?')
    if res == 'yes' :
        root.destroy()
    else:
        mb.showinfo('Return','Returning To Main Application')

root = Tk()
root.title('Yes No Message Box Example')
canvas= Canvas(root,width=200,height=200)
canvas.pack()

b= Button(root,text='Quit Application',command=call)

canvas.create_window(100,100,window=b)


root.mainloop()