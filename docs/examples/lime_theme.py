"""This demonstrates good part of the syntax accepted by theme_create.

This is based on plastik.tcl to python.
You will need the images used by the lime theme to test this. The
images (and other tile themes) can be retreived by doing:

$ cvs -z3 -d:pserver:anonymous@tktable.cvs.sourceforge.net:/cvsroot/tktable \
  co tile-themes

To test this module you should do, for example:

import tkinter
import lime_theme

root = tkinter.Tk()
lime_theme.install(lime_image_dir)
...
Where lime_image_dir contains the path to the images directory used by
the lime theme, something like: tile-themes/images/lime
"""

import os
from glob import glob

from tkinter import PhotoImage
import tkinter.ttk
# import tkinter.font as tkFont

__all__ = ['install']

colours = {
    "frame": '#EFFCF9',#'#2D4C46', "#efefef",
    "disabledfg": "#aaaaaa",
    "selectbg": "#5D9B90",
    "selectfg": "#ffffff",
    'foreground': '#8b0a50',
    'lighter': "#f5f3f0"
    }

imgs = {}
def _load_imgs(imgdir):
    imgdir = os.path.expanduser(imgdir) 
    if not os.path.isdir(imgdir):
        raise Exception("%r is not a directory, can't load images" % imgdir)
    for f in glob("%s/*.png" % imgdir):
        img = os.path.split(f)[1]
        name = img[:-4]
        imgs[name] = PhotoImage(name, file=f, format="png")

