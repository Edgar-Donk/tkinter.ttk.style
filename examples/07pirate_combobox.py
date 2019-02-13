'''
Create theme extract for custom widgets, include state selection to view
the result of changing the state using different images and/or different
settings.
Combobox states disabled, readonly;focus, readonly; normal, focus, pressed, disabled;
normal,readonly,active; normal,pressed,active, disabled
'''

from tkinter import Tk, PhotoImage, StringVar
from tkinter.ttk import Style, Label, Radiobutton, Frame, Combobox

root = Tk()

def change_state():
    oldstate = widg.state()
    if len(oldstate) > 0:
        # convert tuple to string 
        oldst = " ".join(str(x) for x in oldstate) 
        widg.state(['!'+oldst])
        widg1.state(['!'+oldst])
    newstate = state_val.get()
    widg.state([newstate])
    widg1.state([newstate])



fr = Frame(root)
fr.grid(column=0,row=0,sticky='nsew')

states = ['active', 'alternate', 'background', 'disabled',
                      'focus', 'invalid', 'pressed', 'readonly', 'selected']
# Create rasio buttons which will display widget states

state_val = StringVar()
for iy, state in enumerate(states):
    st_rb = Radiobutton(fr, value=state, text=state,
            variable=state_val, command=change_state)
    st_rb.grid(column=0,row=iy,padx=5,pady=5, sticky='nw')

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
style.theme_settings('default', {
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

style.theme_use('default') # 'yummy'
sv = StringVar()
widg = Combobox(fr,values=['apple', 'banana', 'orange'])
widg.grid(column=0,row=10,padx=5,pady=5 )
sv.set('first')
sv1 = StringVar()
widg1 = Combobox(fr,values=['apple', 'banana', 'orange'])
widg1.grid(column=0,row=11,padx=5,pady=5,sticky='ns')
sv1.set('second really really long')

root.mainloop()
