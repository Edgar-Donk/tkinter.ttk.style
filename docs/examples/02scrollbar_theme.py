'''
Altering a widget with orientation

- look how configure needs the orientation in the style cross reference.
The widget needs to have its orientation in the property orient.

When the Scrollbar is unattached it can only be displayed properly using place
rather than pack or grid layout managers.

The classic theme displays a quirky arrow change when the borderwidth is changed.
'''
from tkinter import Tk, font
from tkinter.ttk import Style, Scrollbar

root = Tk()
style = Style()
style.theme_use('default')
test_size = font.Font(family="Times", size=12, weight="bold").measure('Test')
mult = int(test_size / 30)

style.configure("1st.Horizontal.TScrollbar",
                background="Green", troughcolor="lightblue", bordercolor="red",
                 arrowcolor='yellow', arrowsize=20*mult, borderwidth=5)

style.configure("2nd.Horizontal.TScrollbar",
                background="Green", troughcolor="lightblue", bordercolor="red",
                 arrowcolor='yellow', arrowsize=20*mult)

hs = Scrollbar(root, orient="horizontal", style="1st.Horizontal.TScrollbar")
hs.place(x=5*mult, y=5*mult, width=150*mult)
hs.set(0.2,0.3)

hs2 = Scrollbar(root, orient="horizontal", style="2nd.Horizontal.TScrollbar")
hs2.place(x=5*mult, y=50*mult, width=150*mult)
hs2.set(0.2,0.3)

root.mainloop()
