'''
Ensure that the indentations work

Create theme extract for custom widgets, include state selection to view
the result of changing the state using different images and/or different
settings.
Entry states normal, focus; disabled, readonly;focus, readonly; normal, focus;

'''

from tkinter import Tk, PhotoImage, StringVar
from tkinter.ttk import Style, Frame, Entry
from RunState import run_state

root = Tk()

fr = Frame(root)
fr.grid(column=0,row=0,sticky='nsew')

img1 = PhotoImage("entry-n", file='../images/lime/entry-n.png')
img2 = PhotoImage("entry-i", file='../images/lime/entry-i.png')
img3 = PhotoImage("entry-d", file='../images/lime/entry-d.png')

style = Style()
# both theme_create and theme_settings worked
style.theme_create( "yummy", parent="clam", settings={
#style.theme_settings('default', {
# start of theme extract
     'Entry.field': {"element create":
          ('image', "entry-d",
           ('focus', 'entry-n'),
           ('!disabled','invalid', 'entry-i'),
            ('disabled', 'entry-d'),
           {'height': 18,'border':4,'padding':[3,4], 'sticky': 'nsew'})}

# end of theme extract - don't forget to add comma at end when inserting
     })

style.theme_use('yummy') # 'default'
sv = StringVar()
widg = Entry(fr,textvariable=sv)
widg.grid(column=0,row=18,padx=5,pady=5 )
sv.set('first')
sv1 = StringVar()
widg1 = Entry(fr,textvariable=sv1)
widg1.grid(column=0,row=19,padx=5,pady=5,sticky='ns')
sv1.set('second really really long')
run_state(fr,widg,widg1)

root.mainloop()
