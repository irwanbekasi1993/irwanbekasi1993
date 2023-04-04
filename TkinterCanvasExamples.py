from tkinter import *
from tkinter.ttk import *

root = Tk()
root.title('Canvas Example')
#draw automatically
c = Canvas(root,bg='yellow',height=250,width=300)
line = c.create_line(108,120,320,40,fill='green')
arc = c.create_arc(180,150,80,210,start=0,extent=220,fill='red')
oval=c.create_oval(80,30,140,150,fill='blue')
rect = c.create_rectangle(230,10,290,60, fill='blue')
points = [150,100,200,120,240,180,
          210,200,150,150,100,200]
polygon = c.create_polygon(points,fill='orange')
c.pack()

#draw manually
def paint(event):
    x1,y1,x2,y2=(event.x-3),(event.y-3),(event.x+3),(event.y+3)
    Colour="#000fff000"
    w.create_line(x1,y1,x2,y2,fill=Colour)

w=Canvas(root,width=400,height=250)
w.bind('<B1-Motion>',paint)

l=Label(root,text='double click and drag to draw')
l.pack()
w.pack()



root.mainloop()