from tkinter import *

n_root=Tk()

# used to set of open gui
n_root.geometry("500x500")    # take size as width x height

# set minimum size 
n_root.minsize(200,200)       # width,height     

# set max size
n_root.maxsize(1200,600)

na =Label(text="hello that is my first GUI")
na.pack() # without pack item not visible 

n_root.mainloop()