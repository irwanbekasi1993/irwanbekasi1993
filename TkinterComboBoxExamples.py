from tkinter import *
from tkinter.ttk import *

root = Tk()
root.title('Combo Box Example')
root.geometry('500x250')

Label(root, text = 'Combo Box Sample',background='green',foreground='white',
      font=('Times New Roman',15)).grid(row=0,column=1)

Label(root, text = 'Select Month: ',font=('Times New Roman',10)).grid(
    row = 5, column = 0,padx=10,pady=25)

n=StringVar()
monthChoosen=Combobox(root,width=27,textvariable=n)

monthChoosen['values']=('January','February',
                        'March','April',
                        'May','June','July',
                        'September','October',
                        'November','December')

monthChoosen.grid(column=1,row=5)
monthChoosen.current()

root.mainloop()