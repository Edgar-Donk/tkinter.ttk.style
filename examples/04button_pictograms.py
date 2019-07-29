"""
Button with pictograms

use the mouse and press the button
creates second command window, could be to to with PhotoImage
"""

from tkinter import PhotoImage,Tk
from tkinter.ttk import Style, Button,Frame, Label

s=Style()
s.theme_use('default')
root = Tk()
# using alternative cross reference 'im1'
image1=PhotoImage('im1',file='../images/close.gif')
image2=PhotoImage(file='../images/close_active.gif')
image3=PhotoImage(file='../images/close_pressed.gif')
fr = Frame()
fr.pack()
lab = Label(fr,text="Dont't forget to click and hover")
lab.pack(padx=4, pady=10)
# using alternative cross reference 'im1'
but = Button(fr,text='test',compound='right',image=('im1',
             'pressed', image2,'active', image3))
but.image=('im1', 'pressed', image2,'active', image3)
but.pack(padx=4, pady=10)

root.mainloop()             
