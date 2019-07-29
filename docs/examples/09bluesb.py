from PIL import Image, ImageDraw

w=14
h=14
steps = 12

back = 'white' #(102,153,204)
inner = (45,45,102)
from_colour = (111,159,207)
to_colour = (228,236,245)

# lerpcolour gives the colour found between 2 colours
# at fraction of whole c1 and c2 are rgb, 0 <= t <= 1
def LerpColour(c1,c2,t):
    return (int(c1[0]+(c2[0]-c1[0])*t),int(c1[1]+(c2[1]-c1[1])*t),
            int(c1[2]+(c2[2]-c1[2])*t))

img = Image.new('RGBA', (w,h), back) 
idraw = ImageDraw.Draw(img)

# gradient
for j in range(steps):
    cr,cg,cb = LerpColour(from_colour,to_colour,j/(steps-1))
    idraw.line([1,j+1,w-1,j+1],fill=(cr,cg,cb))
    
idraw.rectangle([0,0,w-1,h-1],outline=inner)    

idraw.point([0,0],fill=(0,0,0,0))
idraw.point([w-1,0],fill=(0,0,0,0))
idraw.point([0,h-1],fill=(0,0,0,0))
idraw.point([w-1,h-1],fill=(0,0,0,0))

img.save('../figures/09bluesb.png')



