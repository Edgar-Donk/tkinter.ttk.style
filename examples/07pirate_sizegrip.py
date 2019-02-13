'''
Create theme extract for custom widgets.
'''

from tkinter import Tk, PhotoImage, StringVar
from tkinter.ttk import Style, Label, Radiobutton, Frame, Sizegrip 

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

img1 = PhotoImage("sizegrip", file='../images/piratz/sizegrip.png')

style = Style()
# both theme_create and theme_settings worked
style.theme_create( "yummy", parent="clam", settings={
#style.theme_settings('default', {
# start of theme extract
     'sizegrip': {"element create":
          ('image', "sizegrip")}
# end of theme extract - don't forget to add comma at end when inserting
     })

style.theme_use('yummy') # 'default'
root.columnconfigure(0, weight = 1)
root.rowconfigure(0, weight = 1)
widg = Sizegrip(root)
widg.grid(row=1,column=1,sticky='se')

root.mainloop()
