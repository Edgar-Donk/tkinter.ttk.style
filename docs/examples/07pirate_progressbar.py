'''
Create theme extract for custom widgets, states are selected according to
one of two functions which change the state according to the value of
the progress bar. The selection of the trough border a little tricky,
which is increased to 4 to allow blue sea to show without extra horiz lines.
Make sure that the progress bars are fixed to the same size as the image,
otherwise the trough looks odd.
Ensure that the vertical and horizontal widgets are run in separate frames,
or ensure that the second widget does not expand or else the widgets interact.
The different images require negative states to ensure that the images
change as expected.
'''

from tkinter import Tk, PhotoImage, font
from tkinter.ttk import Style, Frame, Progressbar

root = Tk()

dir0 = 1
dir1 = 1
def steer():
    global dir0
    widg['value'] += 1 * dir0
    if widg['value'] == 100:
        widg.state(['background','!active'])
        dir0 = -1
        widg.after(50, steer)
    elif widg['value'] == 0:
        widg.state(['active','!background'])
        dir0 = 1
        widg.after(50, steer)
    else:
        widg.after(50, steer)

def steer1():
    global dir1
    widg1['value'] += 1 * dir1
    if widg1['value'] == 0 : # (dir1-1)*100+16
        widg1.state(['active','!invalid','!background'])
        dir1 = 1
        widg1.after(40, steer1)
    elif widg1['value'] == 16 : # (dir1-1)*100+16
        widg1.state(['background','!invalid','!active'])
        widg1.after(40, steer1)
    elif widg1['value'] == 33 :
        widg1.state(['invalid','!background','!active'])
        widg1.after(40, steer1)
    elif widg1['value'] == 50 :
        widg1.state(['active','!invalid','!background'])
        widg1.after(40, steer1)
    elif widg1['value'] == 66 :
        widg1.state(['background','!invalid','!active'])
        widg1.after(40, steer1)
    elif widg1['value'] == 83 :
        widg1.state(['invalid','!background','!active'])
        widg1.after(40, steer1)
    elif widg1['value'] == 100 :
        widg1.state(['active','!invalid','!background'])
        dir1 = -1
        widg1.after(40, steer1)
    else:
        widg1.after(40, steer1)    

fr = Frame(root)
fr.grid(column=0,row=0,sticky='nsew')

img1 = PhotoImage("trough-pbar-vert", file='../images/piratz/trough-pbar-vert.png')
img2 = PhotoImage("trough-pbar-horiz", file='../images/piratz/trough-pbar-horiz.png')
img3 = PhotoImage("pbar-boat-a", file='../images/piratz/pbar-boat-a.png')
img4 = PhotoImage("pbar-boat-b", file='../images/piratz/pbar-boat-b.png')
img5 = PhotoImage("pbar-gull-b", file='../images/piratz/pbar-gull-b.png')
img6 = PhotoImage("pbar-gull-i", file='../images/piratz/pbar-gull-i.png')
img7 = PhotoImage("pbar-gull-a", file='../images/piratz/pbar-gull-a.png')

style = Style()
# both theme_create and theme_settings worked
style.theme_create( "yummy", parent="clam", settings={
#style.theme_settings('default', {
# start of theme extract
     'Horizontal.Progressbar.trough': {"element create":
          ('image', "trough-pbar-horiz",
           {'border':4})},
     'Horizontal.Progressbar.pbar': {"element create":
          ('image', "pbar-boat-a", 
           ('background', '!active', "pbar-boat-b"),
           {'border':[2, 9]})
        },
     'Vertical.Progressbar.trough': {"element create":
          ('image', "trough-pbar-vert",
           {'border':3})},
     'Vertical.Progressbar.pbar': {"element create":
          ('image', "pbar-gull-a", 
           ('background', '!active', '!invalid', "pbar-gull-b"),
           ('invalid', '!active', '!background', "pbar-gull-b"),
           {'border':[9, 2]})
        }
# end of theme extract - don't forget to add comma at end when inserting
     })

style.theme_use('yummy') # 'default'
test_size = font.Font(family="Times", size=12, weight="bold").measure('Test')
mult = int(test_size / 30)
widg = Progressbar(fr,length=150*mult,orient='horizontal',mode='indeterminate')
widg.grid(column=0,row=0,sticky='nsew', padx=5, pady=5)
steer()

widg1 = Progressbar(fr,length=150*mult,orient='vertical',mode='indeterminate')
widg1.grid(column=0,row=2, padx=5, pady=5) 
steer1()

root.mainloop()
