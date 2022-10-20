'''
Notebook

Create theme extract for custom widgets, include state selection to view
the result of changing the state using different images and/or different
settings.
'''

from tkinter import Tk, PhotoImage
from tkinter.ttk import Style, Frame, Notebook
from RunState import run_state

root = Tk()

colours = {'bordercolor': '#7FFFD4'}

fr = Frame(root)
fr.grid(column=0,row=0,sticky='nsew')

img1 = PhotoImage("tab-n", file='../images/lime/tab-nx.png')
img2 = PhotoImage("tab-d", file='../images/lime/tab-dx.png')
img3 = PhotoImage("tab-p", file='../images/lime/tab-px.png')
img4 = PhotoImage("tab-h", file='../images/lime/tab-hx.png')

style = Style()
# both theme_create and theme_settings worked
style.theme_create( "yummy", parent="clam", settings={
#style.theme_settings('default', {
# start of theme extract
        # tabmargins allow enough space for expand
    'TNotebook': {'configure': {'tabmargins': [0,3,0,0]}}, # [2,7,5,5]
    'TNotebook.tab': {
        'configure': { 'foreground': '#8b0a50'},
        "map":
        {'expand': [('selected', [0,3,0,0]),('!selected', [0,0,2])]}},


     'tab': {"element create":
          ('image', "tab-n",
           ('active', "tab-h"),
           ('selected', "tab-p"),
           ('disabled', "tab-d"),
           {'border':[4, 15, 4, 15], 'padding':[7,3],'sticky': "nsew"} # ,'height':12
        ) }


# end of theme extract - don't forget to add comma at end when inserting
     })

style.theme_use('yummy') # 'default'
widg = Notebook(fr)
page1 = Frame(widg, width=150, height=150)
page2 = Frame(widg, width=150, height=150)
widg.add(page1,text='Piratz!')
widg.add(page2,text='Piratz! two')
widg.grid(column=0,row=18,sticky='nsew', padx=5, pady=5)
run_state(fr,widg)

root.mainloop()
