'''
Create theme extract for custom widgets, states are selected according to
one of two functions which change the state according to the value of
the scale.
Ensure that the vertical and horizontal widgets are run in separate frames,
or ensure that the second widget does not expand or else the widgets interact.

The slider is 9 pixels wide, the trough has a border 6 pixels wide
'''

from tkinter import Tk, PhotoImage
from tkinter.ttk import Style, Frame, Scale
from RunState import run_state

root = Tk()

fr = Frame(root)
fr.grid(column=0,row=0,sticky='nsew')

img1 = PhotoImage("slider", file='../images/lime/slider.png')
img2 = PhotoImage("vslider", file='../images/lime/vslider.png')
img3 = PhotoImage("slider-p", file='../images/lime/slider-p.png')
img4 = PhotoImage("vslider-p", file='../images/lime/vslider-p.png')
img5 = PhotoImage("scale-nt", file='../images/lime/scale-nt.png') # slider-t.png
img6 = PhotoImage("vslider-t", file='../images/lime/vslider-t.png')
img7 = PhotoImage("scale-dt", file='../images/lime/scale-dt.png') # slider-t.png


style = Style()
# both theme_create and theme_settings worked
style.theme_create( "yummy", parent="clam", settings={
#style.theme_settings('default', {
# start of theme extract
     'Horizontal.Scale.trough': {"element create":
          ('image', "scale-nt",
           ('disabled', "scale-dt"),
            {'border':[6,0,6,0],'sticky': 'wes'})}, # [6,0,6,0]
     'Horizontal.Scale.slider': {"element create":
          ('image', "slider",
           ('pressed','!disabled', "slider-p"),
           {'border':3})
        },
     'Vertical.Scale.trough': {"element create":
          ('image', "vslider-t",
           {'border':[0,6,0,6],'sticky': 'nes'})}, # [0,6,0,6]
     'Vertical.Scale.slider': {"element create":
          ('image', "vslider",
           ('pressed','!disabled', "vslider-p"),
           {'border':3})
        }
# end of theme extract - don't forget to add comma at end when inserting
     })

style.theme_use('yummy') # 'default'
widg = Scale(fr,from_=0, to=100, length=200,orient='horizontal')
widg.grid(column=0,row=13,sticky='nsew', padx=5, pady=5)

widg1 = Scale(fr,from_=100, to=0, length=200,orient='vertical')
widg1.grid(column=0,row=14, padx=5, pady=5)
run_state(fr,widg,widg1)

root.mainloop()


