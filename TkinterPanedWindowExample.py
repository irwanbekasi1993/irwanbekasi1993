from tkinter import *
from tkinter.ttk import *

root = Tk()
root.title('PanedWindow Example')

pw = PanedWindow(orient='vertical')

top=Button(pw,text='Click Here')
top.pack(side=TOP)
pw.add(top)

bot = Checkbutton(pw,text='Choose Me')
bot.pack(side=TOP)
pw.add(bot)

label=Label(pw,text='Label Here')
label.pack(side=TOP)
pw.add(label)

string=StringVar()

entry=Entry(pw,textvariable=string,font=('arial',15,'bold'))
entry.pack()
entry.focus_force()
pw.add(entry)

pw.pack(fill=BOTH,expand=True)


root.mainloop()