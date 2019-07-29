'''
progressbar alternative

since the widget does not expand, opportunity to use 2d gradient
based on rectangle
'''

from PIL import Image, ImageDraw
from tools import gr_2d_rect, trans, LerpColour

exp = 9 # enlargement, also thickness between rectangles
w=17
h=17
we = w*exp
he = h*exp
radius = 3 # gap size
re=radius*exp
centreX = (w-1)/2
centreY = (h-1)/2
hypotSq = (w-3)*(w-3) + (h-3)*(h-3)

first = '#2D4C46' # '#5D9B90'
second = 'white' #(102,153,204)back

stopc =  (222,247,222) # (143,188,143)
startc = (95,156,142) #(143,188,143)

img = gr_2d_rect(we,he,exp,re,first,second,stopc,startc)

img = img.resize((w,h),Image.LANCZOS)
trans(img,w,h,radius,730)
# used on horizontal
img.save('../images/lime/iprog.png')

rimg = Image.new('RGBA',(w,h),second)
rdraw = ImageDraw.Draw(rimg)

rdraw.rectangle([0,0,w-1,h-1],outline=first)

for y in range(1,h-1):
    rise = centreY - y
    rise *= rise

    for x in range(1,w-1):
        run = centreX - x
        run *= run

        distSq = run + rise
        dist = 4 * distSq / hypotSq

        rdraw.point([x,y],fill=LerpColour(startc,stopc,dist))

rdraw.point([0,0],fill=(0,0,0,0))
rdraw.point([0,h-1],fill=(0,0,0,0))
rdraw.point([w-1,0],fill=(0,0,0,0))
rdraw.point([w-1,h-1],fill=(0,0,0,0))

rimg.save('../images/lime/rprog.png')


