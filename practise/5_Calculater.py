from tkinter import *
def calculator():
    root=Tk()
    root.geometry("450x415")
    root.title("Calculater")
    root.configure(background="darkblue")

    def click(event):
        global scvalue
        text=event.widget.cget("text")    
        if text=="=":
            if scvalue.get().isnumeric():
                value1=scvalue.get()
            else:
                try:
                    value1=eval(scvalue.get())
                except:
                    value1="Error...."
            scvalue.set(value1)
            screen.update()
        elif text=="Clear":
            scvalue.set("")
            screen.update()
        else:
            scvalue.set(scvalue.get()+text)
            screen.update()

    scvalue=StringVar()
    scvalue.set("")

    screen= Entry(root,textvariable=scvalue,font="lucida 20 bold")
    screen.pack(fill=X,side=TOP,ipadx=10,padx=10,pady=10)

    frame_= Frame(root,bg="red")
    frame_.pack(padx=10,anchor="nw")

    f1 = Frame(frame_,bg="red")
    f1.pack(padx=10,fill=X)
    f2 = Frame(frame_,bg="red")
    f2.pack(padx=10,fill=X)
    f3 = Frame(frame_,bg="red")
    f3.pack(padx=10,fill=X)
    f4 = Frame(frame_,bg="red")
    f4.pack(padx=10,fill=X)
    f5 = Frame(frame_,bg="red")
    f5.pack(padx=10,fill=X)
    f6 = Frame(frame_,bg="red")
    f6.pack(padx=10,fill=X)

    list1=[1,2,3,"+",4,5,6,"-",7,8,9,"*",0,"%",".","/"]
    list2=["Clear","="]
    butpadx=30
    butpady=5

    for i in list1[:4]:
        b=Button(f1,text=f"{i}",padx=butpadx,pady=butpady,font="comicansms 15 bold")
        b.bind("<Button-1>",click)
        b.pack(side=LEFT,padx=10,pady=10)
    for i in list1[4:8]:
        b=Button(f2,text=f"{i}",padx=butpadx,pady=butpady,font="comicansms 15 bold")
        b.bind("<Button-1>",click)
        b.pack(side=LEFT,padx=10,pady=10)
    for i in list1[8:12]:
        b=Button(f3,text=f"{i}",padx=butpadx,pady=butpady,font="comicansms 15 bold")
        b.bind("<Button-1>",click)
        b.pack(side=LEFT,padx=10,pady=10)
    for i in list1[12:17]:
        b=Button(f4,text=f"{i}",padx=butpadx,pady=butpady,font="comicansms 15 bold")
        b.bind("<Button-1>",click)
        b.pack(side=LEFT,padx=10,pady=10)
    for i in list2:
        b=Button(f5,text=f"{i}",padx=70,pady=butpady,font="comicansms 15 bold")
        b.bind("<Button-1>",click)
        b.pack(side=LEFT,padx=10,pady=10)
    root.mainloop()
calculator()