from tkinter import Tk, font
from tkinter.ttk import Frame, Treeview , Label, Scrollbar, Style
import csv

class Tree:
    def __init__(self,fra,csvFile,csvDelimiter=',',renew=False):
        self.fra = fra
        self.csvFile = csvFile
        self.csvDelimiter = csvDelimiter
        self.renew = renew
        self.treeColumns = []
        self.treeData = []
        if renew:
            del self.treeColumns[:]
            del self.treeData[:]
    
        with open(self.csvFile, newline='', encoding='utf-8-sig') as csvfile:
            treeCsv = csv.reader(csvfile, delimiter=csvDelimiter)
    
            for ix, row in enumerate(treeCsv):
                if ix == 0:
                    self.treeColumns = row
                else:
                    self.treeData.append(row)
                    
        self.build_tree()
        
    def build_tree(self):
        try:
            self.fr.destroy()
        except (NameError, AttributeError):
            pass
        
        self.fr = Frame(self.fra)
        self.fr.pack(fill='both', expand=False) #grid(column=0, row=1, sticky='nsew')
        
        lbl = Label(self.fr, text=self.csvFile)
        lbl.grid(column=0, row=0, sticky='n')
     
        self.tree = Treeview(self.fr,columns=self.treeColumns, show="headings", style='font.Treeview') # ,height =20
        self.tree.grid(column=0, row=1, sticky='ns')
        
        vsb = Scrollbar(self.fr,orient="vertical", command=self.tree.yview)
        vsb.grid(column=1, row=1, sticky='ns') 
        hsb = Scrollbar(self.fr,orient="horizontal", command=self.tree.xview)
        hsb.grid(column=0, row=2,  sticky='ew')
        self.tree.configure(xscrollcommand=hsb.set,yscrollcommand=vsb.set)
        self.fr.grid_columnconfigure(0, weight=1)
        self.fr.grid_rowconfigure(0, weight=1)
        
        if self.renew:
            for row in self.tree.get_children():
                self.tree.delete(row)
        
        for col in self.treeColumns:
            #print(treeColumns,col,col.title())
            self.tree.heading(col, text=col.title())
            self.tree.column(col, width=font.Font().measure(col.title()),stretch=False)
    
        for ix, item in enumerate(self.treeData):
            itemID = self.tree.insert('', 'end', values=item)
        
            for indx, val in enumerate(item):
                ilen = font.Font().measure(val) *8//9
                if self.tree.column(self.treeColumns[indx], width=None) < ilen:
                    self.tree.column(self.treeColumns[indx],width=ilen)
                
if __name__ == "__main__":
    root = Tk()
    s = Style()
    s.theme_use('clam')
    s.configure('font.Treeview.Heading', font=("DejaVu Sans Mono",'12'))
    s.configure('font.Treeview', font=("DejaVu Sans Mono",'10'))
    page1 = Frame()
    page1.pack(fill='both', expand=True) # grid(sticky='nsew')
    csvFile = '../tables/01style_commands.csv'
    app = Tree(page1,csvFile,csvDelimiter=',') 
    root.mainloop()
