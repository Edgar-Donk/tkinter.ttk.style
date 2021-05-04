'''
Button

Create theme extract for custom widgets, include state selection to view
the result of changing the state using different images and/or different
settings.
Selection of border and padding a little tricky.
Using layout putting focus first so the dashed line encircles widget.
In python it is best to run configure and layout together, in tcl they are
separated.
'''

from tkinter import Tk, PhotoImage
from tkinter.ttk import Style, Frame, Button
import tkinter.font as tkFont
from RunState import run_state

root = Tk()

pirate_font = tkFont.Font(family="Palace Script MT", size=14) 
fr = Frame(root)
fr.grid(column=0,row=0,sticky='nsew')


img1 = PhotoImage("button", file='../images/piratz/button.png')
img2 = PhotoImage("button-d", file='../images/piratz/button-d.png')
img3 = PhotoImage("button-p", file='../images/piratz/button-p.png')
img4 = PhotoImage("button-s", file='../images/piratz/button-s.png')

style = Style()
# both theme_create and theme_settings worked
#style.theme_create( "yummy", parent="clam", settings={
style.theme_settings('default', {
# start of theme extract
     'TButton': {
         'configure': {'anchor': 'center', 'font':pirate_font},
         'layout': [
         ('Button.focus', {'children':
            [('Button.button', {'children':
                [('Button.padding', {'children':
                    [('Button.label', {'expand': 0})]
                })]
            })]
        })]},

     'Button.button': {"element create":
          ('image', "button",
           ('pressed', "button-p"),
           ('selected', "button-s"),
           ('active', "button-s"),
           ('disabled', "button-d"),
           {'border':[52,65,47,17], 'padding':[12,54,8,16], 'sticky': "nsew"}) 
         }
      
# end of theme extract - don't forget to add comma at end when inserting
     })

style.theme_use ('default') #('yummy') #

widg = Button(fr,text='Piratz!')
widg.grid(column=0,row=11, padx=5, pady=5) #sticky='nsew',
widg1 = Button(fr,text='Piratz!\nextra line made longer')
widg1.grid(column=0,row=12, padx=5, pady=5) # sticky='nsew',
run_state(fr,widg,widg1)

root.mainloop()
