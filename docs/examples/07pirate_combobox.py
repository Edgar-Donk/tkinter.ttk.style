'''
Combobox with an anchor

Create theme extract for custom widgets, include state selection to view
the result of changing the state using different images and/or different
settings.
Combobox states disabled, readonly;focus, readonly; normal, focus, pressed,
disabled; normal,readonly,active; normal,pressed,active, disabled
'''

from tkinter import Tk, PhotoImage, StringVar
from tkinter.ttk import Style, Frame, Combobox
from RunState import run_state

root = Tk()

fr = Frame(root)
fr.grid(column=0,row=0,sticky='nsew')

img1 = PhotoImage("combo-n", file='../images/piratz/combo-n.png')
img2 = PhotoImage("combo-ra", file='../images/piratz/combo-ra.png')
img3 = PhotoImage("combo-rd", file='../images/piratz/combo-rd.png')
img4 = PhotoImage("combo-rf", file='../images/piratz/combo-rf.png')
img5 = PhotoImage("combo-rn", file='../images/piratz/combo-rn.png')
img6 = PhotoImage("combo-rp", file='../images/piratz/combo-rp.png')
img7 = PhotoImage("comboarrow-a", file='../images/piratz/comboarrow-a.png')
img8 = PhotoImage("comboarrow-d", file='../images/piratz/comboarrow-d.png')
img9 = PhotoImage("comboarrow-n", file='../images/piratz/comboarrow-n.png')
img10 = PhotoImage("comboarrow-p", file='../images/piratz/comboarrow-p.png')


style = Style()
# both theme_create and theme_settings worked
#style.theme_create( "yummy", parent="clam", settings={
style.theme_settings('alt', {
# start of theme extract
     "Combobox.field": {"element create":
           ("image", 'combo-n',
                ('readonly', 'disabled', 'combo-rd'),
                ('readonly', 'pressed', 'combo-rp'),
                ('readonly', 'focus', 'combo-rf'),
                ('readonly',  'combo-rn'),
                {'sticky': 'ew',  'border': [4]}
           )
        },
        "Combobox.downarrow": {"element create":
            ("image", 'comboarrow-n',
                 ('disabled','comboarrow-d'),
                 ('pressed','comboarrow-p'),
                 ('active','comboarrow-a'),
                 {'sticky': '','border': [1]}
             )
        }

# end of theme extract - don't forget to add comma at end when inserting
     })

style.theme_use('alt') # 'yummy'
sv = StringVar()
widg = Combobox(fr,values=['apple', 'banana', 'orange'], textvariable=sv)
widg.grid(column=0,row=18,padx=5,pady=5 )
sv.set('first')
sv1 = StringVar()
widg1 = Combobox(fr,values=['apple', 'banana', 'orange'], textvariable=sv1)
widg1.grid(column=0,row=19,padx=5,pady=5,sticky='ns')
sv1.set('second really really long')
run_state(fr,widg,widg1)

root.mainloop()
