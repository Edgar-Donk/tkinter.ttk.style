'''
Creating a colour change whenever state is changed, using style.configure and style.map
'''
from tkinter import Tk
from tkinter.ttk import Style,Button
import random


def change_style():
    color = random.choice(['red', 'blue', 'yellow', 'dark gray', 'purple', 'cyan', 'brown', 'orange'])
    style.configure('Die.TButton', background=color,    # cross reference 'Die.TButton'
                   foreground=['white' if color != 'yellow' else 'black'],
                    highlightthickness='20',
                    font=('Helvetica', 18, 'bold'))
    style.map('Die.TButton', foreground=[("pressed", "red"), ("active", "blue")], # cross reference 'Die.TButton'
                            background=[('active', active_color(color))])


def active_color(color):
    # active_color returns a lighter version of color for the active background
    # using winfo_rgb to get the RGB code for the color.
    c = root.winfo_rgb(color)
    r = c[0] / 65535 * 255
    g = c[1] / 65535 * 255
    b = c[2] / 65535 * 255
    r += (255 - r) / 2
    g += (255 - g) / 2
    b += (255 - b) / 2
    return ("#%2.2x%2.2x%2.2x" % (round(r), round(g), round(b))).upper()


root = Tk()

style = Style(root)
style.theme_use('default')

button = Button(root, text='Test', style='Die.TButton') # cross reference 'Die.TButton'
change_style()
button.pack()

Button(root, command=change_style, text='Change style').pack(padx=4, pady=10)

root.mainloop()
