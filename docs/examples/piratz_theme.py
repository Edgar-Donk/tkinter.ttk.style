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

from tkinter import PhotoImage #, Tk
import tkinter.ttk
# import tkinter.font as tkFont

__all__ = ['install']

colors = {
    "frame": "#6699cc",
    "disabledfg": "#aaaaaa",
    "selectbg": "#2d2d66",
    "selectfg": "#ffffff",
    'bordercolor': '#7FFFD4'
    }

#root = Tk()
# AttributeError: 'NoneType' object has no attribute 'call'
# can only work after Tk call
#pirate_font = tkFont.Font(family="Backstroke Brush Script MT", size=14) #Palace Script MT Backstroke Brush Script MT

imgs = {}
def _load_imgs(imgdir):
    imgdir = os.path.expanduser(imgdir) #(imgdir) ('img') ('blue')
    #print(imgdir)
    if not os.path.isdir(imgdir):
        raise Exception("%r is not a directory, can't load images" % imgdir)
    for f in glob("%s/*.png" % imgdir):
        img = os.path.split(f)[1]
        name = img[:-4]
        imgs[name] = PhotoImage(name, file=f, format="png")
        #print(imgs[name])

def install(imgdir):
    _load_imgs(imgdir)
    style = tkinter.ttk.Style()
    style.theme_create("piratz", parent="clam", settings={
        # next line refers to common to all widgets
        ".": {
            "configure":
                {"background": colors['frame'],
                 "troughcolor": colors['frame'],
                 "selectbackground": colors['selectbg'],
                 "selectforeground": colors['selectfg'],
                 "fieldbackground": colors['frame'],
                 "font": "TkDefaultFont", # pirate_font, #
                 "borderwidth": 1},
            "map": {"foreground": [("disabled", colors['disabledfg'])]}
        },

        # Label
        'Label.border': {"element create":
          ('image', "label",
           ('disabled', "label-d"),
           {'border':[19, 9, 7, 7], 'padding':[17,5,3,3], 'sticky': "nsew"})
        },

        # LabelFrame
        'Labelframe.border': {"element create":
          ('image', "frame",
           ('disabled', "frame-d"),
           {'border':5, 'sticky': "nsew"}) # 'padding':5,
        },

        # Entry
        'Entry.field': {"element create":
          ('image', "entry-n",
           ('focus', 'entry-f'),
            ('disabled', 'entry-d'),
           {'height': 18,'border':[10,10],'padding':[3,4], 'sticky': 'nsew'})
        },

        # Separator
        'Horizontal.TSeparator': {'layout': [
            ('Horizontal.Separator.separator',{"sticky": "ew"},
        )]},

        'Vertical.TSeparator': {'layout': [
            ('Vertical.Separator.separator',{"sticky": "ns"},
        )]},

        'Horizontal.Separator.separator': {"element create":
            ('image', "separator",
            {'border':[3],'sticky': 'ew'})},

        'Vertical.Separator.separator': {"element create":
            ('image', "separator-v",
            {'border':[3],'sticky': 'ns'})},

        # Sizegrip
        'sizegrip': {"element create":
          ('image', "sizegrip")},

        # Combobox
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

        # Scrollbar
        "Horizontal.TScrollbar": {"layout": [
            ("Horizontal.Scrollbar.leftarrow", {"side": "left", "sticky": ''}),
            ("Horizontal.Scrollbar.rightarrow",
                {"side": "right", "sticky": ''}),
            #("Horizontal.Scrollbar.leftarrow",
                #{"side": "right", "sticky": ''}),
            ("Horizontal.Scrollbar.trough", {"sticky": "ew", "children":
                [("Horizontal.Scrollbar.thumb", {"expand": 1, "unit": 1,
                    "children": [("Horizontal.Scrollbar.grip", {"sticky": ''})]
                })]
            })]},

        "Horizontal.Scrollbar.thumb": {"element create":
            ("image", 'hthumb-n',
             ('disabled', 'hthumb-d'),
             ('pressed', 'hthumb-a'),
             ('active', 'hthumb-a'),
             {"border": [9,2]}) #3 , 'sticky': 'ew', 'padding': [7,2]
        },

        "Horizontal.Scrollbar.grip": {"element create": ("image", 'hgrip')},

        "Horizontal.Scrollbar.trough": {"element create":
            ('image', 'trough-horiz',
             {"border": 2, 'width': 32, 'height':21})}, # , 'sticky': 'ew'

        'Scrollbar.leftarrow': {"element create":
            ("image", 'arrowleft-n',
             ('disabled', 'arrowleft-d'),
             ('pressed', 'arrowleft-p'),
             ('active', 'arrowleft-a'),
             {"border": 1})
            },

        'Scrollbar.rightarrow': {"element create":
            ("image", 'arrowright-n',
             ('disabled', 'arrowright-d'),
             ('pressed', 'arrowright-p'),
             ('active', 'arrowright-a'),
             {"border": 1})
            },

        "Vertical.TScrollbar": {"layout": [
            ("Vertical.Scrollbar.uparrow", {"side": "top", "sticky": ''}),
            ("Vertical.Scrollbar.downarrow", {"side": "bottom", "sticky": ''}),
            #("Vertical.Scrollbar.uparrow", {"side": "bottom", "sticky": ''}),
            ("Vertical.Scrollbar.trough", {"sticky": "ns", "children":
                [("Vertical.Scrollbar.thumb", {"expand": 1, "unit": 1,
                    "children": [("Vertical.Scrollbar.grip", {"sticky": ''})]
                })]
            })]}, # "side": "top",

        "Vertical.Scrollbar.thumb": {"element create":
            ("image", 'vthumb-n',
             ('disabled', 'vthumb-d'),
             ('pressed', 'vthumb-a'),
             ('active', 'vthumb-a'),
             {"border": [2,9]})
        },

        "Vertical.Scrollbar.grip": {"element create": ("image", 'vgrip')},

        "Vertical.Scrollbar.trough": {"element create":
            ('image', 'trough-vert',
             {"border": 2, 'width': 21, 'height':32})},

        'Scrollbar.uparrow': {"element create":
            ("image", 'arrowup-n',
             ('disabled', 'arrowup-d'),
             ('pressed', 'arrowup-p'),
             ('active', 'arrowup-a'),
             {"border": 1})
            },

        'Scrollbar.downarrow': {"element create":
            ("image", 'arrowdown-n',
             ('disabled', 'arrowdown-d'),
             ('pressed', 'arrowdown-p'),
             ('active', 'arrowdown-a'),
             {"border": 1})
        },

        # Radiobutton
        'Radiobutton.indicator': {"element create":
          ('image', "radio",
          ('active', "radio-a"),
           ('selected', "radio-s"),
           ('disabled', "radio-d"),
           {'width':20, 'sticky': "w"})
        },

        # Checkbutton
        'Checkbutton.indicator': {"element create":
          ('image', "check-nu",
           ('pressed', 'selected', "check-nc"),
           ('pressed', "check-nu"),
           ('active', 'selected', "check-nc"),
           ('active', "check-nu"),
           ('selected', "check-nc"),
           ('disabled', "check-du"),
           ('disabled', 'selected', "check-dc"),
           {'width':24, 'sticky': "w"})
         },

        # Notebook
        'TNotebook': {'configure': {'bordercolor': colors['bordercolor'],
                                    'tabmargins':[6,6,6,6]}
       },
        'TNotebook.tab': {"map":
        {'expand': [('selected', [6,6,6,6])]}},

        'tab': {"element create":
          ('image', "sail",
           ('pressed', "sail-p"),
           ('selected', "sail-s"),
           ('disabled', "sail-d"),
           {'border':[30, 17, 27, 32], 'padding':[13,8,12,13], 'sticky': "nsew"}
        ) },

       # Treeview
       'Treeheading.cell': {"element create":
          ('image', "sail",
           ('selected', "sail-s"),
           ('disabled', "sail-d"),
           ('pressed', "sail-s"),
           ('active', "sail-p"),
           {'border':[30, 17, 27, 32], 'padding':[13,8,18,21], 'sticky': "nsew"}
        ) },
       # added map to treeview for selection
       'Treeview': {'configure': {'bordercolor': colors['bordercolor']},
          "map": {"background": [("selected", colors["selectbg"])],
            "foreground": [("selected", colors["selectfg"])]}
       },

       # Button
       'TButton': {
         'configure': {'anchor': 'center', 'font': 'font'},
         'layout': [
         ('Button.focus', {'children':
            [('Button.button', {'children':
                [('Button.padding', {'children':
                    [('Button.label', {'expand': 0})]
                })]
            })]
        })]},

       'Button.button': {"element create":
          ('image', "button",
           ('pressed', "button-p"),
           ('selected', "button-s"),
           ('active', "button-s"),
           ('disabled', "button-d"),
           {'border':[52,65,47,17], 'padding':[12,54,8,16], 'sticky': "nsew"})
       },

       # Progressbar
       'Horizontal.Progressbar.trough': {"element create":
          ('image', "trough-pbar-horiz",
           {'border':4})},

       'Horizontal.Progressbar.pbar': {"element create":
          ('image', "pbar-boat-a",
           ('background', '!active', "pbar-boat-b"),
           {'border':[2, 9]})
        },

       'Vertical.Progressbar.trough': {"element create":
          ('image', "trough-pbar-vert",
           {'border':3})},

       'Vertical.Progressbar.pbar': {"element create":
          ('image', "pbar-gull-a",
           ('background', '!active', '!invalid', "pbar-gull-b"),
           ('invalid', '!active', '!background', "pbar-gull-b"),
           {'border':[9, 2]})
        },

        # Scale
        'Horizontal.Scale.trough': {"element create":
          ('image', "trough-tabletop",
           ('background', 'trough-beach'),
           ('focus', 'trough-beach'),
           ('invalid', 'trough-beach'),
           ('readonly', 'trough-sea'),
           ('selected', 'trough-sea')
           )},

        'Horizontal.Scale.slider': {"element create":
          ('image', "slider-horiz-map",
           ('background', "slider-horiz-c-chest"),
           ('invalid', "slider-horiz-o-chest"),
           ('focus', 'slider-horiz-ben'),
           ('readonly', 'slider-horiz-wheel'),
           ('selected', 'slider-horiz-wheelp'),
           {'border':3})
        },

        'Vertical.Scale.trough': {"element create":
          ('image', "trough-scale-vert",
           )},

        'Vertical.Scale.slider': {"element create":
          ('image', "slider-s-vert",
           ('background', "slider-s-vert-b"),
           ('invalid', "slider-s-vert-i"),
           ('selected', 'slider-s-vert-s'),
           {'border':3})
        }
        })

    style.theme_use("piratz")
