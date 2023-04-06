from tkinter import *
from PIL import Image,ImageTk
import os

root = Tk()
root.title('reading image example')

img = ImageTk.PhotoImage(Image.open("OIP_3.jpg"))

panel=Label(root,image=img)
panel.pack(side='bottom',fill='both',expand='yes')

#using canvas for fix size
# canvas = Canvas(root,width=500,height=250)
# canvas.pack()
# canvas.create_image(135,20,anchor=NW,image=img)
root.mainloop()