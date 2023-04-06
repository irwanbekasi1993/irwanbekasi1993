from tkinter import *

def checkKey(event):
    value=event.widget.get()
    print('your search is: '+value)

    if value == '':
        data = l
    else:
        data=[]
        for item in l:
            if value.lower() in item.lower():
                data.append(item)

    update(data)

def update(data):
    lb.delete(0,'end')
    for item in data:
        lb.insert('end',item)

l=('C','C++','Java','Python','Perl','PHP','ASP','JS')

root = Tk()
root.title('Autocomplete Combobox')

e=Entry(root)
e.pack()
e.bind('<KeyRelease>',checkKey)

lb = Listbox(root)
lb.pack()
update(l)

root.mainloop()