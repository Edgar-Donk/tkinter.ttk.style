'''
Create theme extract for custom widgets.
'''

from tkinter import Tk, PhotoImage, font
from tkinter.ttk import Style, Frame, Sizegrip 

root = Tk()
test_size = font.Font(family="Times", size=12, weight="bold").measure('Test')
mult = int(test_size / 30)
fr = Frame(root, height=50*mult)
fr.grid(column=0,row=0,sticky='nsew')

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
