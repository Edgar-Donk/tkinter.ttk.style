'''
We wish to create a light blue background, working with Linux all we need is to use Style
then configure fieldbackground - however if we run under Windows or Mac we have to use 
a standard ttk theme, such as clam, then the widget can be easily changed using configure.

The additional steps are shown in the commented lines to change the widget if using Windows
and a standard ttk theme is not used. 

Most ttk widgets set the font when using configure, Entry is an exception in that we set the
font as a property.
'''
from tkinter import Tk
from tkinter.ttk import Style, Entry

root_window = Tk()

estyle = Style()
estyle.theme_use('clam') # if not used then uncomment element_create and layout
# estyle.element_create("plain.field", "from", "clam") # "plain.field" is the cross reference 
# follows the layout of "vista", need layout to enable configure with vista
'''
estyle.layout("EntryStyle.TEntry",
                   [('Entry.plain.field', {'children': [( # using the cross reference
                       'Entry.background', {'children': [(
                           'Entry.padding', {'children': [(
                               'Entry.textarea', {'sticky': 'nswe'})],
                      'sticky': 'nswe'})], 'sticky': 'nswe'})],
                      'border':'2', 'sticky': 'nswe'})])
'''
estyle.configure("EntryStyle.TEntry", # handle for style in Entry
    fieldbackground="light blue" # Set colour here "EntryStyle.TEntry"
    )   # font must be set in entry properties - not here        

entry = Entry(root_window, style="EntryStyle.TEntry", font="Gigi 12")
entry.pack(padx=10, pady=10)

root_window.mainloop()
