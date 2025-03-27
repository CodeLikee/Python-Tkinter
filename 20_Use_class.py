from tkinter import *

class GUI (Tk):
    def __init__(self):
        super().__init__()
        self.geometry("800x500")
    def status(self):
        self.var=StringVar()
        self.var.set("Ready")
        self.statusbar = Label(self,textvariable=self.var,relief=SUNKEN,anchor="w")
        self.statusbar.pack(side=BOTTOM,fill=X)
    def cliked(self):
        print("Button is clicked")
    def createbutton(self,inptext):
        Button(text=inptext,command=self.cliked).pack()
if __name__ == '__main__':
    window=GUI()
    window.status()
    window.createbutton("Login")
    window.createbutton("Sign In")
    window.mainloop()