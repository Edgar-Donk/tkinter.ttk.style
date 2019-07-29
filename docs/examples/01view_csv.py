from tkinter import Tk, StringVar, font
from tkinter.ttk import Frame, Treeview , Label, Scrollbar, Style, Entry, Combobox, Notebook
import csv
from glob import glob
from tree import Tree

'''Loads treeview to view tables

    Tables are in csv format to be viewed as multicolumn data.
    Select required table from combobox field
    Delimiters are assumed to be ";" or ","
'''

def csvSel(event):
    #print(csv_value.get())
    with open(csv_value.get()) as f:
        first_line = f.readline()
    csvDelimiter = (';' if ";" in first_line else ',')

    Tree(page2,csv_value.get(),csvDelimiter,renew=True)
    
def on_tab_changed(event):
        event.widget.update_idletasks()
        tab = event.widget.nametowidget(event.widget.select())
        event.widget.configure(height=tab.winfo_reqheight(),width=tab.winfo_reqwidth())

root = Tk()
root.wm_title("Tables with Style")
root.wm_iconbitmap('../_static/ben.ico')
root.geometry('+170+200')
s = Style()
s.theme_use('clam')

csvDelimiter = ','
fr = Frame(root) 
fr.pack(fill='both')

nb = Notebook(fr) 
nb.pack(fill='both', padx=2, pady=3)
nb.bind("<<NotebookTabChanged>>", on_tab_changed)

page1 = Frame(nb) 
csvfiles = []
for file in glob("../tables/*.csv"):
    csvfiles.append(file)
csv_value = StringVar()
cb = Combobox(page1, values=csvfiles, state="readonly",
              textvariable=csv_value, width=30)
cb.set(csvfiles[0])
cb.grid(column=0, row=1)
cb.bind('<<ComboboxSelected>>', csvSel)

nb.add(page1, text="Find CSV")

page2 = Frame(nb, name='page2')

Tree(page2,csv_value.get(),csvDelimiter=',')
        
nb.add(page2, text="Show CSV")

if __name__ == "__main__":
    fr.mainloop()
