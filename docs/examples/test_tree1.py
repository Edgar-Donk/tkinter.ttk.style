

from tkinter import Tk, font
from tkinter.ttk import Frame, Style, Treeview, Label

root = Tk()
style = Style()
fact = font.Font(font="TkDefaultFont").metrics('linespace')
style.configure('font.Treeview', rowheight=fact, # only works with 'vista'
              font=font.nametofont("TkDefaultFont"))
test_size = font.Font(family="Times", size=12, weight="bold").measure('Test')
mult = int(test_size / 30)
style.theme_use('vista')

fr = Frame(root)
fr.grid(column=0, row=0, sticky='nsew')
l = Label(fr, text=style.theme_use())
l.grid(column=0, row=0)
dataCols = ('Name', 'hash')
treeData = (('alice blue', '#F0F8FF'),('azure', '#F0FFFF'), ('brown4', '#8B2323'))
widg = Treeview(fr, columns=dataCols, show='headings',height=6*mult, 
                style='font.Treeview')
for col in dataCols:
    widg.heading(col, text=col.title())
    widg.column(col, width=75*mult)  
for ix, item in enumerate(treeData):
    widg.insert('', 'end', values=item)
widg.grid(column=0,row=1,sticky='nsew', padx=5, pady=5)
root.mainloop()