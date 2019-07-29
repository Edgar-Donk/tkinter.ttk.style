'''
scale

slider made with downward pointer, gradient left to right

'''
from PIL import Image, ImageDraw
from tools import LerpColour

def midFunction(a,b):
    # a,b are tuples or lists
    (r1,g1,b1) = a
    (r2,g2,b2) = b
    return ((r1+r2)//2,(g1+g2)//2,(b1+b2)//2)

w=9
h=14
steps = w-2 # gradient steps

back = 'white'
border = '#5D9B90'
fromc = (222,247,222) 
toc = (143,188,143)

afill = midFunction(fromc,toc) 

img = Image.new('RGBA', (w,h), (0,0,0,0))
rdraw = ImageDraw.Draw(img)
rdraw.rectangle([0,0,w-1,h-3],fill=border)
rdraw.polygon([1,h-4,(w-1)//2,h-1,w-2,h-4],outline=border,
              fill =afill)
# gradient
for j in range(steps):
    cr,cg,cb = LerpColour(fromc,toc,j/(steps-1))
    rdraw.line([j+1,1,j+1,h-4],fill=(cr,cg,cb))

# make corners transparent
rdraw.point([0,0],fill=(0,0,0,0))
rdraw.point([w-1,0],fill=(0,0,0,0))
rdraw.point([0,h-3],fill=(0,0,0,0))
rdraw.point([w-1,h-3],fill=(0,0,0,0))

img.save('../images/lime/slider.png')

img.transpose(Image.FLIP_LEFT_RIGHT).save(
    "../images/lime/slider-p.png")

img.transpose(Image.ROTATE_90).save('../images/lime/vslider-p.png')
#rimg = img.rotate(90) # only square rotated
#rimg.save('../images/lime/vslider-p.png')

rimg = Image.open('../images/lime/vslider-p.png')
rimg.transpose(Image.FLIP_TOP_BOTTOM).save(
    "../images/lime/vslider.png")

