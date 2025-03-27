from tkinter import *
import time
root=Tk()
root.geometry("600x400")
root.title("Status Bar")

def csk():
    statusvar.set("Working...")
    sbar.update()
    time.sleep(1)
    statusvar.set("Done...")
    sbar.update()
    time.sleep(1)
    statusvar.set("Ready for next work")
statusvar= StringVar()
statusvar.set("Ready")

sbar=Label(root,textvariable=statusvar,relief=SUNKEN,anchor=W)
sbar.pack(fill=BOTH,side=BOTTOM)

Button(root,text="Start",command=csk).pack()

root.mainloop()