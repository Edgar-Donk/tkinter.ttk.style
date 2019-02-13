'''
Create theme extract for custom widgets, include state selection to view
the result of changing the state using different images and/or different
settings.
Setting the thumb ensure that the layout has expand 1 i.e.True, otherwise it
will not move in the trough. In turn the border must be large enough to ensure
that the image expands and does not create multiple images.
Grip is not included.
The trough has been copied from elegance, and we see how it has expanded to
create 2 outside coloured edges.
Other ideas are copied from radiance.
'''

from tkinter import Tk, PhotoImage, StringVar, Listbox
from tkinter.ttk import Style, Label, Radiobutton, Frame, Scrollbar

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

direct = ('up', 'down', 'left', 'right')

img1 = PhotoImage("trough-horiz", file='../images/piratz/trough-horiz.png')
img2 = PhotoImage("trough-vert", file='../images/piratz/trough-vert.png')
img3 = PhotoImage("slider-hn", file='../images/piratz/slider-hn.png')
img4 = PhotoImage("slider-vn", file='../images/piratz/slider-vn.png')
img5 = PhotoImage("slider-hd", file='../images/piratz/slider-hd.png')
img6 = PhotoImage("slider-vd", file='../images/piratz/slider-vd.png')
img7 = PhotoImage("slider-ha", file='../images/piratz/slider-ha.png')
img8 = PhotoImage("slider-va", file='../images/piratz/slider-va.png')
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
            ("Horizontal.Scrollbar.trough", {"sticky": "ew", "children":
                 [("Horizontal.Scrollbar.leftarrow", {"side": "left"}),
                 ("Horizontal.Scrollbar.rightarrow", {"side": "right"}),
                 ("Horizontal.Scrollbar.thumb", {"side": "left","expand": 1,"sticky": "ew"})]
            })]},
        
     "Horizontal.Scrollbar.thumb": {"element create":
            ("image", 'slider-hn',
             ('disabled', 'slider-hd'),
             ('pressed', 'slider-ha'),
             ('active', 'slider-ha'),
             {"border": [9,2]}) #3 , 'sticky': 'ew', 'padding': [7,2] 
        },

     "Horizontal.Scrollbar.trough": {"element create":
            ('image', 'trough-horiz',
             {"border": 2, 'width': 32, 'height':21})}, # , 'sticky': 'ew'

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
             ('pressed', 'slider-va'),
             ('active', 'slider-va'),
             {"border": [2,9]})
        },


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
fr1.grid(column=0,row=11,sticky='nsew')

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

root.mainloop()

'''
widg.place(x=5, y=5, width=150)
widg.set(0.2,0.3)

widg1.place(x=25, y=75, height=150)
widg1.set(0.2,0.3)
            
,
'''            
