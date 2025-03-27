from tkinter import *
import tkinter.messagebox as tmsg

def csk():
    print("CSK wins the Match")
root= Tk()
root.geometry("700x400")
root.title("Dialog Box")

mainmenu=Menu(root)

m1=Menu(mainmenu, tearoff=0)
m1.add_command(label="New",command=csk)
m1.add_command(label="Save",command=csk)
m1.add_separator() 
m1.add_command(label="Exit",command=quit)

def help():
    tmsg.showinfo("Hellp","Thank For Help!!!")
def ques():
    ans=tmsg.askquestion("Is EveryThing OK!!!","Is EveryThing OK!!!")
    if ans=="yes":
        tmsg.showinfo("Request","Thank please rate the app on playstore")
    else:
        tmsg.showinfo("Request","Please dont rate my app")
def ques1():
    ans=tmsg.askretrycancel("Is EveryThing OK!!!","You can retry")
    if ans:         # it returns true or false
        tmsg.showinfo("Error","Sorry their is a problem")
    else:
        tmsg.showinfo("Your Choice","you cancelled it")

m2=Menu(mainmenu, tearoff=0)
m2.add_command(label="help",command=help)
m2.add_command(label="OK",command=ques)
m2.add_command(label="Retry",command=ques1)
m2.add_command(label="Exit",command=quit)

root.config(menu=mainmenu)
mainmenu.add_cascade(label="File",menu=m1)
mainmenu.add_cascade(label="Help",menu=m2)
root.mainloop()