"""This demonstrates good part of the syntax accepted by theme_create.

This is a translation of plastik.tcl to python.
You will need the images used by the orange theme to test this. The
images (and other tile themes) can be retreived by doing:

$ cvs -z3 -d:pserver:anonymous@tktable.cvs.sourceforge.net:/cvsroot/tktable \
  co tile-themes

To test this module you should do, for example:

import tkinter
import orange_theme

root = tkinter.Tk()
orange_theme.install(orange_image_dir)
...

Where orange_image_dir contains the path to the images directory used by
the orange theme, something like: '../images/orange'
"""

import os
from glob import glob

from tkinter import PhotoImage
import tkinter.ttk

__all__ = ['install']

colors = {
    "frame": "#efefef",
    "disabledfg": "#aaaaaa",
    "selectbg": "#657a9e",
    "selectfg": "#ffffff"
    }

imgs = {}
def _load_imgs(imgdir):
    imgdir = os.path.expanduser(imgdir) # ('img') ('blue')
    if not os.path.isdir(imgdir):
        raise Exception("%r is not a directory, can't load images" % imgdir)
    for f in glob("%s/*.gif" % imgdir):
        img = os.path.split(f)[1]
        name = img[:-4]
        imgs[name] = PhotoImage(name, file=f, format="gif89")

