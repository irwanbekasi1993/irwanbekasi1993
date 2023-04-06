from tkinter import *

class ScrollBar:
    def __init__(self) -> None:
        root = Tk()
        h= Scrollbar(root,orient='horizontal')
        h.pack(side=BOTTOM,fill=X)
        v=Scrollbar(root)
        v.pack(side=RIGHT,fill=Y)
        t=Text(root,width=15,height=15,wrap=None,
               xscrollcommand=h.set, yscrollcommand=v.set)
        for i in range(20):
            t.insert(END,'abcdefghijklmnopqrstuvwxyz1234567890')

        t.pack(side=TOP,fill=X)
        h.config(command=t.xview)
        v.config(command=t.yview)

        mainloop()

s=ScrollBar()