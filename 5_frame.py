from tkinter import *

root=Tk()
root.title("Frame")
root.geometry("1200x600")
    
# cr    eating a frame
f1 = Frame(root,bg="green",borderwidth=20,relief=SUNKEN)
f1.pack(side=LEFT,fill=Y)

f2 = Frame(root,bg="blue",borderwidth=20,relief=SUNKEN)
f2.pack(fill=X)

na= Label(f1, text="hello frame 1 is here",bg="red",pady=200)
na.pack()

na1= Label(f2, text="hello frame 2 is here",bg="yellow",font="Helvetica 16 bold",fg="red",pady=100)
na1.pack(pady=50)






root.mainloop()