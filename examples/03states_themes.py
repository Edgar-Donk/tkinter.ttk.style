"""Ttk Theme Selector and State.

Although it is a theme selector, you won't notice many changes since
there are only radiobuttons, a frame around and the selected widget.

The state selector only applies to the selected widget.

"""
from tkinter import StringVar, Tk
from tkinter.ttk import Frame, Style, Combobox, Button, Radiobutton

class App:
    def __init__(self,root):
        self.fr = Frame(root)
        self.fr.pack(fill='both', expand=1)
        try:  
            import ttkthemes as ts 
            self.style = ts.themed_style.ThemedStyle()
        except (NameError, AttributeError):
            self.style = Style()
        self._setup_widgets()

    def _change_theme(self):
        newtheme = self.theme_val.get()
        self.style.theme_use(newtheme)

    def _change_state(self):
        oldstate = self.but.state()
        if len(oldstate) > 0:
            # convert tuple to string 
            oldst = " ".join(str(x) for x in oldstate) 
            self.but.state(['!'+oldst])
        newstate = self.state_val.get()
        self.but.state([newstate])

    def _setup_widgets(self):
        themes = sorted(list(self.style.theme_names()))
        # Create rasio buttons which will display themes
        self.theme_val = StringVar()
        for ix, val in enumerate(themes):
            themes_rb = Radiobutton(self.fr, value=val, text=val,
                 variable=self.theme_val, command=self._change_theme)
            themes_rb.grid(column=0,row=ix,padx=5,pady=2, sticky='nw')

        

        states = ['active', 'alternate', 'background', 'disabled',
                      'focus', 'invalid', 'pressed', 'readonly', 'selected']
        # Create rasio buttons which will display widget states
        self.state_val = StringVar()
        for iy, state in enumerate(states):
            st_rb = Radiobutton(self.fr, value=state, text=state,
                   variable=self.state_val, command=self._change_state)
            st_rb.grid(column=1,row=iy,padx=5,pady=5, sticky='nw')

        # selected widget, if using scrollbar place in own frame
        self.but = Button(self.fr, text='Button State')
        self.but.grid(column=0,row=ix+1,padx=5,pady=5)

if __name__ == "__main__":
    root = Tk()
    root.title("Ttk Theme and State Selector")
    app = App(root)
    root.mainloop()
