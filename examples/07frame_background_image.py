'''
replace the image with your own image, if the screen size
is large enough, about 1000 wide by 350 high.
'''

from tkinter import Tk, PhotoImage
from tkinter.ttk import Frame, Style, Label, Entry
from PIL import Image, ImageTk

root = Tk()
s = Style()

im = Image.open('images/BountyMoorea.jpg') # change to your own file
tkim = ImageTk.PhotoImage(im)
width,height = im.size

s.element_create("ship", "image", tkim)
s.layout("ship", [("ship", {"sticky": "nsew"})])

fr=Frame(root, style="ship", height=height,width=width) 
fr.grid(column=0, row=1, sticky='nsew')

il = Label(fr, text= 'Label')
il.place(relx=0.1, rely=0.1, anchor='center') # using place to position widget

en = Entry(fr, width=15)
en.place(relx=0.1, rely=0.15, anchor='center')

root.mainloop()
