'''
Notebook

Images have extra transparent border as in keramik
'''

from PIL import Image, ImageOps
from roundrect import Gr_Base_Rect
from tools import trans

exp = 9 # enlargement, also thickness between rectangles

w=24 # enlarged from 25
h=32

radius = 4 # gap size was 5

back = 'white' #(102,153,204)
second = '#5D9B90' # (222,247,222)
first = '#A3CCC4' # ~half of border
startc = (222,247,222) 
stopc = (143,188,143) 
fromc = (240,244,239) # used in tab-h and tab-p
toc = (229,255,229) # used in tab-h and tab-p
tab=1
fout = '../images/lime/tab-n.png' 
fout2 = '../images/lime/test2.png' 
fout3 = '../images/lime/test1.png' 
Gr_Base_Rect(fout,w,h,exp,radius,first,second,startc,stopc,tab)

img = Image.open(fout)

eimg = ImageOps.expand(img, border= (0,0,1,0), fill=(0,0,0,0))
eimg.save('../images/lime/tab-n.png') 

dimg = img.convert('L')
dimg = dimg.convert('RGBA')
dimg.save(fout2)
trans(dimg,w,h,radius)
dimg = ImageOps.expand(dimg, border= (0,0,1,0), fill=(0,0,0,0))
dimg.save('../images/lime/tab-d.png')

Gr_Base_Rect(fout3,w,h,exp,radius,first,second,fromc,toc,tab)

pimg = Image.open(fout3)
pimg = ImageOps.expand(pimg, border= (0,0,1,0), fill=(0,0,0,0))
pimg.save('../images/lime/tab-p.png') 

epimg = ImageOps.expand(pimg, border= (0,3,0,0), fill=(0,0,0,0))
ImageOps.crop(epimg,(0,0,0,3)).save('../images/lime/tab-h.png') 

