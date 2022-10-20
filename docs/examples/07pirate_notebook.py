'''
Notebook

Create theme extract for custom widgets, include state selection to view
the result of changing the state using different images and/or different
settings.
Selection of border and padding a little tricky.
Try with and without the mapping
'''

from tkinter import Tk, PhotoImage, font
from tkinter.ttk import Style, Frame, Notebook
from RunState import run_state

root = Tk()

colours = {'bordercolor': '#7FFFD4'}

fr = Frame(root)
fr.grid(column=0,row=0,sticky='nsew')

img1 = PhotoImage("sail", file='../images/piratz/sail.png')
img2 = PhotoImage("sail-d", file='../images/piratz/sail-d.png')
img3 = PhotoImage("sail-p", file='../images/piratz/sail-p.png')
img4 = PhotoImage("sail-s", file='../images/piratz/sail-s.png')

style = Style()
# both theme_create and theme_settings worked
style.theme_create( "yummy", parent="clam", settings={
#style.theme_settings('default', {
# start of theme extract
    'TNotebook.tab': {"map":
        {'expand': [('selected', [6,6,6,6])]}}, # 2,7,5,5

     'tab': {"element create":
          ('image', "sail",
           ('pressed', "sail-p"),
           ('selected', "sail-s"),
           ('disabled', "sail-d"),
           {'border':[30, 17, 27, 32], 'padding':[13,8,12,13], 'sticky': "nsew"} #
        ) },
       'TNotebook': {'configure': {'bordercolor': colours['bordercolor'],
                                   'tabmargins':[6,6,6,6]}}

# end of theme extract - don't forget to add comma at end when inserting
     })

style.theme_use('yummy') # 'default'
test_size = font.Font(family="Times", size=12, weight="bold").measure('Test')
mult = int(test_size / 30)
widg = Notebook(fr)
page1 = Frame(widg, width=150*mult, height=150*mult)
page2 = Frame(widg, width=150*mult, height=150*mult)
widg.add(page1,text='Piratz!')
widg.add(page2,text='Piratz!\nextra longish line\nor two')
widg.grid(column=0,row=18,sticky='nsew', padx=5, pady=15)
run_state(fr,widg)

root.mainloop()
