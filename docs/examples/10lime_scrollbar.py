'''
Original Scrollbar script.

Create theme extract for custom widgets, include state selection to view
the result of changing the state using different images and/or different
settings.
Setting the thumb ensure that the layout has expand 1 i.e.True, otherwise it
will not move in the trough. In turn the border must be large enough to ensure
that the image expands and does not create multiple images.
Grip is not included.
'''

from tkinter import Tk, PhotoImage, Listbox
from tkinter.ttk import Style, Frame, Scrollbar
from RunState import run_state
root = Tk()

fr = Frame(root)
fr.grid(column=0,row=0,sticky='nsew')

img3 = PhotoImage("slider-hn", file='../images/lime/slider-hn.png')
img4 = PhotoImage("slider-vn", file='../images/lime/slider-vn.png')
img5 = PhotoImage("slider-hd", file='../images/lime/slider-hd.png')
img6 = PhotoImage("slider-vd", file='../images/lime/slider-vd.png')
img7 = PhotoImage("slider-hp", file='../images/lime/slider-hp.png')
img8 = PhotoImage("slider-vp", file='../images/lime/slider-vp.png')
img9 = PhotoImage("arrowup-a", file='../images/lime/arrowup-a.png')
img10 = PhotoImage("arrowup-d", file='../images/lime/arrowup-d.png')
img11 = PhotoImage("arrowup-n", file='../images/lime/arrowup-n.png')
img12 = PhotoImage("arrowup-p", file='../images/lime/arrowup-p.png')
img13 = PhotoImage("arrowdown-a", file='../images/lime/arrowdown-a.png')
img14= PhotoImage("arrowdown-d", file='../images/lime/arrowdown-d.png')
img15 = PhotoImage("arrowdown-n", file='../images/lime/arrowdown-n.png')
img16 = PhotoImage("arrowdown-p", file='../images/lime/arrowdown-p.png')
img17 = PhotoImage("arrowleft-a", file='../images/lime/arrowleft-a.png')
img18= PhotoImage("arrowleft-d", file='../images/lime/arrowleft-d.png')
img19 = PhotoImage("arrowleft-n", file='../images/lime/arrowleft-n.png')
img20 = PhotoImage("arrowleft-p", file='../images/lime/arrowleft-p.png')
img21 = PhotoImage("arrowright-a", file='../images/lime/arrowright-a.png')
img22= PhotoImage("arrowright-d", file='../images/lime/arrowright-d.png')
img23 = PhotoImage("arrowright-n", file='../images/lime/arrowright-n.png')
img24 = PhotoImage("arrowright-p", file='../images/lime/arrowright-p.png')
img25 = PhotoImage("slider-ha", file='../images/lime/slider-ha.png')
img26 = PhotoImage("slider-va", file='../images/lime/slider-va.png')

style = Style()
# both theme_create and theme_settings worked
style.theme_create( "yummy", parent="clam", settings={
#style.theme_settings('default', {
# start of theme extract
        "Horizontal.TScrollbar": {"layout": [
            ("Horizontal.Scrollbar.trough", { "children": # "sticky": "ew",
                 [("Horizontal.Scrollbar.leftarrow", {"side": "left"}),
                 ("Horizontal.Scrollbar.rightarrow", {"side": "right"}),
                 ("Horizontal.Scrollbar.thumb", {"side": "left","expand": 1,"sticky": "ew"})]
            })]},

     "Horizontal.Scrollbar.thumb": {"element create":
            ("image", 'slider-hn',
             ('disabled', 'slider-hd'),
             ('pressed', 'slider-hp'),
             ('active', 'slider-ha'),
             {"border": 3}) #[9,2] , 'sticky': 'ew', 'padding': [7,2]
        },

     'Scrollbar.leftarrow': {"element create":
            ("image", 'arrowleft-n',
             ('disabled', 'arrowleft-d'),
             ('pressed', 'arrowleft-p'),
             ('active', 'arrowleft-a'),
             {"border": 1})
            },

     'Scrollbar.rightarrow': {"element create":
            ("image", 'arrowright-n',
             ('disabled', 'arrowright-d'),
             ('pressed', 'arrowright-p'),
             ('active', 'arrowright-a'),
             {"border": 1})
            },

     "Vertical.TScrollbar": {"layout": [
            ("Vertical.Scrollbar.trough", {"sticky": "ns", "children":
                 [("Vertical.Scrollbar.uparrow", {"side": "top"}),
                 ("Vertical.Scrollbar.downarrow", {"side": "bottom"}),
                 ("Vertical.Scrollbar.thumb", {"side": "top","expand": 1,"sticky": "ns"})]
            })]},

     "Vertical.Scrollbar.thumb": {"element create":
            ("image", 'slider-vn',
             ('disabled', 'slider-vd'),
             ('pressed', 'slider-vp'),
             ('active', 'slider-va'),
             {"border": [2,9]})
        },

     'Scrollbar.uparrow': {"element create":
            ("image", 'arrowup-n',
             ('disabled', 'arrowup-d'),
             ('pressed', 'arrowup-p'),
             ('active', 'arrowup-a'),
             {"border": 1})
            },

     'Scrollbar.downarrow': {"element create":
            ("image", 'arrowdown-n',
             ('disabled', 'arrowdown-d'),
             ('pressed', 'arrowdown-p'),
             ('active', 'arrowdown-a'),
             {"border": 1})
            },

    'TCombobox': {
        'configure': {'selectborderwidth': 1, 'padding': 2,
                      'insertwidth': 2, 'font': 'TkTextFont'}}

# end of theme extract - don't forget to add comma at end when inserting
     })

style.theme_use('yummy') # 'default'

fr1 = Frame(fr,height=250,width=250)
fr1.grid(column=0,row=14,sticky='nsew')

widg = Scrollbar(fr1, orient="vertical")
widg1 = Scrollbar(fr1, orient="horizontal")
mylist = Listbox(fr1)
for line in range(100):
    mylist.insert('end', "A really long line. "+ str(line)+" Line number " )

mylist.grid( column=0,row=0)

widg.grid(column=1,row=0,sticky='ns')
widg.configure( command = mylist.yview )

widg1.grid(column=0,row=1,sticky='ew')
widg1.configure( command = mylist.xview )
mylist.configure(yscrollcommand = widg.set, xscrollcommand = widg1.set) #

run_state(fr,widg,widg1)
root.mainloop()

