'''
Testing linear gradient with rectangle, ellipse and circle

for balanced ellipse width and height need to be odd
use fill for circle as this reduces number of uncoloured pixels
'''
from PIL import Image, ImageDraw
from math import sqrt

def LerpColour(c1,c2,t):
    return (int(c1[0]+(c2[0]-c1[0])*t),int(c1[1]+(c2[1]-c1[1])*t),
            int(c1[2]+(c2[2]-c1[2])*t))
    #return (int(y) for y in c1 +(c2 - c1)*t)

def circle(draw, center, radius, fill):
    draw.ellipse((center[0] - radius, center[1] - radius,
                center[0] + radius - 1, center[1] + radius - 1),
               fill=fill)

w=21 # width
h=21 # height
e=9  # enlargement
we = w*e
he = h*e
from_colour = (172,161,150)
to_colour = (255,255,255)

img = Image.new(mode='RGB', size=(we,he), color='white')
idraw = ImageDraw.Draw(img)

ul = 0,0
lr = we-1,he-1
steps = (lr[0] if he>we else lr[1])
steps = steps//2+1
# needed to ensure centre is covered
rsq = we*we+he*he

midX = we//2+1
midY = he//2+1
radius = steps #int(sqrt(rsq))

for i in range(steps):
    idraw.rectangle([ul[0]+i, ul[1]+i,lr[0]-i,lr[1]-i],outline=LerpColour(
        to_colour,from_colour,i/(steps-1)))
'''
for i in range(steps):
    idraw.ellipse([ul[0]+i, ul[1]+i,lr[0]-i,lr[1]-i],outline=LerpColour(
        from_colour,to_colour,i/(steps-1)))    

# make highlight more eccentric as divisor is reduced from 9 to 2
for i in range(radius):
    circle(idraw,[midX+i//2,midY+i//2],radius-i,fill=LerpColour(
        from_colour,to_colour,i/(radius-1)))
'''    
#img = img.resize((w,h),Image.LANCZOS)
#img.show()
img.save('test_rect2.png')
         
