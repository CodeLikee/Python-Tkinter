from tkinter import *

root=Tk()
root.geometry("1000x600")   

root.title("hello world")
# improtant label options
'''text - adds the text
font - sets the font 
        1. font=("comicsansms",20,"bold")
        2. font="comicsansms 20 bold italic underline" 
bd - background
fg - foreground
padx - x padding        
pady - y padding
relief - border styling - SUNKEN(solid border), RAISED, GROOVE, RIDGE
'''
title_label =Label(text = '''Lorem ipsum dolor sit amet consectetur\n adipisicing elit.Nam magnam illo recusandae.\n Quasi reprehenderit laborum tenetur, qui optio \nodio assumenda nesciunt doloribus facilis sit?\n Aspernatur minima saepe officia sunt provident\n quis accusamus odio culpa.''', bg='red', fg='aqua', padx= 10, pady= 5, font="comicsansms 9 bold", borderwidth=30, relief=SUNKEN)

# improtant pack options
# anchor = nw
# side = top, bottom, left, right
# fill
# padx
# pady
# title_label.pack(side=BOTTOM,anchor='sw')
# title_label.pack(side=BOTTOM,fill=X)
# title_label.pack(side=LEFT,fill=Y)    # you have to attact left or right only for fill = Y
title_label.pack(side=LEFT,fill=Y,padx=50,pady=50)

root.mainloop()