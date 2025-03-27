from tkinter import *

def grp():
    print(f"user : {uservalue.get()}")
    print(f"password : {passvalue.get()}")

root=Tk()
root.geometry("800x200")
root.title("Input String")

user=Label(root,text="UserName")
password=Label(root,text="Password")

user.grid()
password.grid()


uservalue=StringVar()
passvalue=StringVar()

userentry=Entry(root,textvariable=uservalue)
passentry=Entry(root,textvariable=passvalue)

userentry.grid(row=0,column=1)
passentry.grid(row=1,column=1)

Button(text="Submit",command=grp).grid(row=3,column=3)





root.mainloop()