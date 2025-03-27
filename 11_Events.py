from tkinter import *

def temp(event):
    print(f"Cordinates are {event.x} and {event.y}")

root=Tk()
root.geometry("600x3f00")
root.title("Events in Tkinter")

widget = Button(text="Click me")
widget.pack()

widget.bind('<Button-1>',temp)
widget.bind('<Double-1>',quit)

# there are more events also
# https://python-course.eu/tkinter/events-and-binds-in-tkinter.php



root.mainloop()