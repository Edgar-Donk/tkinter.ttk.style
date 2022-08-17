import tkinter as tk
import tkinter.ttk as ttk
import ttkthemes as ts

root = tk.Tk()
s = ts.themed_style.ThemedStyle()
s.theme_use('radiance')

ttk.Combobox(root,values='radiance').pack()

root.mainloop()