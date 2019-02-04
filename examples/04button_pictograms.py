from tkinter import PhotoImage,Tk
from tkinter.ttk import Style, Button,Frame


s=Style()
s.theme_use('default')
root = Tk()
image1=PhotoImage(file='../images/close.gif')
image2=PhotoImage(file='../images/close_active.gif')
image3=PhotoImage(file='../images/close_pressed.gif')
fr = Frame()
fr.pack()
but = Button(fr,text='test',compound='right',image=(image1 ,
             'pressed', image2,'active', image3))
but.pack()

root.mainloop()             
