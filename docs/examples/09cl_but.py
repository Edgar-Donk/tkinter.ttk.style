from PIL import Image, ImageDraw

# lerpcolour gives the colour found between 2 colours at fraction of whole
# c1 and c2 are rgb, 0 <= t <= 1
def LerpColour(c1,c2,t):
    return (int(c1[0]+(c2[0]-c1[0])*t),int(c1[1]+(c2[1]-c1[1])*t),
            int(c1[2]+(c2[2]-c1[2])*t))

# create pieslice with centre and radius, assume only fill used
def create_pie(idraw,c,r,fill='#888888',start=180,end=270):
    return idraw.pieslice([c[0]-r,c[1]-r,c[0]+r-1,c[1]+r-1],
                          fill=fill,start=start,end=end)

w = 28
h = 28
e = 9 # enlargement, also thickness between rectangles
we = w*e  
he = h*e
gap = 4 # gap size
s=gap*e # space

back = '#EFEBE7'
outer = (148,125,123) #(141,117,115)
shade = (231,219,214)

def round_corner(radius, back, outer):
    """Draw a round corner"""
    corner = Image.new('RGBA', (s, s), back)
    idraw = ImageDraw.Draw(corner)
    create_pie(idraw,[s,s],s,fill=outer)
    create_pie(idraw,[s,s],s-e,fill=back)
    return corner

def round_rectangle(size, radius, back, outer):
    """Draw a rounded rectangle"""
    width, height = size
    box = 0,0,width-1,height-1
    rect = Image.new('RGBA', size, back)
    draw = ImageDraw.Draw(rect)
    corner = round_corner(radius, back, outer)
    draw.rectangle(box, fill=outer)
    # The outer rectangle
    draw.rectangle( # The inner rectangle
        (box[0] + e, box[1] + e, box[2] - e, box[3] - e),
        fill=back)
    rect.paste(corner, (0, 0))
    rect.paste(corner.rotate(90), (0, height - radius))
    # Rotate the corner and paste it
    rect.paste(corner.rotate(180), (width - radius, height - radius))
    rect.paste(corner.rotate(270), (width - radius, 0))
    return rect
 
img = round_rectangle((we, he), s, back, outer)
img = img.resize((w,h),Image.LANCZOS)
rdraw = ImageDraw.Draw(img)

# colours determined from 08find_line_colour.py
from_colour = (250, 248, 247)
to_colour = (229, 220, 215)
steps = h-4

# gradient
for j in range(steps):
    cr,cg,cb = LerpColour(from_colour,to_colour,j/(steps-1))
    rdraw.line([2,j+2,w-3,j+2],fill=(cr,cg,cb))

# highlights
rdraw.line([2,1,w-3,1],fill='white')
rdraw.line([1,2,1,h-3],fill='white')

# extend shading
rdraw.point([w-2,2],fill=shade)
rdraw.point([w-2,h-3],fill=shade)
rdraw.point([w-3,h-2],fill=shade)
rdraw.point([2,h-2],fill=shade)

img.save('../figures/09clbut.png') 