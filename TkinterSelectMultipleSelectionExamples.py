from tkinter import *

root = Tk()
root.title('Select Multiple Selection Example')
root.geometry('100x150')

list = Listbox(root,selectmode='multiple')
list.pack(expand=YES,fill=BOTH)

x=['c','c++','java','python','r','go','ruby','javascript','swift']

for each_item in range(len(x)):
    list.insert(END,x[each_item])
    list.itemconfig(each_item,bg='yellow' if each_item % 2 == 0 else 'cyan')

root.mainloop()