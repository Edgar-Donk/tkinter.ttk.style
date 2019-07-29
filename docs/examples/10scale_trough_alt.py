'''
scale trough

based on keramik trough
horizontal trough open at top, border has gradient

'''
from PIL import Image, ImageDraw, ImageChops
from tools import LerpColour, gr_base, trans

exp = 9 # enlargement, also thickness between rectangles
w=16
h=10
we = w*exp
he = h*exp
radius = 5 # gap size
re=radius*exp
steps = he

first = '#2B2B2B' # '#5D9B90'
second = 'white' #(102,153,204)back
startci = (236,247,222) 
stopci = (148,229,50) 
startc = (240,252,240)
stopc = (87,137,87)

img = gr_base(we,he,exp,re,first,second,startci,stopci)
# img.save('../images/lime/iscale-n.png')

grad = Image.new('RGBA', (we,he), 'white')
igrad = ImageDraw.Draw(grad)

# gradient
for j in range(steps):
    cr,cg,cb = LerpColour(startc,stopc,j/(steps-1))
    igrad.line([0,j,we-1,j],fill=(cr,cg,cb))

limg = ImageChops.lighter(grad,img)
limg = limg.resize((w,h),Image.LANCZOS)
trans(limg,w,h,radius)
limg.save('../images/lime/scale-nt.png')

dimg = limg.convert('L')
dimg = dimg.convert('RGBA')
trans(dimg,w,h,radius)
dimg.save('../images/lime/scale-dt.png')

#img = Image.open('../images/lime/slider-t.png')
#img.transpose(Image.ROTATE_90).save('../images/lime/vslider-t.png')
