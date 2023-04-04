from tkinter import *

root = Tk()
root.title('Tkinter Label Examples')

root.geometry("450x300")

user_name = Label(root, text = 'Username').place(x=40,y=60)
user_name_input_area = Entry(root,width=30).place(x=110,y=60)

user_password = Label(root, text = 'Password').place(x=40,y=100)
user_password_input_area = Entry(root,width=30).place(x=110,y=100)

submit_button = Button(root, text = 'Submit').place(x=40,y=130)

root.mainloop()