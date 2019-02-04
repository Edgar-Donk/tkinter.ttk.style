'''
Using 05rounded_frame.py to make a similar procedure for labelframe.
'''
from tkinter import StringVar, Tk, IntVar, PhotoImage
from tkinter.ttk import Style, Radiobutton, Combobox, LabelFrame, Frame, Checkbutton

class App:
    def __init__(self):
        self.root = Tk()
        self.s = Style()
        self.fr = Frame(self.root)
        self.fr.grid(sticky='nsew')
        self.img = PhotoImage("frameBorder", data="""
R0lGODlhPwA/APcAAAAAAJWVlby8vMTExAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACH5BAEAAP8ALAAAAAA/AD8A
AAj/AP8JHEiwoMGDCBMqXMiwocOHECNKnEixokWGATJq3Mixo8ePF/9pDLlw48SRJB2iVBkgpcSM
LF2ebIlRJkWaCmHafIkTYc+dEH8aFAq0IVGBAnQWjRhAwMGkS086NQg1KtOpBatafdj06dGtPrES
1AoWo9iBZMvmPIv0q1qCXam6fSswbta5dO2OxftWL1q+av22pVuS7b+0hAsKPgy47GLEiQc+bgx2
cuSwXi8ftKxZsWHIlzl3lvyZ8lbRo0WWTk06M2vVrlmjHj27c23Nt0Ovfp07cu/EvwkH7zvZ9NKM
pY0XRf40qXKbyA0zfi6TOUIBznE3ld5WaV7rCbGbNQysETtD7M5XLi9v3iH6j/Djy4/OXSH69PPz
e0Qf8r7//wAG+J9LAxRo4IEIJqjggq81CFZAADs=
""")
        self.img1 = PhotoImage("frameFocusBorder", data="""
R0lGODlhPwA/APcAAAAAAP9jR5WVlby8vMTExAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACH5BAEAAP8ALAAAAAA/AD8A
AAj/AP8JHEiwoMGDCBMqXMiwocOHECNKnEixokWGAjJq3Mixo8ePF/9pDECypMmTKFOm3DhxZICQ
C0tqhJiRJMyHJDM6rPnyJs4AOjHa9AkxJ0YBPYkWDZoQqdKJQBc6fRoxKsIBNalKBDrgINakWnEK
6Grwa9iqY71OPeuQq1qwbGOmLbs2rlyyBc3aZeiWLty9B/vmrQs48NzBfwsTFExQr2LDeBsTfjyQ
8UDHlBcflpyYsmWBmDML/PwvtGjSpjOjnqx682XWnl2Dhv14defaskvTVmxbdMHevivnTh078uvb
vIfvLgw8+L/mwaH7ln5aOXLm1p2Pzq6demvjs6/vaQWqfLld8uB1m4+L3ivW9WHRp1c/tHb7q+/r
A845dv5snsyRl1tj7/Ek3kX8ZTSAf5ctyJFKEEao0kYLMpiXgx9lqOGG/VmIH4YchvhRhSFVaOKJ
KKaoIok3EeDiizDGKOOMNGpno2IBAQA7
""")
        self.s.element_create("RoundedFrame", "image", "frameBorder",
            ("focus", "frameFocusBorder"), border=16, sticky="nsew")
        self.s.layout("RoundedFrame", [("RoundedFrame", {"sticky": "nsew"})])
        self.build()

    def build(self):
        self.rbs = []
        self.rbs1 = []
        self.lF0 = lF0 = LabelFrame(self.fr, text='Widget and Themes')
        lF0.grid(row=0, column=0, sticky='nw')
        self.fr1 = fr1 = Frame(lF0)
        fr1.grid(row=0, column=0, sticky='nw')
        # create check box to select reverse selection order
        self.lF12 = lF12 = LabelFrame(fr1, text='Select Widget before Theme')
        lF12.grid(row=0, column=0, sticky='nw')
        self.ord = ord = IntVar()
        ord.set(0)
        cbut3 = Checkbutton(lF12, text='Reverse selection order', variable=ord, 
                command=self.selord)
        cbut3.grid(row=0, column=0, padx=5, pady=5)
        cbut3.state(['!selected'])
        
        # create a Combobox to choose widgets
        widget_sel = ['Button', 'Checkbutton', 'Combobox', 'Entry', 'Frame',
                      'Label', 'LabelFrame', 'Menubutton', 'Notebook', 
                      'PanedWindow', 'Progressbar', 'Radiobutton', 'Scale', 
                      'Scrollbar', 'Separator', 'Sizegrip', 'Treeview']
        ord = self.ord

        self.lf6 = LabelFrame(self.fr1, text='Select Widget', style="RoundedFrame",
                               padding=(10,1,10,10))
        self.lf6.grid(row=1, column=0, sticky='nw')
        
        self.lf6.state([("focus" if self.ord.get() == 0 else "!focus")]) 
        self.widget_value = StringVar()
        self.cb = Combobox(self.lf6, values=widget_sel,
                           textvariable=self.widget_value,
                           state= ('disabled' if self.ord.get()==1 else 'active'))
        self.cb.grid(row=0, column=0, padx=5, pady=5, sticky='nw')
        self.cb.bind('<<ComboboxSelected>>', self.enabled)

        # create a Radio Buttons to choose orientation
        fr2 = Frame(self.lF0)
        fr2.grid(row=0, column=1, sticky='nw')        
        self.lF5 = lF5 = LabelFrame(fr2, style="RoundedFrame", padding=(10,1,10,10),
            text='Orientation of \nProgressbar \nScale \nScrollbar')
        lF5.grid(row=0, column=0, padx=5, pady=5, sticky='nw')
        self.orient = StringVar()
        orientT = ['Horizontal', 'Vertical']
        for ix, val in enumerate(orientT):
            rb = Radiobutton(lF5, text=val, value=val, command=self.orient_command,
                             variable=self.orient, state='disabled')
            rb.grid(row=ix, column=0, sticky='w')
            self.rbs.append(rb)
            
        # create Radio Buttons to choose themes
        themes = {"alt":  "alt - standard", 
            "clam":  "clam - standard", "classic":  "classic - standard",
            "default":  "default - standard"}
            
        self.lF1 = LabelFrame(self.fr1, text='Select Theme', style="RoundedFrame",
                              padding=(10,1,10,10))
        self.lF1.grid(row=2, column=0, sticky='n')
        self.theme_value = StringVar()
        for ix, val in enumerate(themes):
            rb1 = Radiobutton(self.lF1, text=themes[val], value=val, 
                state='disabled', variable=self.theme_value, command=self.theme_command)
            rb1.grid(row=ix, column=0, padx=10, sticky='nw')
            self.rbs1.append(rb1)
            
    def enabled(self, event):
        # from widget selection
        self.lf6.state(["!focus"]) 
        if self.ord.get() == 0:
            if self.widget_value.get() in ('Progressbar', 'Scale', 'Scrollbar'):
                self.lF5.state(["focus"])
                for opt in self.rbs:
                    opt.state(['!disabled'])
                for opt in self.rbs1:
                    opt.state(['disabled'])
            else:
                for opt in self.rbs1:
                    opt.state(['!disabled'])
                self.lF1.state(["focus"])    
                self.lF1['text'] = 'Select Theme'
                self.theme_value.set(None)
        if self.ord.get() == 1:
            self.lf6['text'] = 'Widget'
            if self.widget_value.get() in ('Progressbar', 'Scale', 'Scrollbar'):
                self.lF5.state(["focus"])
                for opt in self.rbs:
                    opt.state(['!disabled'])
                

    def orient_command(self):
        # from orient selection
        self.lF5.state(["!focus"])
        if self.ord.get() == 0:
            try:
                for opt in self.rbs1:
                    opt.state(['!disabled'])
                self.lF1.state(["focus"])
                self.theme_value.set(None)
                self.lF1['text'] = 'Select Theme'
            except (NameError, AttributeError):
                pass
    
    def theme_command(self):
        # from theme selection
        self.s.theme_use(self.theme_value.get())
        self.lF1.state(["!focus"])
        if self.ord.get() == 0:
            self.lF1['text'] = 'Theme'
        if self.ord.get() == 1:
            self.cb.state(['!disabled'])
            self.lF1['text'] = 'Theme'
            self.lf6.state(["focus"])
            
    def selord(self):
        # from select ord
        if self.ord.get() == 0:
            self.lf6.state(["focus"]) 
            self.lF12['text'] = 'Select widget before theme'
            self.theme_value.set(None)
            self.orient.set(None)
            self.cb.set('')
            self.lF1.state(["!focus"])
            self.lF5.state(["!focus"])
        if self.ord.get() == 1:
            self.lF12['text'] = 'Select theme before widget'
            self.cb.state(['disabled'])
            for opt in self.rbs1:
                opt.state(['!disabled'])
            self.lF1.state(["focus"])
            self.theme_value.set(None)
            self.orient.set(None)
            self.cb.set('')
            self.lf6.state(["!focus"])
            self.lF5.state(["!focus"])

app = App()
app.root.mainloop()
