from tkinter import *
import time

root=Tk()
root.geometry("1000x600")   

root.title("hello world")
for i in range(10):
    time.sleep(1)
    nav =Label(text=f"how are you {i}",bg='red',font="comicsansms 19")
    nav.pack()
root.mainloop()