import pprint
from tkinter import Tk,Label
from tkinter.ttk import Label as ttklab

root = Tk()
w = Label(root, text="Hello, world!")
w.pack()
print('TKINTER')
print()
pprint.pprint(w.config()) # this displays all the configuration options of the widget
print()
print('##################################################')
print()
print('TTK')
print()
w2 = ttklab(root, text="Hello, world!")
w2.pack()
pprint.pprint(w2.config())
root.mainloop()
