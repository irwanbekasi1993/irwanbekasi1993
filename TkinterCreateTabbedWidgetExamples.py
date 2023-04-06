import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title('Create Tabbed Widget Example')

tabControl = ttk.Notebook(root)

tab1=ttk.Frame(tabControl)
tab2=ttk.Frame(tabControl)

tabControl.add(tab1,text='Tab1')
tabControl.add(tab2,text='Tab2')
tabControl.pack(expand=1,fill='both')

ttk.Label(tab1,text='TAB1').grid(column=0,row=0,padx=30,pady=30)
ttk.Label(tab2,text='TAB2').grid(column=0,row=0,padx=30,pady=30)

root.mainloop()