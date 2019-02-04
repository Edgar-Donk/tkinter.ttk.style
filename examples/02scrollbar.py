'''
Altering a widget with orientation - look how configure needs the orientation in the style
cross reference. The widget needs to have its orientation in the property orient.

When the Scrollbar is unattached it can only be displayed properly using place rather than
pack or grid layout managers. 

The classic theme displays a quirky arrow change when the borderwidth is changed.
'''
from tkinter import Tk
from tkinter.ttk import Style, Scrollbar

root = Tk()
style = Style()
style.theme_use('classic')

style.configure("1st.Horizontal.TScrollbar",
                background="Green", troughcolor="lightblue", bordercolor="blue", 
                 arrowsize=20, borderwidth=5)
                 
style.configure("2nd.Horizontal.TScrollbar",
                background="Green", troughcolor="lightblue", bordercolor="blue", 
                 arrowsize=20)  
                 
hs = Scrollbar(root, orient="horizontal", style="1st.Horizontal.TScrollbar")
hs.place(x=5, y=5, width=150)
hs.set(0.2,0.3)

hs2 = Scrollbar(root, orient="horizontal", style="2nd.Horizontal.TScrollbar")
hs2.place(x=5, y=50, width=150)
hs2.set(0.2,0.3)                

root.mainloop()                 
