from tkinter import *
root=Tk()
root.geometry("600x400")
root.title("Tips For Tkinter")

# to get the window or screen height and width
# width1= root.winfo_screenwidth()
# height1= root.winfo_screenheight()
# print(f"width is {width1}\nheight is {height1}")

# Destroy or Close the window
# Button(root,text="Close",command=root.destroy).pack()

# to get text of a button
def click(event):
    text=event.widget.cget("text")    
    print(text)

b=Button(root,text="hello")
b.bind("<Button-1>",click)
b.pack()


root.mainloop()