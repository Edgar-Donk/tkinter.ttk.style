'''
LabelFrame is split,

we have to have two separate configure clauses to be able to alter
the colours of the Label (anciliary part) and the Frame (main part). The first 
2 LabelFrames are displayed one with a label colour change  the other with a 
frame colour change. The third LabelFrame changes both parts.
'''
from tkinter import Frame,Tk, font
from tkinter.ttk import LabelFrame,Style

root = Tk()
test_size = font.Font(family="Times", size=12, weight="bold").measure('Test')
mult = int(test_size / 30)
s = Style()
# change label colour here, we could program different colours to suit the 
# application requirements
ch = 'lightgreen' 
# altering label - anciliary part  
s.configure(ch +'.TLabelframe.Label', background=ch)  
# altering main part
s.configure('pink.TLabelframe', background='pink') 
# altering both parts   
s.configure('both.TLabelframe',background='#40E0D0')  
# altering both parts            
s.configure('both.TLabelframe.Label',background='light blue') 

# LabelFrame with altered anciliary part
# do not use ch+".TLabelframe.Label"
lf = LabelFrame(root, text = "Label", style = ch+".TLabelframe") 
lf.pack( anchor = "w", ipadx = 10*mult, ipady = 5*mult, padx = 10*mult,
                  pady = 0, side = "top")
Frame(lf, width=100*mult, height=100*mult, bg='yellow').pack()

# LabelFrame with altered main part
lf1 = LabelFrame(root, text = "Frame", style = "pink.TLabelframe") 
lf1.pack( anchor = "w", ipadx = 10*mult, ipady = 5*mult, padx = 10*mult,
                  pady = 5*mult, side = "top")
Frame(lf1, width=100*mult, height=100*mult, bg='yellow').pack()

# LabelFrame with both parts altered
lf2 = LabelFrame(root, text = "Both", style = "both.TLabelframe") 
lf2.pack( anchor = "w", ipadx = 10*mult, ipady = 5*mult, padx = 10*mult,
                  pady = 0, side = "top")
Frame(lf2, width=100*mult, height=100*mult, bg='yellow').pack()
root.mainloop()
