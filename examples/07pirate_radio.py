'''
Create theme extract for custom widgets, include state selection to view
the result of changing the state using different images and/or different
settings.

'''

from tkinter import Tk, PhotoImage, StringVar
from tkinter.ttk import Style, Label, Radiobutton, Frame

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

img1 = PhotoImage("radio", file='../images/piratz/radio.png')
img2 = PhotoImage("radio-s", file='../images/piratz/radio-s.png')

style = Style()
# both theme_create and theme_settings worked
style.theme_create( "yummy", parent="clam", settings={
#style.theme_settings('default', {
# start of theme extract
     'Radiobutton.indicator': {"element create":
          ('image', "radio",
           ('selected', "radio-s"),
           {'width':20, 'sticky': "w"}) 
        }
# end of theme extract - don't forget to add comma at end when inserting
     })

style.theme_use('yummy') # 'default'
widg = Label(fr,text='Piratz!')
widg.grid(column=0,row=11,sticky='nsew', padx=5, pady=5)
widg1 = Label(fr,text='Piratz!\nextra line')
widg1.grid(column=0,row=12,sticky='nsew', padx=5, pady=5)

root.mainloop()
