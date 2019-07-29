'''
Check buttons

Create theme extract for custom widgets, include state selection to view
the result of changing the state using different images and/or different
settings.

'''

from tkinter import Tk, PhotoImage, StringVar
from tkinter.ttk import Style, Frame, Checkbutton
from RunState import run_state

root = Tk()

fr = Frame(root)
fr.grid(column=0,row=0,sticky='nsew')

img1 = PhotoImage("check-nc", file='../images/lime/check-nc.png')
img2 = PhotoImage("check-hc", file='../images/lime/check-hc.png')
img3 = PhotoImage("check-hu", file='../images/lime/check-hu.png')
img4 = PhotoImage("check-nu", file='../images/lime/check-nu.png')
img5 = PhotoImage("check-dc", file='../images/lime/check-dc.png')
img6 = PhotoImage("check-du", file='../images/lime/check-du.png')

style = Style()
# both theme_create and theme_settings worked
style.theme_create( "yummy", parent="clam", settings={
#style.theme_settings('default', {
# start of theme extract
     'Checkbutton.indicator': {"element create":
          ('image', "check-nu",
           ('active', 'selected', "check-hc"),
           ('active', "check-hu"),
           ('disabled', 'selected', "check-dc"),
           ('selected', "check-nc"),
           ('disabled', "check-du"),
           { 'sticky': "w", 'padding':3}) # 'width':24,
         }
# end of theme extract - don't forget to add comma at end when inserting
     })

style.theme_use('yummy') # 'default'

widg = Checkbutton(fr, text='Cheese' ,width=-8)
widg1 = Checkbutton(fr, text='Tomato' ,width=-8)
widg.grid(column=0,row=11,sticky='nsew', padx=5, pady=5)
widg1.grid(column=0,row=12,sticky='nsew', padx=5, pady=5)
run_state(fr,widg,widg1)

root.mainloop()
