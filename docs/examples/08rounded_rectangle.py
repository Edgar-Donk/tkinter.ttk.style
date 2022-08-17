# Rounded Rectangle
from PIL import Image, ImageDraw

e = 9 # enlargement, also thickness between rectangles
w = 23
h = 23
we = h*e  # based on circle sizes
he = w*e
j = 5 # gap size
s = j*e # space

# create pieslice with centre and radius, assume only fill used
def create_pie(idraw,c,r,fill='#888888',start=180,end=270):
    return idraw.pieslice([c[0]-r,c[1]-r,c[0]+r-1,c[1]+r-1],
                          fill=fill,start=start,end=end)

def round_corner(radius, outline, fill):
    """Draw a round corner"""
    corner = Image.new('RGBA', (s, s), (0, 0, 0, 0))
    idraw = ImageDraw.Draw(corner)
    create_pie(idraw,[s,s],s,fill=outline)
    create_pie(idraw,[s,s],s-e,fill=fill)
    return corner

def round_rectangle(size, radius, outline, fill):
    """Draw a rounded rectangle"""
    width, height = size
    box = 0,0,width-1,height-1
    rect = Image.new('RGBA', size, fill)
    draw = ImageDraw.Draw(rect)
    corner = round_corner(radius, outline, fill)
    draw.rectangle(box, fill=outline)
    # The outer rectangle
    draw.rectangle( # The inner rectangle
        (box[0] + e, box[1] + e, box[2] - e, box[3] - e),
        fill=fill)
    rect.paste(corner, (0, 0))
    rect.paste(corner.rotate(90), (0, height - radius))
    # Rotate the corner and paste it
    rect.paste(corner.rotate(180), (width - radius, height - radius))
    rect.paste(corner.rotate(270), (width - radius, 0))
    return rect

img = round_rectangle((we, he), s, "blue", "white")
#img.show()
img.save('../figures/08rounded_rect'+str(j)+'.png')

limg = img.resize((w,h),Image.LANCZOS)
#limg.show()
limg.save('../figures/08rounded_rect_L'+str(j)+'.png')
