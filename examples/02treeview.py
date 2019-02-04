'''
Using Treeview to compare the effects of changing the theme with a customised configure.
Since Treeview is a composite widget we require 2 configure clauses - one for the heading
the other for the content of the contents. 

The first treeview is the theme standard, the second treeview is configured. 

The content of Text has been formatted to display the layout in a more pleasing manner
than normal.
'''

from tkinter import Tk, Text
from tkinter.ttk import Style, Combobox, Label, Treeview

def theme_changed(theme): # layout refreshed when the theme is changed
    style.theme_use(theme)
    lay = style.layout('Treeview')
    lay1 = style.layout('Treeview.Heading')
    data = " ".join(str(x) for x in lay) # this can be changed to lay1 if looking at heading layout
    spos = 0
    apos = 0
    ipos = 0
    maxsize = 0
    step = 0
    indent = '    '
    # 1 opening bracket removed when converting to string, step starts from 0
    nrBrackets = data.count('[') 
    while apos != -1:
        apos = data.find(('(' if apos==0 else '['), ipos ) 
        ipos = data.find('{',spos)
        spos = data.find(': [', apos )
        if step == 0:
            elo = '[' + data[apos: ipos] + '\n  ' + data[ipos: spos] + ':'
            adj = len('[' + data[apos: ipos])
        elif step < nrBrackets:
            elo = step*indent + data[apos - 1: ipos] + '\n' +'  ' + step*indent + data[ipos - 1: spos + 1]
        else:
            elo = step*indent + data[apos - 1: ipos] + '\n  ' + step*indent + data[ipos - 1: spos] + ']'
        if len(elo) > maxsize:
            maxsize = len(elo)
        if apos != -1:
            te.insert('end', elo + '\n') # layout information inserted into the Text widget
        step = step + 1
        
    style.configure(
        'Custom.Treeview.Heading',
        background='#FFFFFF', # White
        bordercolor='#00FF00', # Green
        lightcolor='#FF0000', # Red
        darkcolor='#0000FF', # Blue
        borderwidth=4,
        foreground='#00FFFF', # Cyan
        fieldbackground='#FF00FF', # Magenta
        troughcolor='#FFFF00', # Yellow
        arrowcolor='#A52A2A', # brown
        focuscolor='#40E0D0' # turquoise
    )
    
    style.configure(
        'Custom.Treeview',
        background='#FFFF00', # Yellow
        bordercolor='#00FF00', # Green
        lightcolor='#FF0000', # Red
        darkcolor='#0000FF', # Blue
        borderwidth=4,
        foreground='#FF00FF', # Magenta
        fieldbackground='#00FFFF', # Cyan
        troughcolor='#FFFFFF', # White
        arrowcolor='#A52A2A', # brown
        focuscolor='#40E0D0' # turquoise
    )
    return maxsize - adj, step 

root = Tk()
style = Style()
la0 =Label(root, text="Treeview layout, may change with the theme")
la0.pack(pady=5)
te = Text(root, bg='#FFFFBB')
te.pack(pady=5)
la1 =Label(root, text="Select the theme")
la1.pack(pady=5)

combo = Combobox(root, values=sorted(style.theme_names()), state='readonly')
combo.set(style.theme_use())
combo.bind('<<ComboboxSelected>>', lambda _e: theme_changed(combo.get()))
combo.pack(pady=5)

out = theme_changed(style.theme_use())
te['width'] = out[0]
te['height'] = out[1]
dataCols = ('Name', 'hash')
treeData = (('alice blue', '#F0F8FF'),
                        ('azure', '#F0FFFF'), ('brown4', '#8B2323'))
w = Treeview(root, columns=dataCols, show='headings')
for col in dataCols:
    w.heading(col, text=col.title())
    w.column(col, width=75)
for ix, item in enumerate(treeData):
    w.insert('', 'end', values=item)
w.pack(padx=5, pady=5)
w2 = Treeview(root, columns=dataCols, show='headings',
                    style='Custom.Treeview') #.Heading')
for col in dataCols:
    w2.heading(col, text=col.title())
    w2.column(col, width=75)
for ix, item in enumerate(treeData):
    w2.insert('', 'end', values=item)
w2.pack(padx=5, pady=5)

root.mainloop()
