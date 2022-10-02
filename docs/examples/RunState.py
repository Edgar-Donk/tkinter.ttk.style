from tkinter import Tk, StringVar, IntVar
from tkinter.ttk import Frame, Radiobutton, Button, Checkbutton, Separator

class run_state():
    def __init__(self, fr,widg,widg1=None):
        ''' Used to enable state change

        Creates radio buttons showing states
        Creates check button with "Enabled", useful for testing
            check and radio buttons

        Args:
            fr: frame reference in calling program
            widg: widget reference
            widg1: optional widget
        '''
        self.fr = fr
        self.widg = widg
        self.widg1 = widg1

        # Create radio buttons which will display widget states
        
        states = ['active', 'alternate', 'background', 'disabled', 
                  ('disabled', 'alternate'), 'focus', 'invalid', 'pressed', 
                  'readonly', ('disabled', 'selected'), 'selected']

        self.rb = []
        self.state_val = StringVar()
        for iy, state in enumerate(states):
            st_rb = Radiobutton(fr, value=state, text=state,
                variable=self.state_val, command=self.change_state)
            st_rb.grid(column=0,row=iy+2,padx=5,pady=5, sticky='nw')
            self.rb.append(st_rb)

        sep = Separator(fr, orient='h')
        sep.grid(column=0,row=1,sticky='ew')
        
    def change_state(self):
        ''' used to enable state change'''
        oldstate = self.widg.state()
        # Checkbuttons and Radiobuttons start with alternate state
        if len(oldstate) > 0:
            # prefix oldstate with !
            oldst = [f"!{s}" for s in oldstate]
            # convert tuple to string
            oldst = " ".join(oldst)
            self.widg.state([oldst])
            if self.widg1 is not None:
                self.widg1.state([oldst])
        newstate = self.state_val.get()
        self.widg.state([newstate])
        if self.widg1 is not None:
            self.widg1.state([newstate])

if __name__ == '__main__':
    root = Tk()
    fr1 = Frame()
    fr1.grid(column=0,row=0,sticky='nsew')
    Widg = Button(fr1,text='widg')
    Widg.grid(column=0,row=11)
    Widg1 = Button(fr1,text='widg1')
    Widg1.grid(column=0,row=12)
    run_state(fr1,Widg,Widg1)
    root.mainloop()
