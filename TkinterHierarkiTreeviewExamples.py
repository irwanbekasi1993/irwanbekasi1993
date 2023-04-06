from tkinter import *
from tkinter.ttk import *

root = Tk()
root.title('Hierarchical Tree View')

Label(root,text='Hierarchical Tree View').pack()

treeView = Treeview(root)

treeView.pack()

treeView.insert('',0,'item1',text='Sample')

treeView.insert('',1,'item2',text='Sub Sample1')
treeView.insert('',2,'item3',text='Sub Sample2')
treeView.insert('','end','item4',text='Sub Sample3')

treeView.insert('item2','end','Main Sub Category 1',text='Main Sub Category 1')
treeView.insert('item2','end','Main Sub Category 2',text='Main Sub Category 2')
treeView.insert('item3','end','Main Sub Category 3',text='Main Sub Category 3')
treeView.insert('item3','end','Main Sub Category 4',text='Main Sub Category 4')
treeView.insert('item4','end','Main Sub Category 5',text='Main Sub Category 5')
treeView.insert('item4','end','Main Sub Category 6',text='Main Sub Category 6')

treeView.move('item2','item1','end')
treeView.move('item3','item1','end')
treeView.move('item4','item1','end')

root.mainloop()