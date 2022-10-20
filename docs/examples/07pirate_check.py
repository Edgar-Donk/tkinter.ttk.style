'''
Check buttons

Create theme extract for custom widgets, include state selection to view
the result of changing the state using different images and/or different
settings.

'''

from tkinter import Tk, PhotoImage
from tkinter.ttk import Style, Frame, Checkbutton
from RunState import run_state

root = Tk()

fr = Frame(root)
fr.grid(column=0,row=0,sticky='nsew')

img1 = PhotoImage("check-nc", file='../images/piratz/check-nc.png')
img2 = PhotoImage("check-dc", file='../images/piratz/check-dc.png')
img3 = PhotoImage("check-du", file='../images/piratz/check-du.png')
img4 = PhotoImage("check-nu", file='../images/piratz/check-nu.png')

style = Style()
# both theme_create and theme_settings worked
style.theme_create( "yummy", parent="clam", settings={
# style.theme_settings('default', {
# start of theme extract
     'Checkbutton.indicator': {"element create":
          ('image', "check-nu",
           ('pressed', 'selected', "check-nc"),
           ('pressed', "check-nu"),
           ('active', 'selected', "check-nc"),
           ('active', "check-nu"),
           ('disabled', 'selected', "check-dc"),
           ('selected', "check-nc"),
           ('disabled', "check-du"),
           {'width':24, 'sticky': "w"})
         }
# end of theme extract - don't forget to add comma at end when inserting
     })

style.theme_use('yummy') # 'default'

widg = Checkbutton(fr, text='Cheese')
widg1 = Checkbutton(fr, text='Tomato')
widg.grid(column=0,row=18,sticky='nsew', padx=5, pady=5)
widg1.grid(column=0,row=19,sticky='nsew', padx=5, pady=5)
run_state(fr,widg,widg1)
root.mainloop()
