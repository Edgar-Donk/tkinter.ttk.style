'''
Create theme extract for custom widgets, include state selection to view
the result of changing the state using different images and/or different
settings.
Entry states normal, focus; disabled, readonly;focus, readonly; normal, focus;

'''

from tkinter import Tk, PhotoImage, StringVar
from tkinter.ttk import Style, Label, Radiobutton, Frame, Entry

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

img1 = PhotoImage("entry-n", file='../images/piratz/entry-n.png')
img2 = PhotoImage("entry-f", file='../images/piratz/entry-f.png')
img3 = PhotoImage("entry-d", file='../images/piratz/entry-d.png')

style = Style()
# both theme_create and theme_settings worked
style.theme_create( "yummy", parent="clam", settings={
#style.theme_settings('default', {
# start of theme extract
     'Entry.field': {"element create":
          ('image', "entry-n",
           ('focus', 'entry-f'),
            ('disabled', 'entry-d'),
           {'height': 18,'border':[10,10],'padding':[3,4], 'sticky': 'nsew'})}
     
# end of theme extract - don't forget to add comma at end when inserting
     })

style.theme_use('yummy') # 'default'
sv = StringVar()
widg = Entry(fr,textvariable=sv)
widg.grid(column=0,row=10,padx=5,pady=5 )
sv.set('first')
sv1 = StringVar()
widg1 = Entry(fr,textvariable=sv1)
widg1.grid(column=0,row=11,padx=5,pady=5,sticky='ns')
sv1.set('second really really long')

root.mainloop()
