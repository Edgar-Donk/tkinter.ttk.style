'''
draw an ellipse containing out target rectangle

circle radius is √2 times larger to enclose square,
assume that the ellipse will be similar using semi-axes
'''
from PIL import Image, ImageDraw
from math import ceil, sqrt

def LerpColour(c1,c2,t):
    return (int(c1[0]+(c2[0]-c1[0])*t),int(c1[1]+(c2[1]-c1[1])*t),
            int(c1[2]+(c2[2]-c1[2])*t))

def circle(draw, center, radius, fill):
    draw.ellipse((center[0] - radius, center[1] - radius,
                center[0] + radius - 1, center[1] + radius - 1),
               fill=fill)
    
we = 60
he = 34
size = (he if he>we else we)
# centre
cx = we//2
cy = he//2
cs = size//2, size//2
# target rectangle
border = 3 
wi = we-(border-1)*2 # we-4 want 56,30
hi = he-(border-1)*2 # he-4
si = size - (border-1)*2, size - (border-1)*2
ul = border,border # corner
lr = wi,hi # corner
lrs = si
# semi-axes
a = cx-ul[0]
b = cy-ul[1]
 
# outside dimension
semi_rad = sqrt(a*a+b*b)
dimo = round(semi_rad * sqrt(2))
rad = sqrt(si[0]*si[0])
dimso = round(rad * sqrt(2)) -4
#steps = (wi if hi>wi else hi)
#steps = steps+9//2+1
steps = dimo
ex = dimo-hi
#print('ex,steps,a,b',ex,steps,a,b)
stepss = dimso//2
exs = dimso - si[0]
print('cs,exs,stepss,rad',cs,exs,stepss,rad)
'''
# larger box
A = ceil(a*2**0.5)
B = ceil(b*2**0.5)

we = w+A # w+2*A
he = h+B # h+2*B
# if make internal rectangle
UL = 0,0
LR = we,he

steps = (LR[0] if he>we else LR[1])
steps = steps//2+1
'''
from_colour = (241,239,234)
to_colour = (172,161,150)

# stretch y axis
img = Image.new('RGB', (size,size), '#FFFFFF')
idraw = ImageDraw.Draw(img)
'''
for i in range(steps):
    idraw.ellipse([ex+i, ex+i,wi+ex-i,hi+ex-i],fill=LerpColour(
        from_colour,to_colour,i/(steps-1)))
'''
for i in range(stepss):
    circle(idraw,[cs[0], cs[1]],dimso//2-i,fill=LerpColour(
        from_colour,to_colour,i/(stepss-1)))
    
idraw.rectangle([ul[0],ul[1],lrs[0],lrs[1]],outline='red')
#img.show()

#img.save('../figures/09rad_elloc.png')
print(we,he)
img.resize((we,he),resample=1)
img.save('../figures/09rad_ellocr.png')
