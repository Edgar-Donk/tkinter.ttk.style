from tkinter import Tk, IntVar, font
from tkinter.ttk import Style, Scale, Spinbox, Label, Frame
import numpy as np

class  TtkScale(Scale):
    def __init__(self, parent, length=0, from_=0, to=255, orient='horizontal',
                variable=0, digits=0, tickinterval=None, sliderlength=32,
                 command=None, style=None, showvalue=True, resolution=1):

        self.from_ = from_
        self.to = to
        self.variable = variable
        self.length = length
        self.command = command
        self.parent = parent
        self.orient = orient

        super().__init__(parent, length=length, from_=from_, to=to, orient=orient,
                        variable=variable, command=command, style=style)

        self.digits = digits
        self.tickinterval = tickinterval
        self.showvalue = showvalue
        self.resolution = resolution
        self.sliderlength = sliderlength # = 32

        # set sliderlength
        st = Style(self)
        self.bw_val = bw_val = st.lookup(('Horizontal' if self.orient=='horizontal'
                else 'Vertical') +'.Scale.trough','borderwidth', default=1)

        if showvalue:
            self.configure(command=self.display_value)

        def_font = font.nametofont('TkDefaultFont')
        # if from_ more than to swap values
        if from_ < to:
            pass
        else:
            from_, to = to, from_

        data = np.arange(from_, (to+1 if tickinterval >=1 else to+tickinterval),
                        tickinterval)
        self.data = data = np.round(data,1)
        range_vals = tuple(data)
        len_rvs = len(range_vals)
        if self.orient == 'horizontal':
            vals_size = [def_font.measure(str(i)) for i in range_vals]
            data_size = sum(vals_size)
            space_size = len_rvs * def_font.measure('0')
        else:
            lspace = def_font.metrics('linespace')
            data_size = len_rvs * lspace
            space_size = len_rvs * 3
        sizes = data_size + space_size
        min_len = (sizes if sizes % 50 == 0 else sizes + 50 - sizes % 50)
        self.len_val = len_val = min_len if length < min_len else length
        self.configure(length=len_val)
        #print('sliderlength', sliderlength, 'bw_val', bw_val, 'len_val', len_val)
        self.rel_min = rel_min = (sliderlength / 2 + bw_val) / len_val
        self.rel_max = rel_max = 1 - (sliderlength /2 - bw_val) / len_val
        if range_vals[-1] == to:
            pass
        else:
            max_rv = range_vals[-1]
            self.mult_l = ((max_rv - from_)*rel_max/(to - from_))

        self.bind("<Button-1>", self.resolve)

        self.build(from_, to, rel_min, rel_max, range_vals, len_rvs)

    def build(self, from_, to, rel_min, rel_max, range_vals, len_rvs):
        if self.orient == 'horizontal':
            for i, rv in enumerate(range_vals):
                item = Label(self.parent, text=rv)
                item.place(in_=self, bordermode='outside',
                relx=(rel_min + i / (len_rvs - 1) *
                ((rel_max if range_vals[-1] == to else self.mult_l) - rel_min)) ,
                rely=1, anchor='n')
        else:
            for i, rv in enumerate(range_vals):
                item = Label(self.parent, text=rv)
                item.place(in_=self, bordermode='outside',
                rely=(rel_min + i / (len_rvs - 1) *
                ((rel_max if range_vals[-1] == to else self.mult_l) - rel_min)) ,
                relx=1, anchor='w')

        if self.showvalue:
            self.disp_lab = Label(self.parent, text=self.get())
            rel_l = self.convert_to_rel(float(self.get()))
            if self.orient == 'horizontal':
                self.disp_lab.place(in_=self, bordermode='outside',
                relx=rel_l, rely=0, anchor='s')
            else:
                self.disp_lab.place(in_=self, bordermode='outside',
                rely=rel_l, relx=0, anchor='e')

    def convert_to_rel(self, curr_val):
        return ((curr_val - self.from_) * (self.rel_max - self.rel_min) /
                (self.to - self.from_) + self.rel_min)

    def convert_to_act(self, curr_val):
        l_max = self.rel_max * self.len_val
        l_min = self.rel_min * self.len_val
        return ((curr_val - self.from_) * (l_max - l_min) /
                (self.to - self.from_) + l_min)

    def display_value(self, value):
        # position (in pixel) of the center of the slider
        rel_l = self.convert_to_rel(float(value))
        self.disp_lab.config(text=value) # text=""
        if self.orient == 'horizontal':
            self.disp_lab.place_configure(relx=rel_l)
        else:
            self.disp_lab.place_configure(rely=rel_l)
        digits = self.digits
        self.disp_lab.configure(text=f'{float(value):.{digits}f}')
        # if your python is not 3.6 or above use the following 2 lines
        #   instead of the line above
        #my_precision = '{:.{}f}'.format
        #self.disp_lab.configure(text=my_precision(float(value), digits))

    def resolve(self, evt):
        resolution = self.resolution
        if resolution < 1 or self.tickinterval < 1:
            pass
        else:
            value = self.get()
            curr_l = self.convert_to_act(value)
            if self.orient == 'horizontal':
                if evt.x < curr_l - self.sliderlength / 2:
                    self.set(value - resolution + 1)
                elif evt.x > curr_l + self.sliderlength / 2:
                    self.set(value + resolution - 1)
            else:
                if evt.y < curr_l - self.sliderlength / 2:
                    self.set(value - resolution + 1)
                elif evt.y > curr_l + self.sliderlength / 2:
                    self.set(value + resolution - 1)

if __name__ == "__main__":
    root = Tk()

    len_val = 400
    from_val = 0
    to_val = 255
    tick_val = 10
    dig_val = 2
    res_val = 5
    or_val = 'vertical'

    if or_val =='horizontal':
        style_val = 'my.Horizontal.TScale'
        root.geometry(str(len_val+200)+"x200+500+500")
    else:
        style_val = 'my.Vertical.TScale'
        root.geometry("200x"+str(len_val+200)+"+500+300")

    style = Style()
    style.theme_use('default')
    style.configure(style_val)

    fr = Frame(root)
    fr.pack(fill='y')

    ttks = TtkScale(fr, from_=from_val, to=to_val, orient=or_val,
                    tickinterval=tick_val, digits=dig_val,
                    style=style_val, resolution=res_val)
    if or_val =='horizontal':
        ttks.pack(fill='x', pady=40, padx=5)
    else:
        ttks.pack(fill='y', pady=5, padx=40)

    root.mainloop()
