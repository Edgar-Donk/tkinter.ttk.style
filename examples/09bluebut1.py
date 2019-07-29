from PIL import Image, ImageDraw

e = 9 # enlargement, also thickness between rectangles
d = (e-1)//2 # displacement
w=32
h=32
we = w*e  
he = h*e
gap = 4 # gap size
s=gap*e # space

back = (102,153,204)
inner = (45,45,102)
outer = (102,153,204)

steps = 28*e
from_colour = (107,157,206) #(112,159,207)
to_colour = (240,245,249) #(239,244,249)

img = Image.new('RGB', (we,he), back) 

def create_pie(idraw,c,r,fill='#888888',start=180,end=270):
    return idraw.pieslice([c[0]-r,c[1]-r,c[0]+r-1,c[1]+r-1],
                          fill=fill,start=start,end=end)

# lerpcolour gives the colour found between 2 colours
# at fraction of whole c1 and c2 are rgb, 0 <= t <= 1
def LerpColour(c1,c2,t):
    return (int(c1[0]+(c2[0]-c1[0])*t),int(c1[1]+(c2[1]-c1[1])*t),
            int(c1[2]+(c2[2]-c1[2])*t))

def round_corner(radius, outer, inner, back):
    """Draw a round corner"""
    corner = Image.new('RGBA', (s+e, s+e), back)
    cdraw = ImageDraw.Draw(corner)
    create_pie(cdraw,[s+e,s+e],s+e,fill=outer)                   
    create_pie(cdraw,[s+e,s+e],s-e,fill=inner)
    create_pie(cdraw,[s+e,s+e],s-2*e,fill=back)
    return corner

def round_corner2(radius, outer, inner, back):
    """Draw a round corner"""
    corner = Image.new('RGBA', (s+e, s+e), back)
    cdraw = ImageDraw.Draw(corner)
    create_pie(cdraw,[s+e,s+e],s+e,fill=outer)                   
    create_pie(cdraw,[s+e,s+e],s-e,fill=inner)
    create_pie(cdraw,[s+e,s+e],s-2*e,fill=(240,245,249))
    return corner
 
def round_rectangle(size, radius, outer,inner,back):
    """Draw a rounded rectangle"""
    width, height = size
    box = 0,0,width-1,height-1
    rect = Image.new('RGBA', size, back)
    draw = ImageDraw.Draw(rect)
    corner = round_corner(radius, outer, inner, back)
    corner2 = round_corner2(radius, outer, inner, back)
    # The outer rectangle
    '''
    draw.rectangle(box, fill=outer)
    draw.rectangle( # The inner rectangle
        (box[0] + 2*e, box[1] + 2*e, box[2] - 2*e, box[3] - 2*e),
        fill=inner)
    draw.rectangle( # The innermost rectangle
        (box[0] + 3*e, box[1] + 3*e, box[2] - 3*e, box[3] - 3*e),
        fill=back)
    '''
    # gradient
    for j in range(steps):
        cr,cg,cb = LerpColour(from_colour,to_colour,j/(steps-1))
        draw.line([2*e,j+2*e,we-2*e-1,j+2*e],fill=(cr,cg,cb))
    rect.paste(corner, (0, 0))
    # Rotate the corner and paste it
    rect.paste(corner2.rotate(90), (0, height - radius-e))
    rect.paste(corner2.rotate(180), (width - radius-e, height - radius-e))
    rect.paste(corner.rotate(270), (width - radius-e, 0))
    return rect

img = round_rectangle((we, he), s, outer,inner,back)
    
img = img.resize((w,h),Image.LANCZOS)
idraw = ImageDraw.Draw(img)
idraw.line([5,2,26,2],fill=inner)
idraw.line([5,29,26,29],fill=inner)
idraw.line([2,5,2,26],fill=inner)
idraw.line([29,5,29,26],fill=inner)

img.save('../figures/09bluebutton1.png')