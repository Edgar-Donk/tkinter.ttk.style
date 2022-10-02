'''
Combobox

Create theme extract for custom widgets, include state selection to view
the result of changing the state using different images and/or different
settings.
Combobox states disabled, readonly;focus, readonly; normal, focus, pressed,
disabled; normal,readonly,active; normal,pressed,active, disabled
'''

from tkinter import Tk, PhotoImage
from tkinter.ttk import Style, Frame, Combobox
from RunState import run_state

root = Tk()

fr = Frame(root)
fr.grid(column=0,row=0,sticky='nsew')

img1 = PhotoImage("combo-n", file='../images/lime/combo-n.png')
img3 = PhotoImage("combo-d", file='../images/lime/combo-d.png')
img7 = PhotoImage("arrowdown-a", file='../images/lime/arrowdown-a.png')
img8 = PhotoImage("arrowdown-d", file='../images/lime/arrowdown-d.png')
img9 = PhotoImage("arrowdown-n", file='../images/lime/arrowdown-n.png')
img10 = PhotoImage("arrowdown-p", file='../images/lime/arrowdown-p.png')


style = Style()
# both theme_create and theme_settings worked
style.theme_create( "yummy", parent="clam", settings={
#style.theme_settings('alt', {
# start of theme extract
     "Combobox.field": {"element create":
           ("image", 'combo-n',
                ('readonly', 'disabled', 'combo-d'),
                #('readonly', 'pressed', 'combo-rp'),
                #('readonly', 'focus', 'combo-rf'),
                #('readonly',  'combo-rn'),
                {'sticky': 'ew',  'border': [4],'padding': 1}
           )
        },
        "Combobox.downarrow": {"element create":
            ("image", 'arrowdown-n',
                 ('disabled','arrowdown-d'),
                 ('pressed','arrowdown-p'),
                 ('active','arrowdown-a'),
                 {'sticky': '','border': [1],'padding': 4}
             )
        }

# end of theme extract - don't forget to add comma at end when inserting
     })

style.theme_use('yummy') # 'alt'
widg = Combobox(fr,values=['apple', 'banana', 'orange'])
widg.grid(column=0,row=13,padx=5,pady=5 )
widg1 = Combobox(fr,values=['apple', 'banana', 'orange'])
widg1.grid(column=0,row=14,padx=5,pady=5,sticky='ns')
run_state(fr,widg,widg1)

root.mainloop()
