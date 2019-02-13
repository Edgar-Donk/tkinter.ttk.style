'''
Create theme extract for custom widgets, include state selection to view
the result of changing the state using different images and/or different
settings.
Selection of border and padding a little tricky.
'''

from tkinter import Tk, PhotoImage, StringVar
from tkinter.ttk import Style, Label, Radiobutton, Frame, Treeview

root = Tk()

def change_state():
    oldstate = widg.state()
    if len(oldstate) > 0:
        # convert tuple to string 
        oldst = " ".join(str(x) for x in oldstate) 
        widg.state(['!'+oldst])
        #widg1.state(['!'+oldst])
    newstate = state_val.get()
    widg.state([newstate])
    #widg1.state([newstate])

colours = {'bordercolor': '#7FFFD4'}
    

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

img1 = PhotoImage("sail", file='../images/piratz/sail.png')
img2 = PhotoImage("sail-d", file='../images/piratz/sail-d.png')
img3 = PhotoImage("sail-p", file='../images/piratz/sail-p.png')
img4 = PhotoImage("sail-s", file='../images/piratz/sail-s.png')

style = Style()
# both theme_create and theme_settings worked
style.theme_create( "yummy", parent="clam", settings={
#style.theme_settings('default', {
# start of theme extract
     'Treeheading.cell': {"element create":
          ('image', "sail",
           ('selected', "sail-s"),
           ('disabled', "sail-d"),
           ('pressed', "sail-s"),
           ('active', "sail-p"),
           {'border':[30, 17, 27, 32], 'padding':[13,8,18,21], 'sticky': "nsew"} 
        ) },
       'Treeview': {'configure': {'bordercolor': colours['bordercolor']}}, 
         
# end of theme extract - don't forget to add comma at end when inserting
     })

style.theme_use('yummy') # 'default'
dataCols = ('Name', 'hash')
treeData = (('alice blue', '#F0F8FF'),('azure', '#F0FFFF'), ('brown4', '#8B2323'))
widg = Treeview(fr, columns=dataCols, show='headings',height=6)
for col in dataCols:
    widg.heading(col, text=col.title())
    widg.column(col, width=75)
for ix, item in enumerate(treeData):
    widg.insert('', 'end', values=item)    
widg.grid(column=0,row=11,sticky='nsew', padx=5, pady=5)
'''
widg1 = Notebook(fr)
widg1.grid(column=0,row=12,sticky='nsew', padx=5, pady=5)
widg1.add(page1,text='Piratz!')
widg1.add(page2,text='Piratz!\nextra line')
'''
root.mainloop()
