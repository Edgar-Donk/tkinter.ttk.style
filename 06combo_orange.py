import tkinter as tk
from tkinter import ttk
import orange_theme # when using theme the style is not required

    
values = ['car', 'house', 'computer']
root = tk.Tk()
labels = dict((value, ttk.Label(root, text=value)) for value in values)

try:
    orange_theme.install('orange') 
except Exception:
    import warnings
    warnings.warn("orange theme being used without images")
    
def handler(event):
    current = combobox.current()
    if current != -1:
        for label in labels.values():
            label.config(relief='flat')
        value = values[current]
        print(value)
        label = labels[value]
        label.config(relief='raised')

combobox = ttk.Combobox(root, values=values)
combobox.bind('<<ComboboxSelected>>', handler)
combobox.pack()
for value in labels:
    labels[value].pack()

root.mainloop()
