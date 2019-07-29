'''
lime checkbox

requires checked and unchecked widgets
active unchecked new, otherwise copied from scrollbar slider

'''
from PIL import Image, ImageDraw, ImageOps
from roundrect import Gr_Base_Rect
from tools import trans

exp = 9 # enlargement, also thickness between rectangles
w=17
h=18
radius = 5 # gap size

second = 'white' #(102,153,204)
first = (222,247,222) #'#5D9B90'
third = '#5D9B90'
startc = (222,247,222) #(143,188,143) (26,242,195)

stopc = (143,188,143) #(222,247,222) (225,242,238)
tab=0

light = '#D8137F' #'GreenYellow'
med = '#C11373' #'LawnGreen'
dark = '#8b0a50' #'#5D9B90'

fout = '../images/lime/check-hu.png'
fout2 = '../images/lime/check-nu.png'

Gr_Base_Rect(fout,w,h,exp,radius,first,second,startc,stopc,tab)

img = Image.open('../images/lime/check-hu.png')
dimg = img.convert('L')
img = ImageOps.expand(img, border= (0,0,2,0), fill=(0,0,0,0))
img.save('../images/lime/check-hu.png')


dimg = dimg.convert('RGBA')
trans(dimg,w,h,radius)
dimg = ImageOps.expand(dimg, border= (0,0,2,0), fill=(0,0,0,0))
dimg.save('../images/lime/check-du.png')

idraw = ImageDraw.Draw(img)

def cross(idraw):
    idraw.line([4,3,w-3,h-5],fill=light)
    idraw.line([2,4,w-5,h-4],fill=med)
    idraw.line([2,h-5,w-5,3],fill=light)
    idraw.line([4,h-4,w-3,4],fill=med)
    idraw.line([3,h-4,w-3,3],fill=dark)
    idraw.line([2,3,w-4,h-4],fill=dark)
    idraw.line([3,3,w-3,h-4],fill=dark)
    idraw.line([2,h-4,w-4,3],fill=dark)
    
cross(idraw)

img.save('../images/lime/check-hc.png')

Gr_Base_Rect(fout2,w,h,exp,radius,third,second,startc,stopc,tab)
im = Image.open('../images/lime/check-nu.png')

imu = ImageOps.expand(im, border= (0,0,2,0), fill=(0,0,0,0))
imu.save('../images/lime/check-nu.png')

ndraw = ImageDraw.Draw(im)

cross(ndraw)
dcim = im.convert('L')
im = ImageOps.expand(im, border= (0,0,2,0), fill=(0,0,0,0))
im.save('../images/lime/check-nc.png')


dcim = dcim.convert('RGBA')
trans(dcim,w,h,radius)
dcim = ImageOps.expand(dcim, border= (0,0,2,0), fill=(0,0,0,0))
dcim.save('../images/lime/check-dc.png')


