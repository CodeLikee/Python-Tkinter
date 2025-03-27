from tkinter import *
from time import *
root=Tk()
screen_width=900
screen_height=600
root.geometry(f"{screen_width}x{screen_height}")
root.resizable(False,False)
def updatetime():
    tim = strftime("%I:%M:%S")
    clock.config(tim)


clockfrm = Frame(bg="green",borderwidth=0)
clockfrm.place(x=screen_width/2-150,y=100,width=300,height=80)

clock = Label(clockfrm,text="hello")
clock.pack()
updatetime()



root.mainloop()