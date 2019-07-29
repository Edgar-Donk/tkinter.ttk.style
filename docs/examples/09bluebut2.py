from PIL import Image, ImageDraw

w=32
h=32
steps = 26

back = (102,153,204)
inner = (45,45,102)
from_colour = (112,159,207)
to_colour = (239,244,249)

# lerpcolour gives the colour found between 2 colours
# at fraction of whole c1 and c2 are rgb, 0 <= t <= 1
def LerpColour(c1,c2,t):
    return (int(c1[0]+(c2[0]-c1[0])*t),int(c1[1]+(c2[1]-c1[1])*t),
            int(c1[2]+(c2[2]-c1[2])*t))

img = Image.new('RGB', (w,h), back) 
idraw = ImageDraw.Draw(img)

# gradient
for j in range(steps):
    cr,cg,cb = LerpColour(from_colour,to_colour,j/(steps-1))
    idraw.line([3,j+3,w-3-1,j+3],fill=(cr,cg,cb))
    
idraw.rectangle([2,2,w-3,h-3],outline=inner)    

idraw.point([2,2],fill=back)
idraw.point([w-3,2],fill=back)
idraw.point([2,h-3],fill=back)
idraw.point([w-3,h-3],fill=back)

idraw.point([3,3],fill=inner)
idraw.point([w-4,3],fill=inner)
idraw.point([3,h-4],fill=inner)
idraw.point([w-4,h-4],fill=inner)
img.save('../figures/09bluebutton2.png')