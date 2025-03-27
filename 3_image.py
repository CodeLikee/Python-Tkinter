from tkinter import *
from PIL import Image, ImageTk


n_root=Tk()

n_root.geometry("900x500")   

na =Label(text="Now we place a image in it")
na.pack()

photo=PhotoImage(file='zimage.png',width=900,height=800)       

# for jpeg images  ( pip install pillow)
# image1=Image.open("zprofile_photo.jpg")
# photo= ImageTk.PhotoImage(image1)

t=Label(image=photo)
t.pack()



# image=Image.open('zprofile_photo.jpg')

n_root.mainloop()