from tkinter import*

root=Tk()
root.geometry("600x400")
root.title("Form of students")

Label(root,text="Welcome to data Center",font="comicsansms 19 bold").grid(row=0,column=3)

roll=Label(root,text="Roll No.")
name=Label(root,text="Name")
marks=Label(root,text="Marks")

roll.grid(row=1,column=1)
name.grid(row=2,column=1)
marks.grid(row=3,column=1)

rollvalue=StringVar()
namevalue=StringVar()
marksvalue=StringVar()

rollentry=Entry(root,textvariable=rollvalue).grid(row=1,column=2)
nameentry=Entry(root,textvariable=namevalue).grid(row=2,column=2)
marksentry=Entry(root,textvariable=marksvalue).grid(row=3,column=2)



root.mainloop()