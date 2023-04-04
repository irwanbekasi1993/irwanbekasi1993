from tkinter import *
from tkinter.ttk import *

root = Tk()
root.title('Image In Button')

Label(root, text = 'Display image',font=('Verdana',15)).pack(side='top',pady=10)

photo = PhotoImage(file=r"HTML5_badge.png")

photoImage = photo.subsample(3,3)

Button(root, text = 'Display Image', image=photoImage,compound='left').pack(side='top')

root.mainloop()