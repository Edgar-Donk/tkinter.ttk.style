import tkinter as tk
import tkinter.ttk as ttk
import orange_theme

root = tk.Tk()

try:
    orange_theme.install('../images/orange')
except Exception:
    import warnings
    warnings.warn("orange theme being used without images")

ttk.Button(root,text='orange').pack()

root.mainloop()