'''
combo text area, used as entry before cropping

made separate entry for invalid

'''

from PIL import Image, ImageDraw, ImageOps
from roundrect import Bi_Base_Rect
from tools import trans

exp = 9 # enlargement, also thickness between rectangles
#d = (exp-1)//2 # displacement
w=26
h=25

radius = 5 # gap size
tab=0
second = '#5D9B90' # (222,247,222)
first = '#A3CCC4'  # ~half of border
third = 'white'

dark = '#8b0a50'
light = '#D8137F'

fout = '../images/lime/entry-n.png'
fout2 = '../images/lime/entry-d.png'
fout3 = '../images/lime/entry-i.png'

Bi_Base_Rect(fout,w,h, exp, radius, first, second,third,tab) 

img = Image.open(fout)
ImageOps.crop(img,(0,0,radius-2,0)).save('../images/lime/combo-n.png')

img = Image.open(fout)
dimg = img.convert('L')
dimg = dimg.convert('RGBA')
dimg.save(fout2)
trans(dimg,w,h,radius)
dimg.save(fout2)

ImageOps.crop(dimg,(0,0,radius-2,0)).save('../images/lime/combo-d.png')

Bi_Base_Rect(fout3,w,h, exp, radius, light, dark,third,tab)

#trans(w,h,radius,fout3)


