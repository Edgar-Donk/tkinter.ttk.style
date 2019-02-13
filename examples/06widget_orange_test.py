'''
Using theme_create to test the script for the orange standalone theme.
When using theme_settings it gave an error message - not yet resolved.
'''

from tkinter.ttk import Style, Combobox
from tkinter import Tk, PhotoImage

root = Tk()
style = Style()
im0 = PhotoImage('combor-n', file='images/combor-n.gif')
im1 = PhotoImage('combor-rd',file='images/combor-rd.gif')
im2 = PhotoImage('combor-rp',file='images/combor-rp.gif')
im3 = PhotoImage('combor-rf',file='images/combor-rf.gif')
im4 = PhotoImage('combor-rn',file='images/combor-rn.gif')
im5 = PhotoImage('comboarrow-n',file='images/comboarrow-n.gif')
im6 = PhotoImage('comboarrow-p',file='images/comboarrow-p.gif')
im7 = PhotoImage('comboarrow-a',file='images/comboarrow-a.gif')
im8 = PhotoImage('comboarrow-d',file='images/comboarrow-d.gif')

# Try theme_settings, comment out theme_create uncomment theme_settings
# also change theme_use 
style.theme_create('test', parent="clam", settings={
#style.theme_settings("clam", {    
   "TCombobox": {
       "configure": {"selectbackground": "#657a9e"}}, # 'light blue'
       "Combobox.field": {"element create":
           ("image", 'combor-n',
                ('readonly', 'disabled', 'combor-rd'),
                ('readonly', 'pressed', 'combor-rp'),
                ('readonly', 'focus', 'combor-rf'),
                ('readonly',  'combor-rn'),
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
})

style.theme_use('test') # change to style.theme_use('clam') if using theme_settings
combo = Combobox(values=['apple', 'banana', 'orange']).pack()
root.mainloop()
