'''
Scrollbar with grip

Create theme extract for custom widgets, include state selection to view
the result of changing the state using different images and/or different
settings.
Setting the thumb ensure that the layout has expand 1 i.e.True, otherwise it
will not move in the trough. In turn the border must be large enough to ensure
that the image expands and does not create multiple images.

The trough has been copied from elegance, and we see how it has expanded to
create 2 outside coloured edges.
Other ideas are copied from radiance.
'''

from tkinter import Tk, PhotoImage, Listbox
from tkinter.ttk import Style, Frame, Scrollbar
from RunState import run_state

root = Tk()

fr = Frame(root)
fr.grid(column=0,row=0,sticky='nsew')

img1 = PhotoImage("trough-horiz", file='../images/piratz/trough-horiz.png')
img2 = PhotoImage("trough-vert", file='../images/piratz/trough-vert.png')
img3 = PhotoImage("hthumb-n", file='../images/piratz/hthumb-n.png')
img4 = PhotoImage("vthumb-n", file='../images/piratz/vthumb-n.png')
img5 = PhotoImage("hthumb-d", file='../images/piratz/hthumb-d.png')
img6 = PhotoImage("vthumb-d", file='../images/piratz/vthumb-d.png')
img7 = PhotoImage("hthumb-a", file='../images/piratz/hthumb-a.png')
img8 = PhotoImage("vthumb-a", file='../images/piratz/vthumb-a.png')
img25 = PhotoImage("vgrip", file='../images/piratz/vgrip.png')
img26 = PhotoImage("hgrip", file='../images/piratz/hgrip.png')
img9 = PhotoImage("arrowup-a", file='../images/piratz/arrowup-a.png')
img10 = PhotoImage("arrowup-d", file='../images/piratz/arrowup-d.png')
img11 = PhotoImage("arrowup-n", file='../images/piratz/arrowup-n.png')
img12 = PhotoImage("arrowup-p", file='../images/piratz/arrowup-p.png')
img13 = PhotoImage("arrowdown-a", file='../images/piratz/arrowdown-a.png')
img14= PhotoImage("arrowdown-d", file='../images/piratz/arrowdown-d.png')
img15 = PhotoImage("arrowdown-n", file='../images/piratz/arrowdown-n.png')
img16 = PhotoImage("arrowdown-p", file='../images/piratz/arrowdown-p.png')
img17 = PhotoImage("arrowleft-a", file='../images/piratz/arrowleft-a.png')
img18= PhotoImage("arrowleft-d", file='../images/piratz/arrowleft-d.png')
img19 = PhotoImage("arrowleft-n", file='../images/piratz/arrowleft-n.png')
img20 = PhotoImage("arrowleft-p", file='../images/piratz/arrowleft-p.png')
img21 = PhotoImage("arrowright-a", file='../images/piratz/arrowright-a.png')
img22= PhotoImage("arrowright-d", file='../images/piratz/arrowright-d.png')
img23 = PhotoImage("arrowright-n", file='../images/piratz/arrowright-n.png')
img24 = PhotoImage("arrowright-p", file='../images/piratz/arrowright-p.png')

style = Style()
# both theme_create and theme_settings worked
style.theme_create( "yummy", parent="clam", settings={
#style.theme_settings('default', {
# start of theme extract
        "Horizontal.TScrollbar": {"layout": [
            ("Horizontal.Scrollbar.leftarrow", {"side": "left", "sticky": ''}),
            ("Horizontal.Scrollbar.rightarrow",
                {"side": "right", "sticky": ''}),
            #("Horizontal.Scrollbar.leftarrow",
                #{"side": "right", "sticky": ''}),
            ("Horizontal.Scrollbar.trough", {"sticky": "ew", "children":
                [("Horizontal.Scrollbar.thumb", {"expand": 1, "unit": 1,
                    "children": [("Horizontal.Scrollbar.grip", {"sticky": ''})]
                })]
            })]},

        "Horizontal.Scrollbar.thumb": {"element create":
            ("image", 'hthumb-n',
             ('disabled', 'hthumb-d'),
             ('pressed', 'hthumb-a'),
             ('active', 'hthumb-a'),
             {"border": [9,2]}) #3 , 'sticky': 'ew', 'padding': [7,2]
        },

        "Horizontal.Scrollbar.grip": {"element create": ("image", 'hgrip')},

        "Horizontal.Scrollbar.trough": {"element create":
            ('image', 'trough-horiz',
             {"border": 2, 'width': 32, 'height':21})},

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
            ("Vertical.Scrollbar.uparrow", {"side": "top", "sticky": ''}),
            ("Vertical.Scrollbar.downarrow", {"side": "bottom", "sticky": ''}),
            #("Vertical.Scrollbar.uparrow", {"side": "bottom", "sticky": ''}),
            ("Vertical.Scrollbar.trough", {"sticky": "ns", "children":
                [("Vertical.Scrollbar.thumb", {"expand": 1, "unit": 1,
                    "children": [("Vertical.Scrollbar.grip", {"sticky": ''})]
                })]
            })]}, # "side": "top",

        "Vertical.Scrollbar.thumb": {"element create":
            ("image", 'vthumb-n',
             ('disabled', 'vthumb-d'),
             ('pressed', 'vthumb-a'),
             ('active', 'vthumb-a'),
             {"border": [2,9]})
        },

        "Vertical.Scrollbar.grip": {"element create": ("image", 'vgrip')},

        "Vertical.Scrollbar.trough": {"element create":
            ('image', 'trough-vert',
             {"border": 2, 'width': 21, 'height':32})},

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
            }

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
mylist.configure(yscrollcommand = widg.set, xscrollcommand = widg1.set)
run_state(fr,widg,widg1)

root.mainloop()

