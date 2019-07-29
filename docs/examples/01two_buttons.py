""" Comparing the Button widgets 

Compare different methods of running python.
"""
from tkinter.ttk import Style, Label
from tkinter import Tk
from tkinter import Button as origbutton
from tkinter.ttk import Button as tilebutton

root=Tk()
s = Style()
# using the ttk default scheme 
s.theme_use('default') 
Label(root,text='Move your mouse over each of the buttons below,\n \
      then left click on each of them').pack()
origbutton(root,text='original').pack()
origbutton(root,text='2nd original').pack()
tilebutton(root,text='ttk themed').pack()
tilebutton(root,text='2nd themed').pack()

root.mainloop()
