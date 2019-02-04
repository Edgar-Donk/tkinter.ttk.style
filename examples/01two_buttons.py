# comparing the button widgets
from tkinter.ttk import Style
from tkinter import Tk
from tkinter import Button as origbutton
from tkinter.ttk import Button as tilebutton

root=Tk()
s = Style()
s.theme_use('default') # using the ttk default scheme so that all os will be similar 
origbutton(root,text='original').pack()
tilebutton(root,text='ttk themed').pack()
tilebutton(root,text='2nd ttk').pack()

root.mainloop()