def install(imgdir):
    _load_imgs(imgdir)
    style = tkinter.ttk.Style()
    style.theme_create("orange", "default", settings={ # "clam"
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

        "Vertical.TScrollbar": {"layout": [
            ("Vertical.Scrollbar.uparrow", {"side": "top", "sticky": ''}),
            ("Vertical.Scrollbar.downarrow", {"side": "bottom", "sticky": ''}),
            ("Vertical.Scrollbar.uparrow", {"side": "bottom", "sticky": ''}),
            ("Vertical.Scrollbar.trough", {"sticky": "ns", "children":
                [("Vertical.Scrollbar.thumb", {"expand": 1, "unit": 1,
                    "children": [("Vertical.Scrollbar.grip", {"sticky": ''})]
                })]
            })]
        },

        "Horizontal.TScrollbar": {"layout": [
            ("Horizontal.Scrollbar.leftarrow", {"side": "left", "sticky": ''}),
            ("Horizontal.Scrollbar.rightarrow",
                {"side": "right", "sticky": ''}),
            ("Horizontal.Scrollbar.leftarrow",
                {"side": "right", "sticky": ''}),
            ("Horizontal.Scrollbar.trough", {"sticky": "ew", "children":
                [("Horizontal.Scrollbar.thumb", {"expand": 1, "unit": 1,
                    "children": [("Horizontal.Scrollbar.grip", {"sticky": ''})]
                })]
            })]
        },

        "TButton": {
            "configure": {"width": 10, "anchor": "center", "padding": [10, 0]},
            "layout": [
                ("Button.focus", {"children":
                    [("Button.button", {"children":
                        [("Button.padding", {"children":
                            [("Button.label", {"side": "left", "expand": 1})]
                        })]
                    })]
                })
            ]
        },

        "Toolbutton": {
            "configure": {"anchor": "center"},
            "layout": [
                ("Toolbutton.border", {"children":
                    [("Toolbutton.button", {"children":
                        [("Toolbutton.padding", {"children":
                            [("Toolbutton.label", {"side":"left", "expand":1})]
                        })]
                    })]
                })
            ]
        },

        "TMenubutton": {"layout": [
            ("Menubutton.button", {"children":
                [("Menubutton.indicator", {"side": "right"}),
                 ("Menubutton.focus", {"children":
                    [("Menubutton.padding", {"children":
                        [("Menubutton.label", {"side": "left", "expand": 1})]
                    })]
                })]
            })]
        },

        "TNotebook": {"configure": {"tabmargins": [0, 2, 0, 0]}},
        "TNotebook.tab": {
            "configure": {"padding": [6, 2, 6, 2], "expand": [0, 0, 2]},
            "map": {"expand": [("selected", [1, 2, 4, 2])]}
        },
      # added map to treeview for selection
        "Treeview": {"configure": {"padding": 0},
         "map": {"background": [("selected", colors["selectbg"])],
            "foreground": [("selected", colors["selectfg"])]}
      },

        # elements
        "Button.button": {"element create":
            ("image", 'button-n',
                ("pressed", 'button-p'), ("active", 'button-h'),
                {"border": [4, 10], "padding": 4, "sticky":"ewns"}
            )
        },

        "Toolbutton.button": {"element create":
            ("image", 'tbutton-n',
                ("selected", 'tbutton-p'), ("pressed", 'tbutton-p'),
                ("active", 'tbutton-h'),
                {"border": [4, 9], "padding": 3, "sticky": "news"}
            )
        },

        "Checkbutton.indicator": {"element create":
            ("image", 'check-nu',
                ('active', 'selected', 'check-hc'),
                ('pressed', 'selected', 'check-pc'),
                ('active', 'check-hu'),
                ("selected", 'check-nc'),
                {"sticky": ''}
            )
        },

        "Radiobutton.indicator": {"element create":
            ("image", 'radio-nu',
                ('active', 'selected', 'radio-hc'),
                ('pressed', 'selected', 'radio-pc'),
                ('active', 'radio-hu'), ('selected', 'radio-nc'),
                {"sticky": ''}
            )
        },

        "Horizontal.Scrollbar.thumb": {"element create":
            ("image", 'hsb-n', {"border": 3, "sticky": "ew"})
        },

        "Horizontal.Scrollbar.grip": {"element create": ("image", 'hsb-g')},
        "Horizontal.Scrollbar.trough": {"element create": ("image", 'hsb-t')},
        "Vertical.Scrollbar.thumb": {"element create":
            ("image", 'vsb-n', {"border": 3, "sticky": "ns"})
        },
        "Vertical.Scrollbar.grip": {"element create": ("image", 'vsb-g')},
        "Vertical.Scrollbar.trough": {"element create": ("image", 'vsb-t')},
        "Scrollbar.uparrow": {"element create":
            ("image", 'arrowup-n', ("pressed", 'arrowup-p'), {"sticky": ''})
        },
        "Scrollbar.downarrow": {"element create":
            ("image", 'arrowdown-n',
            ("pressed", 'arrowdown-p'), {'sticky': ''})
        },
        "Scrollbar.leftarrow": {"element create":
            ("image", 'arrowleft-n',
            ("pressed", 'arrowleft-p'), {'sticky': ''})
        },
        "Scrollbar.rightarrow": {"element create":
            ("image", 'arrowright-n', ("pressed", 'arrowright-p'),
            {'sticky': ''})
        },

        "Horizontal.Scale.slider": {"element create":
            ("image", 'hslider-n', {'sticky': ''})
        },
        "Horizontal.Scale.trough": {"element create":
            ("image", 'hslider-t', {'border': 1, 'padding': 0})
        },
        "Vertical.Scale.slider": {"element create":
            ("image", 'vslider-n', {'sticky': ''})
        },
        "Vertical.Scale.trough": {"element create":
            ("image", 'vslider-t', {'border': 1, 'padding': 0})
        },

        "Entry.field": {"element create":
            ("image", 'entry-n',
                ("focus", 'entry-f'),
                {'border': 2, 'padding': [3, 4], 'sticky': 'news'}
            )
        },

        "Labelframe.border": {"element create":
            ("image", 'border', {'border': 4, 'padding': 4, 'sticky': 'news'})
        },

        "Menubutton.button": {"element create":
            ("image", 'combo-r',
                ('active', 'combo-ra'),
                {'sticky': 'news', 'border': [4, 6, 24, 15],
                 'padding': [4, 4, 5]}
            )
        },
        "Menubutton.indicator": {"element create":
            ("image", 'arrow-d', {"sticky": "e", "border": [15, 0, 0, 0]})
        },

           "TCombobox": {
       "configure": {"selectbackground": "#657a9e"}}, # 'light blue'
       "Combobox.field": {"element create":
           ("image", 'combo-n',
                ('readonly', 'disabled', 'combo-rd'),
                ('readonly', 'pressed', 'combo-rp'),
                ('readonly', 'focus', 'combo-rf'),
                ('readonly',  'combo-rn'),
                {'sticky': 'ew',  'border': [4]}
           )
        },
        "Combobox.downarrow": {"element create":
            ("image", 'comboarrow-n',
                 ('disabled','comboarrow-d'),
                 ('pressed','comboarrow-p'),
                 ('active','comboarrow-a'),
                 {'sticky': '','border': [1]}
             )
   },

        "Notebook.client": {"element create":
            ("image", 'notebook-c', {'border': 4})
        },
        "Notebook.tab": {"element create":
            ("image", 'notebook-tn',
                ("selected", 'notebook-ts'), ("active", 'notebook-ta'),
                {'padding': [0, 2, 0, 0], 'border': [4, 10, 4, 10]}
            )
        },

        "Progressbar.trough": {"element create":
            ("image", 'hprogress-t', {'border': 2})
        },
        "Horizontal.Progressbar.pbar": {"element create":
            ("image", 'hprogress-b', {'border': [2, 9]})
        },
        "Vertical.Progressbar.pbar": {"element create":
            ("image", 'vprogress-b', {'border': [9, 2]})
        },

        "Treeheading.cell": {"element create":
            ("image", 'tree-n',
                ("pressed", 'tree-p'),
                {'border': [4, 10], 'padding': 4, 'sticky': 'news'}
            )
        }

    })
    style.theme_use("orange")
