'''
Radio Buttons

Create theme extract for custom widgets, include state selection to view
the result of changing the state using different images and/or different
settings.

'''

from tkinter import Tk, PhotoImage
from tkinter.ttk import Style, Label, Radiobutton, Frame
from RunState import run_state

root = Tk()


fr = Frame(root)
fr.grid(column=0,row=0,sticky='nsew')

img1 = PhotoImage("radio", file='../images/piratz/radio.png')
img2 = PhotoImage("radio-s", file='../images/piratz/radio-s.png')
img3 = PhotoImage("radio-d", file='../images/piratz/radio-d.png')
img4 = PhotoImage("radio-a", file='../images/piratz/radio-a.png')

style = Style()
# both theme_create and theme_settings worked
style.theme_create( "yummy", parent="clam", settings={
#style.theme_settings('default', {
# start of theme extract
     'Radiobutton.indicator': {"element create":
          ('image', "radio",
            ('active', "radio-a"),
           ('selected', "radio-s"),
            ('disabled', "radio-d"),
           {'width':20, 'sticky': "w"})
        }
# end of theme extract - don't forget to add comma at end when inserting
     })

style.theme_use('yummy') # 'default'
widg = Radiobutton(fr,text='Piratz!')
widg.grid(column=0,row=11,sticky='nsew', padx=5, pady=5)
widg1 = Radiobutton(fr,text='Piratz!\nextra line')
widg1.grid(column=0,row=12,sticky='nsew', padx=5, pady=5)
run_state(fr,widg,widg1)

root.mainloop()
