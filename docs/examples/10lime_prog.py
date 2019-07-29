from tkinter import Tk, PhotoImage
from tkinter.ttk import Style, Frame, Progressbar

root = Tk()

fr = Frame(root)
fr.grid(column=0,row=0,sticky='nsew')

img1 = PhotoImage("slider-va", file='../images/lime/slider-va.png')
img2 = PhotoImage("slider-ha", file='../images/lime/slider-ha.png')
img3 = PhotoImage("hprog", file='../images/lime/rprog.png') # hprog
img4 = PhotoImage("vprog", file='../images/lime/iprog.png') # vprog

style = Style()
# both theme_create and theme_settings worked
style.theme_create( "yummy", parent="clam", settings={
#style.theme_settings('default', {
# start of theme extract
     'Horizontal.Progressbar.trough': {"element create":
          ('image', "slider-ha",
           {'border':[9,2]})},
     'Horizontal.Progressbar.pbar': {"element create":
          ('image', "hprog", 
           {'border':4})
        },
     'Vertical.Progressbar.trough': {"element create":
          ('image', "slider-va",
           {'border':[2,9]})},
     'Vertical.Progressbar.pbar': {"element create":
          ('image', "vprog", 
           {'border':4})
        }
# end of theme extract - don't forget to add comma at end when inserting
     })

style.theme_use('yummy') # 'default'

widg = Progressbar(fr,length=150,orient='horizontal',mode='indeterminate')
widg.grid(column=0,row=0,sticky='nsew', padx=5, pady=5)


widg1 = Progressbar(fr,length=150,orient='vertical',mode='indeterminate')
widg1.grid(column=0,row=2, padx=5, pady=5) 


root.mainloop()
