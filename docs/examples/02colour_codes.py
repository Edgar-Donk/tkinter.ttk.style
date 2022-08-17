from tkinter import Tk, Button, StringVar,Label
from tkinter.ttk import Frame, Entry, LabelFrame
from ast import literal_eval as make_tuple

def contrast(x):
    (r,g,b) = tuple(y/255 for y in x)
    con = 0.299 * r + 0.587 * g + 0.114 * b
    return con

def getit() :
    value=ey.get()
    if value[0] == '(':
        value = make_tuple(value)
        if contrast(value) < 0.5:
            lbl2["foreground"]='white'
        tvalue = value = '#%02x%02x%02x' % value
    elif value[0].isdigit():
        valuei = tuple(int(item) for item in value.split(',') if item.strip())
        tvalue = '#%02x%02x%02x' % valuei
        value = make_tuple(value) # normal tuple(value) --> ('0', ',', '0', ',', '0')
        if contrast(value) < 0.5:
            lbl2["foreground"]='white'
        value = tvalue
    elif value[0].isalpha() :
        value0 = lbl2.winfo_rgb(value)
        rgb = [int(i/65535 * 255) for i in value0]
        rgb = tuple(rgb)
        if contrast(rgb) < 0.5:
            lbl2["foreground"]='white'
        tvalue = value = '#%02x%02x%02x' % rgb
    elif value[0] == '#':
        h = value.lstrip('#')
        tvalue = tuple(int(h[i:i+2], 16) for i in (0, 2 ,4))
        if contrast(tvalue) < 0.5:
            lbl2["foreground"]='white'

    lbl2["text"]=tvalue
    lbl2["background"]=value

root = Tk()
fr = Frame(root)
fr.grid(column=0,row=0)
fr2 = Frame(root)
fr2.grid(column=1,row=0)
lbl = Label(fr,text= 'Enter colour code\n use no quotes\n code can be r,g,b\n \
    hash #rrggbb\n or name')
lbl.grid(column=0,row=0,padx=5,pady=10)

ey = Entry(fr2)
ey.grid(column=0,row=0,padx=5,pady=10)
#out=StringVar(ey.get())

lf=LabelFrame(fr,text='Colour')
lf.grid(column=0,row=1)
lbl2=Label(lf,text='waiting')
lbl2.grid(column=0,row=1)
but1=Button(fr2,text='Make Colour', command=getit)
but1.grid(column=0,row=1, padx=5, pady =5)
root.mainloop( )
