'''
scale trough

standard widget method
'''
from PIL import Image, ImageDraw
from roundrect import Gr_Base_Rect

exp = 9 # enlargement, also thickness between rectangles
w=16
h=10
radius = 5 # gap size

second = 'white' #(102,153,204)back
first = '#5D9B90' # (222,247,222)border
startc = (222,247,222) #(143,188,143) (26,242,195)
fromci = (183,217,183) # (212,239,212)
stopc = (143,188,143) #(222,247,222) (225,242,238)
toci = (143,188,143) #(222,247,222) (210,242,234)
fout = '../images/lime/slider-t.png'
tab = 0

Gr_Base_Rect(fout,w,h,exp,radius,first,second,startc,stopc,tab)

img = Image.open('../images/lime/slider-t.png')
img.transpose(Image.ROTATE_90).save('../images/lime/vslider-t.png')
