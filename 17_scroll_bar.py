from tkinter import *
root=Tk()
root.geometry("600x400")
root.title("ScrollBar")
# for connecting  scrollbar to a widget
# 1. widget(yscrollcommand = scrollbar.set)
# 2. scrollbar.config(command = widget.yview)

sb= Scrollbar(root)  # creating scroll bar
sb.pack(side=RIGHT,fill=Y)

# creating a widget
lbx=Listbox(root,yscrollcommand=sb.set)
for i in range(100):
    lbx.insert(END,f"Item {i}")
lbx.pack(fill=BOTH)
sb.config(command=lbx.yview)

root.mainloop()