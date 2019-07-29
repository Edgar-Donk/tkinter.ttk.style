'''
Using pprint we have an easier method to show the layout in a reasonable manner.

Configure has probably more colours than will be displayed, it will help show
which elements can be coloured, where they are situated. In this exercise use
colours that can be easily picked out rather than for final looks.
'''
from pprint import pformat
from tkinter import Tk, Message
from tkinter.ttk import Style, Combobox, Button, Checkbutton

def theme_changed(theme):
    style.theme_use(theme)

    lay = style.layout(tWidg)
    
    ppout = pformat(lay)

    style.configure(
        'Custom.' + tWidg,
        background='#FFFFFF', # White
        bordercolor='#00FF00', # Green
        lightcolor='#FF0000', # Red
        darkcolor='#0000FF', # Blue
        borderwidth=4,
        foreground='#00FFFF', # Cyan
        fieldbackground='#FF00FF', # Magenta
        troughcolor='#FFFF00', # Yellow
        arrowcolor='#A52A2A', # brown
        focuscolor='#40E0D0' # turquoise
    )
    return ppout 

root = Tk()
style = Style()
tWidg = 'TCheckbutton'
combo = Combobox(root, values=sorted(style.theme_names()), state='readonly')
combo.set(style.theme_use())
combo.bind('<<ComboboxSelected>>', lambda _e: theme_changed(combo.get()))
combo.pack()

out = theme_changed(style.theme_use())

button = Checkbutton(root, text="Normal Button")
button.pack()

button = Checkbutton(root, style="Custom." + tWidg, text="Custom Button")
button.pack()

mess = Message(root, text='layout \n\n'+out, width=250)
mess.pack()

root.mainloop()


