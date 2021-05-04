'''
LabelFrame and Label loaded together

Create theme extract for custom widgets, include state selection to view
the result of changing the state using different images and/or different
settings.
There should be no interaction between label and labelframe.
We need extra internal padding so that the frame is not overwritten by the
internal widget placed inside of labelframe.
'''

from tkinter import Tk, PhotoImage
from tkinter.ttk import Style, Label, Frame, LabelFrame
from RunState import run_state

root = Tk()

fr = Frame(root)
fr.grid(column=0,row=0,sticky='nsew')

img2 = PhotoImage("frame-d", file='../images/piratz/frame-d.png')
img1 = PhotoImage("frame", file='../images/piratz/frame.png')

style = Style()
# both theme_create and theme_settings worked
style.theme_create( "yummy", parent="clam", settings={
#style.theme_settings('default', {
# start of theme extract
     'Labelframe.border': {"element create":
          ('image', "frame",
           ('disabled', "frame-d"),
           {'border':5, 'sticky': "nsew"}) } #'padding':5,
# end of theme extract - don't forget to add comma at end when inserting
     })

style.theme_use('yummy') # 'default'
widg = LabelFrame(fr,text='Piratz!')
widg.grid(column=0,row=11,sticky='nsew', padx=5, pady=5, ipadx=5, ipady=5)
f0 = Label(widg,text='Something to say')
f0.grid()
widg1 = LabelFrame(fr,text='Piratz!\nextra line')
widg1.grid(column=0,row=12,sticky='nsew',padx=5,pady=5,ipadx=5,ipady=5) #  ipadx=5, ipady=5
f1 = Label(widg1,text='Something else to say\nwith an extra line')
f1.grid()
run_state(fr,widg,widg1)

root.mainloop()
