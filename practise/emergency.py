from tkinter import *
from time import *
root=Tk()
screen_width=900
screen_height=600
root.geometry(f"{screen_width}x{screen_height}")


def updatetime():
    tim = strftime("%I:%M:%S")
    clock.config(text=tim)


clock = Label(root,text="hello")
clock.pack()
updatetime()



root.mainloop()