from tkinter import *

root=Tk()
root.geometry("1200x800")
root.title("Grid and Widgets")

user=Label(root,text="Username")
password=Label(root,text="Password")

user.grid(row=1)
password.grid(column=1,row=1)

root.mainloop()