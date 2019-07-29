''' colouring the ttk buttons '''
from tkinter.ttk import Style, Label
from tkinter import Tk
from tkinter import Button as origb
from tkinter.ttk import Button as tileb

root=Tk()
s = Style()
s.theme_use('default')
l = Label(root,text='Run the mouse over the buttons below \n also left click \
on each one').pack(padx=5, pady=5)
s.configure('green.TButton', foreground='green')
s.configure('red.green.TButton', background='red')
origb(root,text='original tkinter').pack(padx=5, pady=5)
tileb(root,text='ttk themed',style='green.TButton').pack(padx=5, pady=5)
tileb(root,text='2nd ttk',style='red.green.TButton').pack(padx=5, pady=5)

root.mainloop()
