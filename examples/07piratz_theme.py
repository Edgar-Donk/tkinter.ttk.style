"""This demonstrates good part of the syntax accepted by theme_create.

This is a translation of plastik.tcl to python.
You will need the images used by the plastik theme to test this. The
images (and other tile themes) can be retreived by doing:

$ cvs -z3 -d:pserver:anonymous@tktable.cvs.sourceforge.net:/cvsroot/tktable \
  co tile-themes

To test this module you should do, for example:

import tkinter
import piratz_theme

root = tkinter.Tk()
piratze_theme.install(piratz_image_dir)
...

Where piratz_image_dir contains the path to the images directory used by
the piratz theme, something like: tile-themes/piratz/piratz
"""

import os
from glob import glob

from tkinter import PhotoImage
import tkinter.ttk

__all__ = ['install']

colors = {
    "frame": "#6699cc",
    "disabledfg": "#aaaaaa",
    "selectbg": "#2d2d66",
    "selectfg": "#ffffff",
    "window": "#e6f3ff",
    "lighter": "#bcd2e8"
    }

imgs = {}
def _load_imgs(imgdir):
    imgdir = os.path.expanduser(imgdir) #(imgdir) ('img') ('blue')
    if not os.path.isdir(imgdir):
        raise Exception("%r is not a directory, can't load images" % imgdir)
    for f in glob("%s/*.gif" % imgdir):
        img = os.path.split(f)[1]
        name = img[:-4]
        imgs[name] = PhotoImage(name, file=f, format="gif89")

def install(imgdir):
    _load_imgs(imgdir)
    style = tkinter.ttk.Style()
    # style.theme_create("orange", "default", settings={
    style.theme_create("piratz", "clam", settings={
	# next line refers to common to all widgets
        ".": {
            "configure":
                {"background": colors['frame'],
                 "troughcolor": colors['frame'],
                 "selectbackground": colors['selectbg'],
                 "selectforeground": colors['selectfg'],
                 "fieldbackground": colors['frame'],
                 "font": "TkDefaultFont",
                 "borderwidth": 1},
            "map": {"foreground": [("disabled", colors['disabledfg'])]}
        },
        # Label
        'Label.border': {"element create":
          ('image', "label",
           ('disabled', "label-d"),
           {'border':[19, 9, 7, 7], 'padding':[19,3,3,3], 'sticky': "nsew"}) 
        },
        
