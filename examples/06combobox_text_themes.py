# https://stackoverflow.com/questions/43086378/how-to-modify-ttk-combobox-fonts
# thanks to CommonSense
'''
Using the widget Text to display the customised colours, their hash representation and to which element 
they have been assigned. The combobox font cannot be easily modified, hence the element_options
used with a CustomBox (modified combobox). The alternative is to use option_add.
'''

from pprint import pformat
from tkinter import Tk, Message, Text
from tkinter.ttk import Style, Combobox, Button, Separator, Frame, Label

def theme_changed(theme):
    style.theme_use(theme)

    lay = style.layout(tWidg)
    ppout = pformat(lay)

    style.configure(
        'Custom.' + tWidg,
        arrowcolor = element_options['arrowcolor'],
            background = element_options['background'], 
            bordercolor = element_options['bordercolor'],
            darkcolor = element_options['darkcolor'],
            fieldbackground = element_options['fieldbackground'],
            foreground = element_options['foreground'],
            focuscolor = element_options['focuscolor'],
            indicatorcolor = element_options['indicatorcolor'],
            itemaccentfill = element_options['itemaccentfill'],
            itemfill = element_options['itemfill'],
            lightcolor = element_options['lightcolor'],
            selectbackground = element_options['selectbackground'],
            selectforeground = element_options['selectforeground'],
            stripebackground = element_options['stripebackground'],
            troughborder = element_options['troughborder'],
            troughcolor = element_options['troughcolor'],
            borderwidth = element_options['borderwidth'],
            selectborderwidth = element_options['selectborderwidth'],
            gripcount = element_options['gripcount'],
            sashthickness = element_options['sashthickness'],
            font = element_options['font']
    )
    return ppout 

element_options = {  
                'arrowcolor': '#FF2222', 'background': '#FFFF00', 
                'bordercolor': '#00FFFF', 'checklight': '#40E0D0', 
                'darkcolor': '#440044', 
                'fieldbackground': '#FFAAAA',
                'foreground': '#884444', 'focuscolor': '#880088',
                'indicatorcolor': '#51FF51', 
                'itemaccentfill': '#ffff77', 'itemfill': '#dddd77',
                'lightcolor': '#FF0000', 
                'selectbackground': '#C1FFC1', 
                'selectforeground': '#FF4400',
                'stripebackground': '#bbbb77',
                'text': '#228822',
                'troughborder': '#226622', 'troughcolor': '#FFCCCC', 
                'borderwidth': 4, 
                'selectborderwidth': 5, 'gripcount': 10,
                'sashthickness': 10, 'font': 'Gigi 12'}

root = Tk()
try:  
    import ttkthemes as ts 
    style = ts.themed_style.ThemedStyle()
except (NameError, AttributeError):
    style = Style()
tWidg = 'TCombobox'


class CustomBox(Combobox):
    def __init__(self, *args, **kwargs):
        #   initialisation of the combobox entry
        super().__init__(*args, **kwargs)
        #   "initialisation" of the combobox popdown
        self._handle_popdown_font()

    def _handle_popdown_font(self):
        """ Handle popdown font
        Note: https://github.com/nomad-software/tcltk/blob/master/dist/library/ttk/combobox.tcl#L270
        """
        #   grab (create a new one or get existing) popdown
        popdown = self.tk.eval('ttk::combobox::PopdownWindow %s' % self)
        #   configure popdown font
        self.tk.call('%s.f.l' % popdown, 'configure', '-font', self['font'])

    def configure(self, cnf=None, **kw):
        """Configure resources of a widget. Overridden!

        The values for resources are specified as keyword
        arguments. To get an overview about
        the allowed keyword arguments call the method keys.
        """

        #   default configure behavior
        self._configure('configure', cnf, kw)
        #   if font was configured - configure font for popdown as well
        if 'font' in kw or 'font' in cnf:
            self._handle_popdown_font()

    #   keep overridden shortcut
    config = configure

tex = Text(root, relief='sunken', width=30, bg='#FFFFBB')
tex.grid(row=0, column=0, sticky='ns', padx=5, pady=5)
step = 0
for key, value in element_options.items():
    st = str(step+1)+'.19'
    st_end = str(step+1)+'.28'
    if str(value)[0] == '#':
        tex.tag_add(('theme'+str(step)), st, st_end) 
        tex.tag_configure(('theme'+str(step)), background=str(value),
				relief= 'raised')
        tex.insert('insert', '{:<16} {} '.format(key,value))
        tex.insert('end','    \n',('theme'+str(step)))
    else:
        if str(key) in ('font'):
            tex.tag_add(('theme'+str(step)), st, st_end) 
            tex.tag_configure(('theme'+str(step)), font=str(value))
            tex.insert('insert', '{:<10} {} '.format(key,value))
            tex.insert('end','Font\n','theme'+str(step))
        else:
            tex.insert('end', '{:<16} {}\n'.format(key,value)) 
    step = step + 1

fra = Frame(root, height=80, width=130)
fra.grid(row=0, column=1, padx=5, pady=5)

combo = Combobox(fra, values=sorted(style.theme_names()), state='readonly')
combo.set(style.theme_use())
combo.bind('<<ComboboxSelected>>', lambda _e: theme_changed(combo.get()))
combo.grid(row=0, column=1, padx=5, pady=5)

out = theme_changed(style.theme_use())

lab1 = Label(fra, text='Choose Theme')
lab1.grid(row=0, column=0, padx=5, pady=5)

sep = Separator(fra, orient='horizontal')
sep.grid(row=1, column=1, padx=5, pady=5, sticky='ew')

combo1 = Combobox(fra, values=("Apple","Orange","Melon"))
combo1.grid(row=2, column=1, padx=5, pady=5)
combo1.set('Apple')

lab2 = Label(fra, text='Normal Widget')
lab2.grid(row=2, column=0, padx=5, pady=5)          

'''
# try uncommenting these lines, and comment out the cb lines following 
combo2 = Combobox(fra, style="Custom." + tWidg, values=("Milk","Water","Juice"))
combo2.grid(row=3, column=0, padx=5, pady=5)
combo2.option_add('*TCombobox*Listbox.font', element_options['font'])
combo2.set('Milk')
# this affects all comboboxes
'''
cb = CustomBox(fra, font=element_options['font'], style="Custom." + tWidg,
                      values=("Milk","Water","Juice"))
cb.grid(row=3, column=1, padx=5, pady=5)
cb.set('Milk')

lab3 = Label(fra, text='Widget with Style')
lab3.grid(row=3, column=0, padx=5, pady=5)
lab4 = Label(fra, text='Widget Layout')
lab4.grid(row=4, column=0, padx=5, pady=5)

mess = Message(fra, text=out, width=250)
mess.grid(row=5, column=0, padx=5, pady=5)

root.mainloop()

