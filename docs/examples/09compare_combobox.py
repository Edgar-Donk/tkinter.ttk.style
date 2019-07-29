'''
Create theme extract for custom widgets, need state selection to compare
different themes. Both widgets almost same, but pil (lower one) has slightly
jagged edges around arrow.
'''

from tkinter import Tk, PhotoImage, StringVar
from tkinter.ttk import Style, Label, Radiobutton, Frame, Combobox

root = Tk()

fr = Frame(root)
fr.grid(column=0,row=0,sticky='nsew')

img1 = PhotoImage("combo-n", file='../images/combo-n.png')
img2 = PhotoImage("combo-p", file='../figures/09combo.png')
img9 = PhotoImage("comboarrow-n", file='../images/comboarrow-n.png')
img11 = PhotoImage("comboarrow-p", file='../figures/09comboarrow5.png')


style = Style()
# both theme_create and theme_settings worked
style.theme_create( "yummy", parent="clam", settings={
#style.theme_settings('default', {

     "Combobox.field": {"element create":
           ("image", 'combo-p',
                ('alternate',  'combo-n'),
                {'sticky': 'ew',  'border': [4]}
           )
        },
        "Combobox.downarrow": {"element create":
            ("image", 'comboarrow-p',
                 ('alternate','comboarrow-n'),
                 {'sticky': '','border': [1]}
             )
        }
     
     })

style.theme_use('yummy') # 'clam' 'yummy'
sv = StringVar()
widg = Combobox(fr,values=['ubuntu', 'banana', 'orange'])
widg.grid(column=0,row=10,padx=5,pady=5 )
sv.set('ubuntu')
sv1 = StringVar()
widg1 = Combobox(fr,values=['created with pil', 'banana', 'orange'])
widg1.grid(column=0,row=11,padx=5,pady=5,sticky='ns')
sv1.set('created with pil')
widg.state(['alternate'])

root.mainloop()
