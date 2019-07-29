'''
Radio Buttons

Create theme extract for custom widgets, include state selection to view
the result of changing the state using different images and/or different
settings.

'''

from tkinter import Tk, PhotoImage, StringVar
from tkinter.ttk import Style, Radiobutton, Frame
from RunState import run_state

root = Tk()

fr = Frame(root)
fr.grid(column=0,row=0,sticky='nsew')

img1 = PhotoImage("radio-n", file='../images/lime/radio-n.png')
img2 = PhotoImage("radio-s", file='../images/lime/radio-s.png')
img3 = PhotoImage("radio-d", file='../images/lime/radio-d.png')
img4 = PhotoImage("radio-ds", file='../images/lime/radio-ds.png')

style = Style()
# both theme_create and theme_settings worked
style.theme_create( "yummy", parent="clam", settings={
#style.theme_settings('default', {
# start of theme extract
     'Radiobutton.indicator': {"element create":
          ('image', "radio-n",
           ('disabled','selected', "radio-ds"),
         ('disabled', "radio-d"),
           ('selected', "radio-s"),
           {'width':20, 'sticky': "w"}) 
        }
# end of theme extract - don't forget to add comma at end when inserting
     })


style.theme_use('yummy') # 'default'
happy = ['Great', 'Good', 'OK', 'Poor', 'Awful']
happiness = StringVar()
for ix,s in enumerate(happy):
    widg = Radiobutton(fr, text=s, value=s,
            variable=happiness)
    widg.grid(column=0,row=11+ix,sticky='nw')
    
run_state(fr,widg)

root.mainloop()
