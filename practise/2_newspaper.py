from tkinter import *

root=Tk()
root.geometry("800x600")
root.maxsize(1200,900)
root.title('Newspaper')
head=Label(text="Newspaper",fg='red',font="comicansms 30 bold italic underline")
head.pack()

photo=PhotoImage(file="zimage.png",width=500,height=200)
t=Label(image=photo)
t.pack()

news=Label(text="did you know about what is that???",fg='darkblue',font="comicansms 19")
news.pack()

root.mainloop()