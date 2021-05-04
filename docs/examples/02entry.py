'''
Entry may cause problems with the OS

We wish to create a light blue background, working with Linux all we need is to
use Style then configure fieldbackground - however if we run under Windows or
Mac we have to use a standard ttk theme, such as clam, then the widget can be
easily changed using configure.

The additional steps are shown in the commented lines to change the widget if
using Windows and a standard ttk theme is not used.

Most ttk widgets set the font when using configure, Entry is an exception in
that we set the font as a property.
'''
from tkinter import Tk, font
from tkinter.ttk import Style, Entry, Label

root_window = Tk()
root_window.geometry("100x100+600+500")
estyle = Style()
estyle.theme_use('clam') # if not used then uncomment element_create and layout
# estyle.element_create("plain.field", "from", "clam") # "plain.field" is the
# cross reference follows the layout of "vista", need layout to enable
# configure with vista
#test_size = font.Font(family="Times", size=12, weight="bold").measure('Test')
#mult = int(test_size / 30)
fact = font.Font(font="Gigi 12").metrics('linespace')
#print(fact)
'''
estyle.layout("EntryStyle.TEntry",
# using the cross reference
                   [('Entry.plain.field', {'children': [(
                       'Entry.background', {'children': [(
                           'Entry.padding', {'children': [(
                               'Entry.textarea', {'sticky': 'nswe'})],
                      'sticky': 'nswe'})], 'sticky': 'nswe'})],
                      'border':'2', 'sticky': 'nswe'})])
'''
estyle.configure("EntryStyle.TEntry", # handle for style in Entry
    fieldbackground="light blue", # Set colour here "EntryStyle.TEntry"
    height=fact)   # font must be set in entry properties - not here
lab = Label(root_window, text = 'Enter a comment in the entry below')
lab.pack(padx=10, pady=10)
entry = Entry(root_window, style="EntryStyle.TEntry", font="Gigi 12")
entry.pack(padx=10, pady=10)

root_window.mainloop()
