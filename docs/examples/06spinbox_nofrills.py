'''
Spinbox - based on Combobox

Create theme extract for custom widgets, include state selection to view
the result of changing the state using different images and/or different
settings.
Spinbox states disabled, readonly;focus, readonly; normal, focus, pressed,
disabled; normal,readonly,active; normal,pressed,active, disabled

Do not use directly when making the lime theme.
'''

from tkinter import Tk, PhotoImage
from tkinter.ttk import Style, Frame, Spinbox
from RunState import run_state

root = Tk()

fr = Frame(root)
fr.grid(column=0,row=0,sticky='nsew')

img1 = PhotoImage("combo-n", file='../images/lime/combo-n.png')
img3 = PhotoImage("combo-d", file='../images/lime/combo-d.png')
img7 = PhotoImage("arrowdown-a", file='../images/lime/arrspd-h.png')
img8 = PhotoImage("arrowdown-d", file='../images/lime/arrspd-d.png')
img9 = PhotoImage("arrowdown-n", file='../images/lime/arrspd-n.png')
img10 = PhotoImage("arrowdown-p", file='../images/lime/arrspd-p.png')
img11 = PhotoImage("arrowup-a", file='../images/lime/arrspu-h.png')
img12 = PhotoImage("arrowup-d", file='../images/lime/arrspu-d.png')
img13 = PhotoImage("arrowup-n", file='../images/lime/arrspu-n.png')
img14 = PhotoImage("arrowup-p", file='../images/lime/arrspu-p.png')


style = Style()
# both theme_create and theme_settings worked
style.theme_create( "yummy", parent="clam", settings={
#style.theme_settings('alt', {
# start of theme extract
     "Spinbox.field": {"element create":
           ("image", 'combo-n',
                ('readonly', 'disabled', 'combo-d'),
                {'sticky': 'ew',  'border': [4],'padding': 1} # 'padding': 0
           )
        },
        "Spinbox.downarrow": {"element create":
            ("image", 'arrowdown-n',
                 ('disabled','arrowdown-d'),
                 ('pressed','arrowdown-p'),
                 ('active','arrowdown-a'),
                 {'sticky': 'e','border': [0],'padding': 4} # 'border': [1]
             )
        },
     "Spinbox.uparrow": {"element create":
            ("image", 'arrowup-n',
                 ('disabled','arrowup-d'),
                 ('pressed','arrowup-p'),
                 ('active','arrowup-a'),
                 {'sticky': 'e','border': [0],'padding': 4}
             )
        }


# end of theme extract - don't forget to add comma at end when inserting
     })

style.theme_use('yummy') # 'alt'
widg = Spinbox(fr,from_=0, to=100,width=4)
widg.grid(column=0,row=10,padx=5,pady=5 )
widg1 = Spinbox(fr,from_=0, to=100)
widg1.grid(column=0,row=11,padx=5,pady=5,sticky='ns')
run_state(fr,widg,widg1)

root.mainloop()
