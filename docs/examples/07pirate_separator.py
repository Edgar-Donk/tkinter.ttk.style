'''
Vertical Separator tricky

Create theme extract for custom widgets.
Separator problems with vertical images because we have no distinct
vertical separator component, if we use the same image for both orientations,
the vertical widget does not look particurly clever. Uncomment the extra
line for the second state, change the border value from 3 to 2, uncomment
the line for widg1 state call.
'''

from tkinter import Tk, PhotoImage, StringVar
from tkinter.ttk import Style, Label, Frame, Separator 

root = Tk()

fr = Frame(root)
fr.grid(column=0,row=0,sticky='nsew')

img1 = PhotoImage("separator", file='../images/piratz/separator.png')
img2 = PhotoImage("separator-v", file='../images/piratz/separator-v.png')

style = Style()
# both theme_create and theme_settings worked
style.theme_create( "yummy", parent="clam", settings={
#style.theme_settings('default', {
# start of theme extract
     'Separator.separator': {"element create":
          ('image', "separator",
           #('invalid', "separator-v"), ## uncomment when using 2nd state
           {'border':[3],'sticky': 'nsew'})} ## change from 3 to 2
# end of theme extract - don't forget to add comma at end when inserting
     })

fr1 = Frame(fr, height=250, width=250)
fr1.grid(column=1,row=0,sticky='nsew', padx=5, pady=5)                    
style.theme_use('yummy') # 'default'
widg = Separator(fr1,orient="horizontal")
widg.place(x=5, y=5, width=150)

widg1 = Separator(fr1,orient="vertical")
#widg1.state(['invalid']) ## uncomment when using 2nd state
widg1.place(x=75, y=50, height=150, width=8) #, width=5


root.mainloop()
