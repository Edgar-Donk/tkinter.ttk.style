'''
lime scrollbar and active unchecked checkbox
- used as template for other button widgets

Create selected state, based on normal state
'''
from roundrect import Gr_Bi_Base_Rect

exp = 9 # enlargement, also thickness between rectangles
w=27 # enlarged from 25
h=27
radius = 6 # gap size was 5
tab = 0
first = '#A3CCC4'
second = '#5D9B90'
third = 'white'
startc = (222,247,222)
stopc = (143,188,143)
fout = '../images/lime/button-sa.png'

Gr_Bi_Base_Rect(fout,w,h,exp,radius,first,second,third,startc,stopc,tab)


