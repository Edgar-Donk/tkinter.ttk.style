'''
Changing the colour of a widget using theme_settings, configure and map are used to set up the widget
'''
from tkinter.ttk import Style, Combobox
from tkinter import Tk
root = Tk()
style = Style()
style.theme_use('default') # this is needed even though we are using 'default' in theme_settings
style.theme_settings("default", {
   "TCombobox": {          # widget class name
       "configure": {"padding": 5}, # note how style.configure and style.map are formatted
       "map": {
           "background": [("active", "green2"), # background refers to downarrow
                          ("!disabled", "green4")],
               # on first selecting from list the text background is grey, inherited from default theme
               "fieldbackground": [("!disabled", "green3")], # fieldbackground refers to field
               "foreground": [("focus", "OliveDrab1"),
                          ("!disabled", "OliveDrab2")]
           }
   }
})
combo = Combobox(values=['apple', 'banana', 'orange']).pack()
root.mainloop()
