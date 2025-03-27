from tkinter import *

root=Tk()
root.title("Frame")
root.geometry("1200x400")

frm=Frame(root,bg="green",borderwidth=30,relief=SUNKEN)
frm.pack(fill=X)

#  creating buttons      ( all parameter are aplicable of frame lablel pack)

but=Button(frm,fg="red",text="hello world")
but.pack(side=LEFT)
 
but1=Button(frm,fg="red",text="hello world")
but1.pack(side=LEFT)
 
# command             ( only gave name of function)
def grp():
    print("it work")
but2=Button(frm,fg="red",text="Command here",command=grp)
but2.pack(side=LEFT,padx=30)
 


root.mainloop()
