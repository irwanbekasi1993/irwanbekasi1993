import tkinter

class A:
    def __init__(self):
        self.root = tkinter.Tk()
        self.root.geometry('500x500')
        self.frame1=tkinter.Label(self.root,width=400,height=400,bg='#AAAAAA')
        self.frame1.pack()

    def popup(self):
        self.popupMenu = tkinter.Menu(self.root,tearoff=0)
        self.popupMenu.add_command(label='say hi',command=lambda:self.hey('hi'))
        self.popupMenu.add_command(label='say hello',command=lambda:self.hey('hi'))
        self.popupMenu.add_separator()
        self.popupMenu.add_command(label='say bye',command=lambda:self.hey('hi'))

    def doPopUp(self,event):
        try:
            self.popupMenu.tk_popup(event.x_root,event.y_root)
        finally:
            self.popupMenu.grab_release()

    def hey(self,s):
        self.frame1.configure(text=s)

    def run(self):
        self.popup()
        self.root.bind("<Button-3>",self.doPopUp)
        tkinter.mainloop()

a=A()
a.run()