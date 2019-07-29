from PIL import Image, ImageDraw
from math import ceil, sqrt

def LerpColour(c1,c2,t):
    return (int(c1[0]+(c2[0]-c1[0])*t),int(c1[1]+(c2[1]-c1[1])*t),
            int(c1[2]+(c2[2]-c1[2])*t))

w = 60
h = 34
# centre
cx = w//2
cy = h//2
print('cx,cy',cx,cy)
# target rectangle
border = 3
wi = w-(border-1)*2  # we-4
hi = h-(border-1)*2  # he-4

ul = border,border # corner
lr = wi,hi # corner
# semi-axes
a = cx-ul[0]
b = cy-ul[1]
semi_rad = sqrt(a*a+b*b)
# larger box
A = round(a*sqrt(2)) # ceil
B = round(b*sqrt(2)) # ceil
#dimo = round(semi_rad * sqrt(2))
#ex = dimo - b
exa = A - a
exb = B - b
print('exa,a,exb,b',exa,a,exb,b)
we = w+A # w+2*A
he = h+B # h+2*B
# if make internal rectangle
UL = 0,0
LR = we,he

#steps = (LR[0] if he>we else LR[1])
steps = B #dimo # steps//2+1
xf = A/B # x multiplication factor

from_colour = (241,239,234)
to_colour = (172,161,150)

img = Image.new('RGB', (w+2*exa,h+2*exb), '#FFFFFF') # (we+1,he+1)
idraw = ImageDraw.Draw(img)

for i in range(steps):
    #idraw.ellipse([UL[0]+i, UL[1]+i,LR[0]-i,LR[1]-i],fill=LerpColour(
    idraw.ellipse([cx-A+round(i*xf), cy-B+i,cx+A-round(i*xf),cy+B-i],fill=LerpColour(
        from_colour,to_colour,i/(steps-1)))
    #print(he+ex-i)

#idraw.rectangle([ul[0]+A//2,ul[1]+B//2,lr[0]+A//2,lr[1]+B//2,],outline='red')
idraw.rectangle([border,border,wi,hi],outline='red')
idraw.point([cx,cy],fill='red')
#img.show()
img.save('../figures/09rad_ell.png')
