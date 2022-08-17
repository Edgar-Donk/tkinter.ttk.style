'''
LabelFrame and Label loaded together

Create theme extract for custom widgets, include state selection to view
the result of changing the state using different images and/or different
settings.
There should be no interaction between label and labelframe.
We need extra internal padding so that the frame is not overwritten by the
internal widget placed inside of labelframe.
'''

from tkinter import Tk, PhotoImage, StringVar
from tkinter.ttk import Style, Label, Radiobutton, Frame, LabelFrame

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

img1 = PhotoImage("label", file='../images/piratz/label.png')
img2 = PhotoImage("label-d", file='../images/piratz/label-d.png')
img3 = PhotoImage("frame", file='../images/piratz/frame.png')
img4 = PhotoImage("frame-d", file='../images/piratz/frame-d.png')

style = Style()
# both theme_create and theme_settings worked
style.theme_create( "yummy", parent="clam", settings={
#style.theme_settings('default', {
# start of theme extract
     'Label.border': {"element create":
          ('image', "label",
           ('disabled', "label-d"),
           {'border':[19, 9, 7, 7],  'sticky': "nsew"}) # [19, 9, 7, 7]'padding':[19,3,3,3],
        },
     'Labelframe.border': {"element create":
          ('image', "frame",
           ('disabled', "frame-d"),
           {'border':7, 'padding':5, 'sticky': "nsew"}) }
# end of theme extract - don't forget to add comma at end when inserting
     })

style.theme_use('yummy') # 'default'
widg = LabelFrame(fr,text='Piratz!')
widg.grid(column=0,row=11,sticky='nsew', padx=5, pady=5, ipadx=5, ipady=5)
f0 = Label(widg,text='Something to say')
f0.grid()
widg1 = LabelFrame(fr,text='Piratz!\nextra line')
widg1.grid(column=0,row=12,sticky='nsew', padx=5, pady=5, ipadx=5, ipady=5)
f1 = Label(widg1,text='Something else to say')
f1.grid()

root.mainloop()
