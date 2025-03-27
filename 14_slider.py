from tkinter import *
root= Tk()
root.geometry("700x400")
root.title("Slider")

# myslider= Scale(root,from_=0,to=10,width=30)
# myslider.pack()
# for horizantal slider
# myslider= Scale(root,from_=0,to=10,orient=HORIZONTAL,width=30)
# myslider.pack()

# taking values
def rateyou():
    print(f"you rated {myslider.get()}")
Label(root,text="Rate YourSelf:").pack()
myslider= Scale(root,from_=0,to=10,orient=HORIZONTAL,width=30,tickinterval=2)
myslider.set(9)
myslider.pack()
Button(root,text="Submit",command=rateyou).pack()

root.mainloop()