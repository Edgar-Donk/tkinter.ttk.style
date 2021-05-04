#! /usr/bin/env python
# based on example from py in the eye

from tkinter import Tk, IntVar, StringVar, font
from tkinter.ttk import Frame, Notebook, Separator, Checkbutton, Button, Radiobutton, LabelFrame, Treeview,\
Scrollbar, Combobox, Style, Scale, Progressbar, Sizegrip, Label, Entry, Spinbox
from tkinter.font import Font
import lime_theme

class NotebookDemo:

    def __init__(self, fr):

        self.fr = fr
        self.style = Style() # ts.ThemedStyle() # Style()
        self._create_demo_panel() # run this before allBtns
        self.allBtns = self.ttkbut + self.cbs[1:] + self.rb
        try:
            lime_theme.install('../images/lime')
        except Exception:
            import warnings
            warnings.warn("lime theme being used without images")
        self.style.theme_use('lime')

    def _create_demo_panel(self):
        demoPanel = Frame(self.fr, name="demo")
        demoPanel.pack(side='top', fill='both', expand='y')

        # create the notebook
        self.nb = nb = Notebook(demoPanel, name="nb")
        nb.bind("<<NotebookTabChanged>>", self._on_tab_changed)

        # extend bindings to top level window allowing
        #   CTRL+TAB - cycles thru tabs
        #   SHIFT+CTRL+TAB - previous tab
        #   ALT+K - select tab using mnemonic (K = underlined letter)
        nb.enable_traversal()

        nb.pack(fill='both', expand='y', padx=2, pady=3)
        self._create_descrip_tab(nb)
        self._create_treeview_tab(nb)
        self._create_text_tab(nb)

    def _create_descrip_tab(self, nb):
        # frame to hold contents
        frame = Frame(nb, name='descrip')

        # widgets to be displayed on 'Description' tab
        # position and set resize behaviour

        frame.rowconfigure(1, weight=1)
        frame.columnconfigure((0,1), weight=1, uniform=1)
        lf = LabelFrame(frame, text='Animals')
        lf.pack(pady=5,padx=5,side='left',fill='y')
        themes = ['horse','elephant',
                  'crocodile','bat','grouse with extra\n line made longer']
        self.ttkbut = []
        for t in themes:
            b = Button(lf, text=t)
            b.pack(pady=2)
            self.ttkbut.append(b)

        lF2 = LabelFrame(frame,text="Theme Combobox")
        lF2.pack(anchor='n',pady=5,padx=5)
        themes = list(sorted(self.style.theme_names())) # get_themes # used in ttkthemes
        themes.insert(0, "Pick a theme")
        self.cb = cb = Combobox(lF2, values=themes, state="readonly", height=10)
        cb.set(themes[0])
        #cb.bind('<<ComboboxSelected>>', self.change_style)
        cb.grid(row=0,column=0,sticky='nw', pady=5)

        lF3 = LabelFrame(frame,text="Entry")
        lF3.pack(anchor='n')
        self.en = Entry(lF3)
        self.en.grid(row=0,column=0,sticky='ew', pady=5, padx=5)

        lf1 = LabelFrame(frame, text='Checkbuttons')
        lf1.pack(pady=5,padx=5,side='left',fill='y')

        # control variables
        self.enabled = IntVar()
        self.cheese = IntVar()
        self.tomato = IntVar()
        self.basil = IntVar()
        self.oregano = IntVar()
        # checkbuttons
        self.cbOpt = Checkbutton(lf1, text='Enabled', variable=self.enabled, command=self._toggle_opt)
        cbCheese = Checkbutton(text='Cheese', variable=self.cheese, command=self._show_vars)
        cbTomato = Checkbutton(text='Tomato', variable=self.tomato, command=self._show_vars)
        sep1 = Separator(orient='h')
        cbBasil = Checkbutton(text='Basil', variable=self.basil, command=self._show_vars)
        cbOregano = Checkbutton(text='Oregano', variable=self.oregano, command=self._show_vars)
        sep2 = Separator(orient='h')

        self.cbs = [self.cbOpt, sep1, cbCheese, cbTomato, sep2, cbBasil, cbOregano]
        for opt in self.cbs:
            if opt.winfo_class() == 'TCheckbutton':
                opt.configure(onvalue=1, offvalue=0)
                opt.setvar(opt.cget('variable'), 0)

            opt.pack(in_=lf1, side='top', fill='x', pady=2, padx=5, anchor='nw')

        lf2 = LabelFrame(frame, text='Radiobuttons', labelanchor='n')
        lf2.pack(pady=5,padx=5,side='left',fill='y')

        self.rb=[]
        self.happiness = StringVar()
        for s in ['Great', 'Good', 'OK', 'Poor', 'Awful']:
            b = Radiobutton(lf2, text=s, value=s,
                                variable=self.happiness,
                                command=lambda s=s: self._show_vars())
            b.pack(anchor='nw', side='top', fill='x', pady=5,padx=5)
            self.rb.append(b)

        right = LabelFrame(frame, text='Control Variables')
        right.pack(pady=5,padx=5,side='left',fill='y')

        self.vb0 = Label(right, font=('Courier', 10))
        self.vb1 = Label(right, font=('Courier', 10))
        self.vb2 = Label(right, font=('Courier', 10))
        self.vb3 = Label(right, font=('Courier', 10))
        self.vb4 = Label(right, font=('Courier', 10))
        self.vb5 = Label(right, font=('Courier', 10))

        self.vb0.pack(anchor='nw', pady=5,padx=5)
        self.vb1.pack(anchor='nw', pady=5,padx=5)
        self.vb2.pack(anchor='nw', pady=5,padx=5)
        self.vb3.pack(anchor='nw', pady=5,padx=5)
        self.vb4.pack(anchor='nw', pady=5,padx=5)
        self.vb5.pack(anchor='nw', pady=5,padx=5)

        self._show_vars()
        # add to notebook (underline = index for short-cut character)
        nb.add(frame, text='Description', underline=0, padding=2)



    # =============================================================================
    def _create_treeview_tab(self, nb):
        # Populate the second pane. Note that the content doesn't really matter
        # tree = None
        self.backg = ["white",'#f0f0ff']
        tree_columns = ("country", "capital", "currency")
        tree_data = [
            ("Argentina",      "Buenos Aires",     "ARS"),
            ("Australia",      "Canberra",         "AUD"),
            ("Brazil",         "Brazilia",         "BRL"),
            ("Canada",         "Ottawa",           "CAD"),
            ("China",          "Beijing",          "CNY"),
            ("France",         "Paris",            "EUR"),
            ("Germany",        "Berlin",           "EUR"),
            ("India",          "New Delhi",        "INR"),
            ("Italy",          "Rome",             "EUR"),
            ("Japan",          "Tokyo",            "JPY"),
            ("Mexico",         "Mexico City",      "MXN"),
            ("Russia",         "Moscow",           "RUB"),
            ("South Africa",   "Pretoria",         "ZAR"),
            ("United Kingdom", "London",           "GBP"),
            ("United States",  "Washington, D.C.", "USD")
            ]

        fact = font.Font(font="TkDefaultFont").metrics('linespace')
        self.style.configure('fact.Treeview', rowheight=fact,
                           font=font.nametofont("TkDefaultFont"))
        
        container = Frame(nb)
        container.pack(fill='both', expand=False)
        self.tree = Treeview(container, columns=tree_columns, show="headings",
                             style='fact.Treeview')
        vsb = Scrollbar(container, orient="vertical", command=self.tree.yview)
        hsb = Scrollbar(container, orient="horizontal", command=self.tree.xview)
        self.tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
        self.tree.grid(column=0, row=0, sticky='nsew', in_=container)
        vsb.grid(column=1, row=0, sticky='ns', in_=container)
        hsb.grid(column=0, row=1, sticky='ew', in_=container)

        container.grid_columnconfigure(0, weight=1)
        container.grid_rowconfigure(0, weight=1)

        for col in tree_columns:
            self.tree.heading(col, text=col.title(),
                command=lambda c=col: self.sortby(self.tree, c, 0))
            # XXX tkFont.Font().measure expected args are incorrect according
            #     to the Tk docs
            self.tree.column(col, width=Font().measure(col.title()),stretch=False)

        for ix,item in enumerate(tree_data):
            itemID = self.tree.insert('', 'end', values=item)
            self.tree.item(itemID, tags=itemID)
            self.tree.tag_configure(itemID, background=self.backg[ix%2])

            # adjust columns lengths if necessary
            for indx, val in enumerate(item):
                ilen = Font().measure(val)
                if self.tree.column(tree_columns[indx], width=None) < ilen:
                    self.tree.column(tree_columns[indx], width=ilen)

        sg = Sizegrip(container)
        sg.grid(sticky='e')

        nb.add(container, text='Treeview', underline=0, padding=2)

    # =============================================================================
    def _create_text_tab(self, nb):
        self.dir0 = 1
        self.dir1 = 1
        # populate the third frame with other widgets
        fr = Frame(nb, name='fr1')
        lF = LabelFrame(fr,text="Scale")
        fr3 = Frame(lF)
        fr3.grid(row=0,column=0,sticky='nsew')
        scl = Label(fr3,
            text='Position mouse to cursor ,left mouse click and move\nor use spinbox arrows')

        scl.grid(row=0,column=0,sticky='nw')
        fr1 = Frame(lF)
        fr1.grid(row=1,column=0,sticky='nsew')
        from_=0
        to=100
        value=0
        step=10
        fontSize = 9
        self.scvar = IntVar()

        scRange=self.any_number_range(from_,to,step)
        scLen = len(scRange[1]) * (fontSize + 10)
        print('scLen',scLen)
        self.sc = Scale(fr1, from_=from_, to=to, variable=self.scvar,
                    orient='vertical', length=scLen)
        self.sc.set(value)
        #l1 = Label(fr1,textvariable=self.scvar,width=5)
        l1 = Spinbox(fr1, from_=from_, to=to, textvariable=self.scvar, width=4)
        l1.grid(row=1,column=0,padx=5,pady=5)
        self.sc.grid(row=1,column=1,padx=5,pady=5)
        fr4=Frame(fr1)
        fr4.grid(row=1, column=2)
        sc_split = '\n'.join(scRange[0].split())
        lb = Label(fr1, text=sc_split, font=('Courier New', str(fontSize)),
                   width=4*len(scRange[1]))
        lb.grid(row=1, column=2,padx=5,pady=5)

        sep = Separator(lF, orient="vertical")
        sep.grid(row=1,column=2,sticky='ns')
        fr2 = Frame(lF, name='fr2')
        fr2.grid(row=1,column=3,sticky='nsew')
        self.schvar = IntVar()
        a=0
        b=100
        schRange = self.any_number_range(a,b,s=10)
        schLen = Font().measure(schRange[0])
        print('schLen',schLen)
        self.sch = Scale(fr2, from_=a, to=b, length=schLen, variable=self.schvar,
                         orient='horizontal')

        self.sch.set(0)
        #l2 = Label(fr2,textvariable=self.schvar,width=5)
        l2 = Spinbox(lF, from_=a, to=b, textvariable=self.schvar, width=4)
        l2.grid(row=1,column=3,pady=2)
        self.sch.grid(row=2,column=1,padx=5,pady=5,sticky='nsew')
        l3 = Label(fr2,text=schRange[0], font=('Courier New', str(fontSize)),
                   width=4*len(schRange[1]))
        l3.grid(row=3,column=1,padx=5,pady=5)
        lF.grid(row=0,column=0,sticky='nesw',pady=5,padx=5)

        lF1 = LabelFrame(fr,text="Progress", name = 'lf')
        pb1var = IntVar()
        pb2var = IntVar()
        self.pbar = Progressbar(lF1, variable = pb1var, length = 150,
                                mode ="indeterminate", name='pb1', orient='horizontal')
        self.pb2 = Progressbar(lF1, variable = pb2var, length = 150,
                               mode='indeterminate', name='pb2', orient='vertical')
        self.pbar["value"] = 25

        self.pbar.grid(row=1,column=0,padx=5,pady=5,sticky='nw')
        sep = Separator(lF1, orient="vertical")
        self.pb2.grid(row=1,column=2,padx=5,pady=5,sticky='nw')
        l3 = Label(lF1,textvariable=pb1var)
        l3.grid(row=0,column=0,pady=2,sticky='nw')

        sep.grid(row=0,column=1,rowspan=2,sticky='ns')
        l4 = Label(lF1,textvariable=pb2var)
        l4.grid(row=0,column=2,pady=2,sticky='nw')

        sg1 = Sizegrip(fr)
        sg1.grid(row=2,column=2,sticky='e')

        lF1.grid(row=1,column=0,sticky='nesw',pady=5,padx=5)
        start = Button(lF1, text='Start Progress',
                   command=lambda: self._do_bars('start'))
        stop = Button(lF1, text='Stop Progress',
                   command=lambda: self._do_bars('stop'))
        start.grid(row=2,column=0,padx=5,pady=5,sticky='nw')
        stop.grid(row=3,column=0,padx=5,pady=5,sticky='nw')

        # add to notebook (underline = index for short-cut character)
        nb.add(fr, text='Scale & Others', underline=0)

    #=========================================================================
    def _toggle_opt(self):
        # state of the option buttons controlled
        # by the state of the Option frame label widget
        if self.enabled.get() == 1:
            self.sc.state(['!disabled'])
            self.sch.state(['!disabled'])
            self.cb.state(['!disabled'])
            self.en.state(['!disabled'])
            self.pbar.state(['!disabled'])
            self.pb2.state(['!disabled'])
        else:
            self.sc.state(['disabled'])
            self.sch.state(['disabled'])
            self.cb.state(['disabled'])
            self.en.state(['disabled'])
            self.pbar.state(['disabled'])
            self.pb2.state(['disabled'])

        for opt in self.allBtns:
            #print(opt)
            if opt.winfo_class() != 'TSeparator':
                if self.cbOpt.instate(('selected', )):
                    opt['state'] = '!disabled'  # enable option
                    self.nb.tab(1, state='normal')

                else:
                    opt['state'] = 'disabled'
                    self.nb.tab(1, state='disabled')

        self._show_vars()


    def _show_vars(self):
        # set text for labels in var_panel to include the control
        # variable name and current variable value
        self.vb0['text'] = '{:<11} {:<8}'.format('enabled:', self.enabled.get())
        self.vb1['text'] = '{:<11} {:<8}'.format('cheese:', self.cheese.get())
        self.vb2['text'] = '{:<11} {:<8}'.format('tomato:', self.tomato.get())
        self.vb3['text'] = '{:<11} {:<8}'.format('basil:', self.basil.get())
        self.vb4['text'] = '{:<11} {:<8}'.format('oregano:', self.oregano.get())
        self.vb5['text'] = '{:<11} {:<8}'.format('happiness:', self.happiness.get())

    def sortby(self, tree, col, descending):
        """Sort tree contents when a column is clicked on."""
        # grab values to sort
        data = [(tree.set(child, col), child) for child in tree.get_children('')]

        # reorder data
        data.sort(reverse=descending)
        for indx, item in enumerate(data):
            tree.move(item[1], '', indx)

        # switch the heading so that it will sort in the opposite direction
        tree.heading(col,
            command=lambda col=col: self.sortby(tree, col, int(not descending)))
        # reconfigure tags after ordering
        list_of_items = tree.get_children('')
        for i in range(len(list_of_items)):
            tree.tag_configure(list_of_items[i], background=self.backg[i%2])

    def any_number_range(self,a,b,s=1):
        """ Generate consecutive values list between two numbers with optional step (default=1)."""
        if (a == b):
            return a
        else:
            mx = max(a,b)
            mn = min(a,b)
            result = []
            output = ''
            # inclusive upper limit. If not needed, delete '+1' in the line below
            while(mn < mx + 1):
                # if step is positive we go from min to max
                if s > 0:
                    result.append(mn)
                    mn += s
                # if step is negative we go from max to min
                if s < 0:
                    result.append(mx)
                    mx += s
                # val
            maxLen = 0
            output = ""
            for ix,res in enumerate(result[:-1]): # last value ignored
                if len(str(res)) > maxLen:
                    maxLen = len(str(res))
            if maxLen == 1:
                output = ' '.join(str(i) for i in result) # converts list to string
            else:
                for ix, res in enumerate(result):
                    if maxLen == 2:
                        if len(str(res)) == 1:
                            output = output + str(res) + " " * maxLen
                        elif len(str(res)) == 2:
                            output = output + str(res) + " "
                        else:
                            output = output + str(res)
            # print(a,b,output,result)
            return output,result

    def _do_bars(self, op):
        pbar = self.pbar.nametowidget('.fr.demo.nb.fr1.lf.pb1')
        pb2 = self.pb2.nametowidget('.fr.demo.nb.fr1.lf.pb2')

        if op == 'start':
            pbar.start()
            pb2.start()
        else:
            pbar.stop()
            pb2.stop()

    def _on_tab_changed(self,event):
        event.widget.update_idletasks()
        tab = event.widget.nametowidget(event.widget.select())
        event.widget.configure(height=tab.winfo_reqheight(),width=tab.winfo_reqwidth())

    #========================================================================
if __name__ == '__main__':
    root = Tk()
    #root.geometry("{}x{}+{}+{}".format(w, h, x, y))
    #root.geometry("{}x{}+{}+{}".format(400, 440, 70, 100))
    f = Frame(root,name="fr")
    f.pack(fill='both', expand='y')
    NotebookDemo(f)
    root.mainloop()
