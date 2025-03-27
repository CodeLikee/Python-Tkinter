from tkinter import *
root=Tk()
root.geometry("600x400")
root.title("TextBox")

sb= Scrollbar(root)
sb.pack(side=RIGHT,fill=Y)

text1=Text(root,yscrollcommand=sb.set)
text1.pack(fill=BOTH)

sb.config(command=text1.yview)

root.mainloop()