from tkinter import *

def change():
    try:
        root.geometry(f"{widthh.get()}x{heightt.get()}")
    except:
        pass

root=Tk()
root.geometry("500x400")
Label(root,text="Lets Change size!!!",font="comicansms 19 bold").grid(row=0,column=2)

Label(root,text="Enter Width:",font="comicansms 19 bold").grid(row=1,column=2)
Label(root,text="Enter Hight:",font="comicansms 19 bold").grid(row=2,column=2)

widthh=StringVar()
heightt=StringVar()

Entry(root,textvariable=widthh).grid(row=1,column=3)
Entry(root,textvariable=heightt).grid(row=2,column=3)

Button(text="Change It",font="Comicansms 19 bold",command=change).grid(row=4,column=3)
root.mainloop()