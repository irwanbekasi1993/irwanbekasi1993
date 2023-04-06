from tkinter import *
from tkinter import messagebox

root = Tk()
root.title('Ask Dialog Message Box Example')
root.geometry('150x120')

def question1():
    messagebox.askquestion('Form','Is Your Name Correct?',icon='error')

def question2():
    messagebox.askquestion('Form','Do You Want To Continue?',icon='info')

def question3():
    messagebox.askquestion('Form','Are You 18+?',icon='question')

def question4():
    messagebox.askquestion('Form','What Is Your Gender?',icon='error')

B1= Button(root,text='Check Question 1',command=question1)
B2= Button(root,text='Check Question 2',command=question2)
B3= Button(root,text='Check Question 3',command=question3)
B4= Button(root,text='Check Question 4',command=question4)

B1.pack()
B2.pack()
B3.pack()
B4.pack()

root.mainloop()