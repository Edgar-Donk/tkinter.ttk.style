'''
lime scrollbar thumb - used as template for other lime
widgets

First choice gradient start colour too sickly, the gradient
was then reversed.
'''
from PIL import Image
from roundrect import Gr_Base_Rect
from tools import trans

exp = 9 # enlargement, also thickness between rectangles
w=25
h=21
radius = 5 # gap size

second = 'white' #(102,153,204)
first = '#5D9B90'
startc = (222,247,222) #(143,188,143) (26,242,195)
fromci = (212,239,212)
stopc = (143,188,143) #(222,247,222) (225,242,238)
toci = (143,188,143) #(222,247,222) (210,242,234)
fout = '../images/lime/slider-hn.png'
tab = 0

Gr_Base_Rect(fout,w,h,exp,radius,first,second,startc,stopc,tab)


img = Image.open('../images/lime/slider-hn.png')

#rimg = img.rotate(90)
img.transpose(Image.ROTATE_90).save('../images/lime/slider-vn.png')
rimg = Image.open('../images/lime/slider-vn.png')

drimg = rimg.convert('L')
drimg = drimg.convert('RGBA')
trans(drimg,h,w,radius)
drimg.save('../images/lime/slider-vd.png')

#primg = img.rotate(270)
img.transpose(Image.ROTATE_270).save('../images/lime/slider-vp.png')
#primg.Image.open('../images/lime/slider-vp.png')

pimg = img.rotate(180)
pimg.save('../images/lime/slider-hp.png')

dimg = img.convert('L')
dimg = dimg.convert('RGBA')
trans(dimg,w,h,radius)
dimg.save('../images/lime/slider-hd.png')

aimg = img.point(lambda p: int(p * 1.1))
aimg.save('../images/lime/slider-ha.png')

arimg = rimg.point(lambda p: p * int(1.1))

arimg.save('../images/lime/slider-va.png')


