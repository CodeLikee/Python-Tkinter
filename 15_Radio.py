from tkinter import *
import tkinter.messagebox as tmsg
root= Tk()
root.geometry("700x400")
root.title("Radio Button")

def takeorder():
    tmsg.showinfo("Order!!!",f"You ordered {option.get()}")

Label(root,text="What do you want to eat?",font="comicansms 20 bold",bg="red",fg="yellow").pack()
option= StringVar()
option.set("Nome")
radio=Radiobutton(root,text="Roti",variable=option,value="Roti").pack(anchor="w")
radio=Radiobutton(root,text="Paratha",variable=option,value="Paratha").pack(anchor="w")
radio=Radiobutton(root,text="IceCream",variable=option,value="IceCream").pack(anchor="w")
radio=Radiobutton(root,text="PaniPuri",variable=option,value="PaniPuri").pack(anchor="w")

Button(root,text="Place Order",command=takeorder).pack()

root.mainloop()