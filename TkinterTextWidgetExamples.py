from tkinter import *
from tkinter.ttk import *

root = Tk()
root.title('Text Widget Example')
root.geometry('300x300')

def takeInput():
    input= inputText.get('1.0','end-1c')
    print(input)
    if(input == '120'):
        output.insert(END,'Correct')
    else:
        output.insert(END,'Wrong Answer')

l=Label(text='What is 24 * 5?')
inputText = Text(root,height=10,width=25,bg='light yellow')
output = Text(root,height=5,width=25,bg='light cyan')
display= Button(root,width=20,text='Show',command=lambda:takeInput())

l.pack()
inputText.pack()
display.pack()
output.pack()

root.mainloop()