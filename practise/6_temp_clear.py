import os
import shutil
from tkinter import *
import send2trash

root= Tk()
root.geometry("400x200")
root.title("Clear Temp files")
def deletefile():
   path=r"C:\Users\user\AppData\Local\Temp"
   for file in os.listdir(path):
      address=os.path.join(path,file)
      try:
         if os.path.isfile(address):
            os.remove(address)
         elif os.path.isdir(address):
            shutil.rmtree(address)
      except Exception as e:
         print(f"{file}")

Button(text="Clear Temp",command=deletefile).pack()
root.mainloop()