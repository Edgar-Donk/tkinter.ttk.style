'''
button alternative

based on keramik button
open at top, border has gradient
make certain inner and outer gradients contrast
use ImageChops.lighter to combine gradients, then
can resize giving good antialias, so require function
gr_base

'''
from PIL import Image, ImageDraw, ImageChops
#from roundrect import Gr_Base_Rect
from tools import LerpColour, gr_base, trans

exp = 9 # enlargement, also thickness between rectangles
w=25
h=25
we = w*exp
he = h*exp
radius = 5 # gap size
re=radius*exp
steps = he

second = 'white' #(102,153,204)back
first = '#2B2B2B' #'#5D9B90' # (222,247,222)border
startci = (236,247,222) # (227,247,227) (143,188,143) (26,242,195)
stopci = (148,229,50) #(143,188,143) (222,247,222) (225,242,238)
startc = (240,252,240)
stopc = (87,137,87) #(222,247,222) (210,242,234)

img = gr_base(we,he,exp,re,first,second,startci,stopci)
#img.save('../images/lime/ibutton-n.png')

grad = Image.new('RGBA', (we,he), 'white')
igrad = ImageDraw.Draw(grad)


# gradient
for j in range(steps):
    cr,cg,cb = LerpColour(startc,stopc,j/(steps-1))
    igrad.line([0,j,we-1,j],fill=(cr,cg,cb))
    
#grad.save('../images/lime/grad.png') 

limg = ImageChops.lighter(grad,img)
limg = limg.resize((w,h),Image.LANCZOS)
trans(limg,w,h,radius)
limg.save('../images/lime/button-n.png') 

pimg = limg.rotate(180)
pimg.save('../images/lime/button-p.png')

aimg = limg.point(lambda p: p * 1.1)
aimg.save('../images/lime/button-a.png')

dimg = limg.convert('L')
dimg = dimg.convert('RGBA')
trans(dimg,w,h,radius)
dimg.save('../images/lime/button-d.png')
