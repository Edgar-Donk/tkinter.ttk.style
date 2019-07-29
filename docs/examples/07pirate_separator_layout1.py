'''
Vertical Separator using layout

element name common
'''

from tkinter import Tk, PhotoImage, StringVar
from tkinter.ttk import Style, Label, Radiobutton, Frame, Separator 

root = Tk()

fr = Frame(root)
fr.grid(column=0,row=0,sticky='nsew')

img1 = PhotoImage("separator", file='../images/piratz/separator.png')
img2 = PhotoImage("separator-v", file='../images/piratz/separator-v.png')

style = Style()
# both theme_create and theme_settings worked
style.theme_create( "yummy", parent="clam", settings={
#style.theme_settings('default', {
# start of theme extract
    'Horizontal.TSeparator': {'layout': [
        ('Horizontal.Separator.separator',{"sticky": "ew"},
        )]},
    
    'Vertical.TSeparator': {'layout': [
        ('Vertical.Separator.separator',{"sticky": "ns"},
        )]},

    'Horizontal.Separator.separator': {"element create":
        ('image', "separator",
         {'border':[3],'sticky': 'ew'})},

    'Vertical.Separator.separator': {"element create":
        ('image', "separator-v",
         {'border':[3],'sticky': 'ns'})}
    
# end of theme extract - don't forget to add comma at end when inserting
     })

fr1 = Frame(fr, height=250, width=250)
fr1.grid(column=1,row=0,sticky='nsew', padx=5, pady=5)                    
style.theme_use('yummy') # 'default'
widg = Separator(fr1,orient="horizontal")
widg.place(x=5, y=5, width=150)

widg1 = Separator(fr1,orient="vertical")
widg1.place(x=75, y=50, height=150, width=8) #, width=5


root.mainloop()
