# colouring the ttk buttons
from tkinter.ttk import Style
from tkinter import Tk
from tkinter import Button as origbutton
from tkinter.ttk import Button as tilebutton

root=Tk()
s = Style()
s.theme_use('default')
s.configure('green.TButton', foreground='green')
s.configure('red.green.TButton', background='red')
origbutton(root,text='original').pack()
tilebutton(root,text='ttk themed',style='green.TButton').pack()
tilebutton(root,text='2nd ttk',style='red.green.TButton').pack()

root.mainloop()
