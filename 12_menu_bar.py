from tkinter import *

def csk():
    print("CSK wins the Match")
root= Tk()
root.geometry("700x400")
root.title("Menu Setup")

# Use it for non dropdown Menu
# Mymenu=Menu(root)
# Mymenu.add_command(label="File",command=csk)
# Mymenu.add_command(label="Exit",command=quit)
# root.config(menu=Mymenu)

# for drop down Menu
mainmenu=Menu(root)

m1=Menu(mainmenu, tearoff=0)
m1.add_command(label="New",command=csk)
m1.add_command(label="Save",command=csk)
m1.add_separator() # use to make a seprate line
m1.add_command(label="Exit",command=quit)

root.config(menu=mainmenu)
mainmenu.add_cascade(label="File",menu=m1)
mainmenu.add_cascade(label="File1",menu=m1)




root.mainloop()