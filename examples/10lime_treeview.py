'''
Treeview

Create theme extract for custom widgets, include state selection to view
the result of changing the state using different images and/or different
settings.
'''

from tkinter import Tk, PhotoImage, StringVar
from tkinter.ttk import Style, Frame, Treeview
from RunState import run_state

root = Tk()

colours = {"selectbg": '#5D9B90', #"#657a9e",
           "selectfg": "#ffffff"}

fr = Frame(root)
fr.grid(column=0,row=0,sticky='nsew')

img1 = PhotoImage("slider-hn", file='../images/lime/slider-hn.png')
img2 = PhotoImage("slider-hd", file='../images/lime/slider-hd.png')
img3 = PhotoImage("slider-hp", file='../images/lime/slider-hp.png')
img4 = PhotoImage("slider-ha", file='../images/lime/slider-ha.png')

style = Style()
# both theme_create and theme_settings worked
style.theme_create( "yummy", parent="clam", settings={
#style.theme_settings('default', {
# start of theme extract
     'Treeheading.cell': {"element create":
          ('image', "slider-hn",
           ('pressed', "slider-hp"),
           ('active', "slider-ha"),
           ('focus', "slider-ha"),
           ('disabled', "slider-hd"),
           
           
           {'border':[4,12,4,12], 'padding':4, 'sticky': "nsew"} 
        ) },
         'Treeview': {'map':{'background':[('selected', colours['selectbg'])],
                      'foreground': [('selected',colours['selectfg'])]}}
     
       #'Treeview': {'configure': {'bordercolor': colours['bordercolor']}}, 
         
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
run_state(fr,widg)


root.mainloop()
