'''
Spinbox 

Create theme extract for custom widgets, include state selection to view
the result of changing the state using different images and/or different
settings.
Spinbox states disabled, readonly; normal,pressed,active, disabled
'''

from PIL import Image, ImageOps
from tools import trans
from roundrect import Gr_Base_Rect

exp = 9 # enlargement, also thickness between rectangles

w= 15 # (26)arrow base 18
h= 14 # (32) overall height about 23 (58), so half 11 (29) + 3 for cropping

radius = 4 # gap size was 5

back = 'white' #(102,153,204)
second = '#5D9B90' # (222,247,222)
first = '#A3CCC4' # ~half of border
startc = (222,247,222) 
stopc = (143,188,143) 
fromc = (240,244,239) # used in tab-h and tab-p
toc = (229,255,229) # used in tab-h and tab-p
stoph = (216,255,216)
tab=1
fout = '../images/lime/arrspu-n.png' 
fout2 = '../images/lime/arrspu-h.png' 
fout3 = '../images/lime/arrspu-p.png'

Gr_Base_Rect(fout,w,h,exp,radius,first,second,startc,stopc,tab)

img = Image.open(fout)
dimg = img.convert('L')
#img = ImageOps.expand(img, border= (0,3,0,0), fill=(0,0,0,0))
ImageOps.crop(img,(0,0,0,3)).save(fout)
img.transpose(Image.ROTATE_180).save('../images/lime/arrspd-n.png')

img = Image.open(fout)

dimg = dimg.convert('RGBA')
trans(dimg,w,h,radius)

#dimg = ImageOps.expand(dimg, border= (0,3,0,0), fill=(0,0,0,0))
ImageOps.crop(dimg,(0,0,0,3)).save('../images/lime/arrspu-d.png')
dimg.transpose(Image.ROTATE_180).save('../images/lime/arrspd-d.png')

Gr_Base_Rect(fout2,w,h,exp,radius,first,second,fromc,toc,tab)
himg = Image.open(fout2)
himg.transpose(Image.ROTATE_180).save('../images/lime/arrspd-h.png')

Gr_Base_Rect(fout3,w,h,exp,radius,first,second,toc,stoph,tab)
pimg = Image.open(fout3)
pimg.transpose(Image.ROTATE_180).save('../images/lime/arrspd-p.png')

bimg = Image.new('RGBA', (w, h*2), '#FFFFFF00')
bimg.save('../images/lime/spinbut.png')

