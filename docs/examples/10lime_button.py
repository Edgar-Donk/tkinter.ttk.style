'''
Button

All slider apart from button-sa
required padding 4 to compress the buttons
'''

from tkinter import Tk, PhotoImage
from tkinter.ttk import Style, Frame, Button
from RunState import run_state

root = Tk()

fr = Frame(root)
fr.grid(column=0,row=0,sticky='nsew')

img1 = PhotoImage("slider-hn", file='../images/lime/slider-hn.png')
img2 = PhotoImage("slider-hd", file='../images/lime/slider-hd.png')
img3 = PhotoImage("slider-hp", file='../images/lime/slider-hp.png')
img4 = PhotoImage("button-sa", file='../images/lime/button-sa.png')
img5 = PhotoImage("slider-ha", file='../images/lime/slider-ha.png')


style = Style()
# both theme_create and theme_settings worked
#style.theme_create( "yummy", parent="clam", settings={
style.theme_settings('default', {
# start of theme extract
     'TButton': {
         'configure': { "anchor": "center",'padding': [10,0], 'foreground': '#8b0a50'}, # "width": 10,,
         'layout': [
         ('Button.focus', {'children':
            [('Button.button', {'children':
                [('Button.padding', {'children':
                    [('Button.label', {"side": "left",'expand': 1})]
                })]
            })]
        })]},

     'Button.button': {"element create":
          ('image', "slider-hn",
           ('pressed', "slider-hp"),
           ('active', "slider-ha"),
           ('selected', "button-sa"),
           ('disabled', "slider-hd"),           
           {'border':[5,12,5,12], 'padding': 4,  'sticky': "nsew"}) # "nsew"
         }
      
# end of theme extract - don't forget to add comma at end when inserting
     })

style.theme_use ('default') #('yummy') #
widg = Button(fr,text='Piratz!')
widg.grid(column=0,row=11, padx=5, pady=5) #sticky='nsew',
widg1 = Button(fr,text='Piratz!\nextra line made longer')
# sticky='nsew', makes no difference
widg1.grid(column=0,row=12, padx=5, pady=5) # sticky='nsew',
run_state(fr,widg,widg1)

root.mainloop()
