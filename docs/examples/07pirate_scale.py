'''
Create theme extract for custom widgets, states are selected according to
one of two functions which change the state according to the value of
the scale. 
Ensure that the vertical and horizontal widgets are run in separate frames,
or ensure that the second widget does not expand or else the widgets interact.
'''

from tkinter import Tk, PhotoImage, StringVar
from tkinter.ttk import Style, Label, Radiobutton, Frame, Scale

root = Tk()

def slide_move(val):
    v = int(float(val))
    imgw = {0:['readonly','!selected','!background','!focus','!active'],
               1:['selected','!readonly','!background','!focus','!active']}
    if v >= 0 and v < 10 :
        widg.state(['active','!readonly','!selected'])
    elif v > 80 and v < 91:
        widg.state(['focus','!background','!readonly','!selected'])
    elif v > 90 and v < 100:
        widg.state(['background','!invalid','!focus'])
    elif v == 100 :
        widg.state(['invalid','!background'])
    else:
        widg.state(imgw[v%2])

def slide_vert(val):
    v = int(float(val))
    imgw = {0:['background','!selected','!invalid','!active'],
               1:['selected','!invalid','!background','!active']}
    if v >= 0 and v < 5 :
        widg1.state(['active','!background','!selected'])
#    elif v > 95 and v < 100:
#        widg.state(['background','!invalid'])
    elif v >90:
        widg1.state(['invalid','!selected','!background'])
    else:
        widg1.state(imgw[v%2])        

fr = Frame(root)
fr.grid(column=0,row=0,sticky='nsew')

img1 = PhotoImage("trough-sea", file='../images/piratz/trough-sea.png')
img2 = PhotoImage("trough-tabletop", file='../images/piratz/trough-tabletop.png')
img3 = PhotoImage("trough-beach", file='../images/piratz/trough-beach.png')
img4 = PhotoImage("slider-horiz-map", file='../images/piratz/slider-horiz-map.png')
img5 = PhotoImage("slider-horiz-c-chest", file='../images/piratz/slider-horiz-c-chest.png')
img6 = PhotoImage("slider-horiz-o-chest", file='../images/piratz/slider-horiz-o-chest.png')
img7 = PhotoImage("slider-horiz-wheel", file='../images/piratz/slider-horiz-wheel.png')
img8 = PhotoImage("slider-horiz-wheelp", file='../images/piratz/slider-horiz-wheelp.png')
img9 = PhotoImage("trough-scale-vert", file='../images/piratz/trough-scale-vert.png')
img10 = PhotoImage("slider-s-vert-i", file='../images/piratz/slider-s-vert-i.png')
img11 = PhotoImage("slider-s-vert-b", file='../images/piratz/slider-s-vert-b.png')
img12 = PhotoImage("slider-s-vert-s", file='../images/piratz/slider-s-vert-s.png')
img13 = PhotoImage("slider-s-vert", file='../images/piratz/slider-s-vert.png')
img14 = PhotoImage("slider-horiz-ben", file='../images/piratz/slider-horiz-ben.png')

style = Style()
# both theme_create and theme_settings worked
style.theme_create( "yummy", parent="clam", settings={
#style.theme_settings('default', {
# start of theme extract
     'Horizontal.Scale.trough': {"element create":
          ('image', "trough-tabletop",
           ('background', 'trough-beach'),
           ('focus', 'trough-beach'),
           ('invalid', 'trough-beach'),
           ('readonly', 'trough-sea'),
           ('selected', 'trough-sea')
           )},
     'Horizontal.Scale.slider': {"element create":
          ('image', "slider-horiz-map", 
           ('background', "slider-horiz-c-chest"),
           ('invalid', "slider-horiz-o-chest"),
           ('focus', 'slider-horiz-ben'),
           ('readonly', 'slider-horiz-wheel'),
           ('selected', 'slider-horiz-wheelp'),
           {'border':3})
        },
     'Vertical.Scale.trough': {"element create":
          ('image', "trough-scale-vert",
           )},
     'Vertical.Scale.slider': {"element create":
          ('image', "slider-s-vert", 
           ('background', "slider-s-vert-b"),
           ('invalid', "slider-s-vert-i"),
           ('selected', 'slider-s-vert-s'),
           {'border':3})
        }
# end of theme extract - don't forget to add comma at end when inserting
     })

style.theme_use('yummy') # 'default'
widg = Scale(fr,from_=0, to=100, length=200,orient='horizontal',command=slide_move)
widg.grid(column=0,row=0,sticky='nsew', padx=5, pady=5)

widg1 = Scale(fr,from_=100, to=0, length=200,orient='vertical',command=slide_vert)
widg1.grid(column=0,row=2, padx=5, pady=5) 


root.mainloop()

'''
,
     'Vertical.Progressbar.trough': {"element create":
          ('image', "trough-pbar-vert",
           {'border':3})},
     'Vertical.Progressbar.pbar': {"element create":
          ('image', "pbar-gull-a", 
           ('background', '!active', '!invalid', "pbar-gull-b"),
           ('invalid', '!active', '!background', "pbar-gull-b"),
           {'border':[9, 2]})
        }
'''        