def install(imgdir):
    _load_imgs(imgdir)
    style = tkinter.ttk.Style()
    style.theme_create("lime", parent="clam", settings={
        # next line refers to common to all widgets
        ".": {
            "configure":
                {"background": colours['frame'],
                 "troughcolor": colours['frame'],
                 "selectbackground": colours['selectbg'],
                 "selectforeground": colours['selectfg'],
                 "fieldbackground": colours['frame'],
                 "font": "TkDefaultFont", 
                 "foreground": colours['foreground'],
                 "borderwidth": 1},
            "map": {"foreground": [("disabled", colours['disabledfg'])],
                   "background": [("disabled", colours['frame']),
                    ] }
        },

    ## Buttons
     'TButton': {
         'configure': { "anchor": "center",'padding': [10,0]}, # , 'foreground': '#8b0a50'"width": 10
         'layout': [
         ('Button.focus', {'children':
            [('Button.button', {'children':
                [('Button.padding', {'children':
                    [('Button.label', {"side": "left",'expand': 1})]
                })]
            })]
        })]},
        
     # substituted button for slider-hn, hp, ha, hd
     'Button.button': {"element create":
          ('image', "button-n",
           ('pressed', "button-p"),
           ('active', "button-a"),
           ('selected', "button-sa"),
           ('disabled', "button-d"),           
           {'border':[5,12,5,12], 'padding': 4, 'sticky': "nsew"}) #  "ew"
         },

    'Checkbutton.indicator': {"element create":
          ('image', "check-nu",
           ('active', 'selected', "check-hc"),
           ('active', "check-hu"),
           ('disabled', 'selected', "check-dc"),
           ('selected', "check-nc"),
           ('disabled', "check-du"),
           {'width':30, 'sticky': ""}) # 
         },

        'Radiobutton.indicator': {"element create":
          ('image', "radio-n",
           ('disabled','selected', "radio-ds"),
         ('disabled', "radio-d"),
           ('selected', "radio-s"),
           {'width':20, 'sticky': "w"}) 
        },

    ## Entry, Combobox
        'Entry.field': {"element create":
          ('image', "entry-d",
           ('focus', 'entry-n'),
           ('!disabled','invalid', 'entry-i'),
            ('disabled', 'entry-d'),
           {'height': 18,'border':4,'padding':[3,4], 'sticky': 'nsew'})
          },
            
        "Combobox.field": {"element create":
           ("image", 'combo-n',
                ('readonly', 'disabled', 'combo-d'),
                {'sticky': 'ew',  'border': [4]}
           )
        },
            
        "Combobox.downarrow": {"element create":
            ("image", 'arrowdown-n',
                 ('disabled','arrowdown-d'),
                 ('pressed','arrowdown-p'),
                 ('active','arrowdown-a'),
                 {'sticky': '','border': [1]}
             )
        },

    ## Notebook
        'TNotebook': {'configure': {'tabmargins': [0,3,0,0]}},
            'TNotebook.tab': {
            'configure': { 'foreground': '#8b0a50'},
            "map":  
            {'expand': [('selected', [0,3,0,0]),('!selected', [0,0,2])]}}, 
    
         'tab': {"element create":
           ('image', "tab-nx",
           ('active', "tab-hx"),
           ('selected', "tab-px"),
           ('disabled', "tab-dx"),
           {'border':[4, 15, 4, 15], 'padding':[7,3],'height':12} # , 'sticky': "nsew"
        ) },

    ## Labelframes.
        'TLabelframe': {
              'configure': {'borderwidth': 2, 'relief': 'groove'}
                 },
        'TLabelframe.Label': {
                'configure': {'font': "TkDefaultFont"},
                },

     ## Scrollbars.
        "Horizontal.TScrollbar": {"layout": [
            ("Horizontal.Scrollbar.trough", { "children": # "sticky": "ew",
                 [("Horizontal.Scrollbar.leftarrow", {"side": "left"}),
                 ("Horizontal.Scrollbar.rightarrow", {"side": "right"}),
                 ("Horizontal.Scrollbar.thumb", {"side": "left","expand": 1,"sticky": "ew"})]
            })]},
        
     "Horizontal.Scrollbar.thumb": {"element create":
            ("image", 'slider-hn',
             ('disabled', 'slider-hd'),
             ('pressed', 'slider-hp'),
             ('active', 'slider-ha'),
             {"border": 3}) #[9,2] , 'sticky': 'ew', 'padding': [7,2] 
        },

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
            ("Vertical.Scrollbar.trough", {"sticky": "ns", "children":
                 [("Vertical.Scrollbar.uparrow", {"side": "top"}),
                 ("Vertical.Scrollbar.downarrow", {"side": "bottom"}),
                 ("Vertical.Scrollbar.thumb", {"side": "top","expand": 1,"sticky": "ns"})]
            })]},
        
     "Vertical.Scrollbar.thumb": {"element create":
            ("image", 'slider-vn',
             ('disabled', 'slider-vd'),
             ('pressed', 'slider-vp'),
             ('active', 'slider-va'),
             {"border": [2,9]})
        },

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
        
    'TCombobox': {
        'configure': {'selectborderwidth': 1, 'padding': 2,
                      'insertwidth': 2, 'font': 'TkTextFont'}
            },

    ## Scales.
      'Horizontal.Scale.trough': {"element create":
          ('image', "scale-nt",
           ('disabled', "scale-dt"),
            {'border':[6,0,6,0],'sticky': 'wes'})},
     'Horizontal.Scale.slider': {"element create":
          ('image', "slider", 
           ('pressed','!disabled', "slider-p"),
           {'border':3})
        },
     'Vertical.Scale.trough': {"element create":
          ('image', "vslider-t",
           {'border':[0,6,0,6],'sticky': 'nes'})},
     'Vertical.Scale.slider': {"element create":
          ('image', "vslider", 
           ('pressed','!disabled', "vslider-p"),
           {'border':3})
        },

    ## Progressbar.
        'Horizontal.Progressbar.trough': {"element create":
          ('image', "slider-ha",
           {'border':[9,2]})},
     'Horizontal.Progressbar.pbar': {"element create":
          ('image', "rprog", 
           {'border':4})
        },
     'Vertical.Progressbar.trough': {"element create":
          ('image', "slider-va",
           {'border':[2,9]})},
     'Vertical.Progressbar.pbar': {"element create":
          ('image', "iprog", 
           {'border':4})
        },

      ## Spinbox - added for Python 3.7+
         "Spinbox.field": {"element create":
           ("image", 'combo-n',
                ('readonly', 'disabled', 'combo-d'),
                {'sticky': 'nsew',  'border': [4],'padding': 0} # 'padding': 0
           )
        },
        "Spinbox.downarrow": {"element create":
            ("image", 'arrspd-n',
                 ('disabled','arrspd-d'),
                 ('pressed','arrspd-p'),
                 ('active','arrspd-h'),
                 {'sticky': 'e','border': [0],'padding': 4} # 'border': [1]
             )
        },
     "Spinbox.uparrow": {"element create":
            ("image", 'arrspu-n',
                 ('disabled','arrspu-d'),
                 ('pressed','arrspu-p'),
                 ('active','arrspu-h'),
                 {'sticky': 'e','border': [0],'padding': 4}
             )
        },
         
    ## Treeview
        'Treeheading.cell': {"element create":
          ('image', "slider-hn",
           ('pressed', "slider-hp"),
           ('active', "slider-ha"),
           ('selected', "slider-ha"),
           ('disabled', "slider-hd"),
           {'border':[4,12,4,12], 'padding':4, 'sticky': "nsew"} 
        ) },
         'Treeview': {'map':{'background':[('selected', colours['selectbg'])],
                      'foreground': [('selected',colours['selectfg'])]}}
        
    })



   
