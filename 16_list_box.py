from tkinter import *

root= Tk()
root.geometry("700x400")
root.title("List Box")
i=0
def add():
   global i
   lbx.insert(ACTIVE,f"{i}") # insert after you selected
   #lbx.insert(f"{i}") 
   i+=1

Label(root,text="This is a list box",font="comicansms 20 bold",bg="red",fg="white").pack()

lbx=Listbox(root)
lbx.pack()

lbx.insert(END,"First Element")


Button(root,text="Add",command=add).pack()

root.mainloop()