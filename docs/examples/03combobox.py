'''
Changing the colour of a widget using theme_settings,

configure and map are used to set up the widget
'''
from tkinter.ttk import Style, Combobox, Label
from tkinter import Tk
root = Tk()
style = Style()
# this is needed even though we are using 'default' in theme_settings
style.theme_use('default')
style.theme_settings("default", {
   "TCombobox": {          # widget class name
       # note how style.configure and style.map are formatted
       "configure": {"padding": 5},
       "map": {
        # background refers to downarrow
           "background": [("active", "sky blue"),
                          ("!disabled", "cyan")],
                # on first selecting from list the text background is grey,
                # inherited from default theme
                # fieldbackground refers to field
               "fieldbackground": [("!disabled", "green3")],
               "foreground": [("focus", "OliveDrab1"),
                          ("!disabled", "OliveDrab2")],
               "font": ('Gigi 12')
           }
   }
})
l= Label(text='Use the right down arrow to see choice then select')
l.pack(padx=5, pady=5)
combo = Combobox(values=['apple', 'banana', 'orange']).pack(padx=5, pady=5)
root.mainloop()
