'''
Treeview

Create theme extract for custom widgets, include state selection to view
the result of changing the state using different images and/or different
settings.
Selection of border and padding a little tricky.
'''

from tkinter import Tk, PhotoImage, font
from tkinter.ttk import Style, Frame, Treeview
from RunState import run_state

root = Tk()

colors = {'bordercolor': '#7FFFD4',
            "selectbg": "#2d2d66",
            "selectfg": "#ffffff"}


fr = Frame(root)
fr.grid(column=0,row=0,sticky='nsew')


img1 = PhotoImage("sail", file='../images/piratz/sail.png')
img2 = PhotoImage("sail-d", file='../images/piratz/sail-d.png')
img3 = PhotoImage("sail-p", file='../images/piratz/sail-p.png')
img4 = PhotoImage("sail-s", file='../images/piratz/sail-s.png')

style = Style()
fact = font.Font(font="TkDefaultFont").metrics('linespace')
style.configure('font.Treeview', rowheight=fact,
              font=font.nametofont("TkDefaultFont"))
test_size = font.Font(family="Times", size=12, weight="bold").measure('Test')
mult = int(test_size / 30)
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
       # added map to treeview for selection
       'Treeview': {'configure': {'bordercolor': colors['bordercolor']},
          "map": {"background": [("selected", colors["selectbg"])],
            "foreground": [("selected", colors["selectfg"])]}},

# end of theme extract - don't forget to add comma at end when inserting
     })

style.theme_use('yummy') # 'default'
dataCols = ('Name', 'hash')
treeData = (('alice blue', '#F0F8FF'),('azure', '#F0FFFF'), ('brown4', '#8B2323'))
widg = Treeview(fr, columns=dataCols, show='headings',height=6*mult,
                style='font.Treeview')
for col in dataCols:
    widg.heading(col, text=col.title())
    widg.column(col, width=75*mult)
for ix, item in enumerate(treeData):
    widg.insert('', 'end', values=item)
widg.grid(column=0,row=11,sticky='nsew', padx=5, pady=5)
run_state(fr,widg)

root.mainloop()
