from tkinter import *

Num_Vertical = ("\nA\nB\nC\nD\nE\nF\nG\n\
H\nI\nJ\nK\nL\nM\nN\nO\nP\nQ\nR\nS\nT\n\
U\nV\nW\nX\nY\nZ")
Num_Horizontal = ("A  B  C  D  E  F  G  H \
I  J  K  L  M  N  O  P  Q  R  S  T  U  V \
W  X  Y  Z")

root = Tk()
root.title('Double Scrollable')
root.geometry('250x200')

SVBar = Scrollbar(root)
SVBar.pack(side=RIGHT,fill='y')

SHBar = Scrollbar(root,orient='horizontal')
SHBar.pack(side=BOTTOM,fill='x')

TBox = Text(root,height=500,width=500,yscrollcommand=SVBar.set,xscrollcommand=SHBar.set,wrap='none')
TBox = Text(root,height=500,width=500,yscrollcommand=SVBar.set,xscrollcommand=SHBar.set,wrap='none')

TBox.pack(expand=0,fill=BOTH)

TBox.insert(END,Num_Horizontal)
TBox.insert(END,Num_Vertical)

SHBar.config(command=TBox.xview)
SVBar.config(command=TBox.yview)

root.mainloop()