from tkinter import *
import time
root=Tk()
root.geometry("600x400")
root.title("Status Bar")

statusvar= StringVar()
statusvar.set("Ready")
def csk():
    for i in range(10):
        sbar.update()
        statusvar.set(f"Item {i}")
        time.sleep(1)

sbar=Label(root,textvariable=statusvar,relief=SUNKEN,anchor=W)
sbar.pack(fill=BOTH,side=BOTTOM)
Button(root,text="Start",command=csk).pack()
root.mainloop()