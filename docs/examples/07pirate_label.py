'''
Used as template for other widgets in the theme

Create theme extract for custom widgets, include state selection to view
the result of changing the state using different images and/or different
settings.
Selection of border and padding a little tricky try the border with
[20, 6, 4, 4] with/without padding, padding positions the text
also experiment with sticky as "ew".
'''

from tkinter import Tk, PhotoImage
from tkinter.ttk import Style, Label, Frame
from RunState import run_state

root = Tk()
img1 = PhotoImage("label", file='../images/piratz/label.png')
img2 = PhotoImage("label-d", file='../images/piratz/label-d.png')

style = Style()
# both theme_create and theme_settings worked
style.theme_create( "yummy", parent="clam", settings={
#style.theme_settings('default', {
# start of theme extract
     'Label.border': {"element create":
          ('image', "label",
           ('disabled', "label-d"),
           {'border':[17, 9, 3, 7], 'padding':[17,5,3,3], 'sticky': "nsew"})

        }
# end of theme extract - don't forget to add comma at end when inserting
     })

style.theme_use('yummy') # 'default'

fr = Frame(root)
fr.grid(column=0,row=0,sticky='nsew')
widg = Label(fr,text='Piratz! make it long')
widg.grid(column=0,row=13,sticky='nsew', padx=5, pady=5)
widg1 = Label(fr,text='Piratz!\nextra line')
widg1.grid(column=0,row=14,sticky='nsew', padx=5, pady=5)
run_state(fr,widg,widg1)

root.mainloop()
