from tkinter import *

root=Tk()
root.title("Shapes")
canvas_width=1000
canvas_height=600

root.geometry(f"{canvas_width}x{canvas_height}")

can_widget = Canvas(root,width=canvas_width,height=canvas_height)
can_widget.pack()

# x1 y1 and x2 y2 cordinate has to give 
can_widget.create_line(0,0,1000,600,fill="red")
can_widget.create_line(0,600,1000,0)

# top left and bottom right
can_widget.create_rectangle(5,6,100,100)

# create text
can_widget.create_text(200,200,text="hello!")

# oval take as rectangle points
can_widget.create_oval(5,6,100,100,fill="blue")


root.mainloop()