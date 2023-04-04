from tkinter import *
from tkinter.ttk import *

class Action:
    def __init__(self,root=None):
        self.x=1
        self.y=0
        self.canvas=Canvas(root)
        self.rectangle=self.canvas.create_rectangle(5,5,25,25,fill='black')
        self.canvas.pack()
        self.movement()

    def movement(self):
        self.canvas.move(self.rectangle,self.x,self.y)
        self.canvas.after(100,self.movement)

    def left(self,event):
        print(event.keysym)
        self.x=-5
        self.y=0

    def right(self,event):
        print(event.keysym)
        self.x=5
        self.y=0

    def up(self,event):
        print(event.keysym)
        self.x=0
        self.y=-5

    def down(self,event):
        print(event.keysym)
        self.x=0
        self.y=5

if __name__=="__main__":
    root = Tk()
    runner = Action(root)
    root.title('Moving Objects Examples')
    root.bind('<KeyPress-Left>',lambda e: runner.left(e))
    root.bind('<KeyPress-Right>',lambda e:runner.right(e))
    root.bind('<KeyPress-Up>',lambda e:runner.up(e))
    root.bind('<KeyPress-Down>',lambda e:runner.down(e))

    root.mainloop()