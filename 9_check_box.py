from tkinter import*

root=Tk()
root.geometry("600x400")
root.title("Form of students")

def savee():
    with open("data.txt","a") as f:
        f.write(f"{rollvalue.get()} {namevalue.get()} {marksvalue.get()} {notrob.get()}\n")
        



Label(root,text="Welcome to data Center",font="comicsansms 19 bold").grid(row=0,column=5)

roll=Label(root,text="Roll No.")
name=Label(root,text="Name")
marks=Label(root,text="Marks")

roll.grid(row=1,column=3)
name.grid(row=2,column=3)
marks.grid(row=3,column=3)

rollvalue=StringVar()
namevalue=StringVar()
marksvalue=StringVar()
notrob=IntVar()

rollentry=Entry(root,textvariable=rollvalue).grid(row=1,column=4)
nameentry=Entry(root,textvariable=namevalue).grid(row=2,column=4)
marksentry=Entry(root,textvariable=marksvalue).grid(row=3,column=4)

# check box

notrobcheck=Checkbutton(text="You are not a Robot",variable=notrob)
notrobcheck.grid(row=5,column=4)

Button(text="Submit",command=savee).grid(row=6,column=4)

root.mainloop()