from PIL import Image, ImageDraw

# http://nadiana.com/pil-tutorial-basic-advanced-drawing

e = 9 # enlargement, also thickness between rectangles
w=16
h=23
we = w*e  # based on circle sizes
he = h*e
j = 5 # gap size
s=j*e # space

# create pieslice with centre and radius, assume only fill used
def create_pie(idraw,c,r,fill='#888888',start=180,end=270):
    return idraw.pieslice([c[0]-r,c[1]-r,c[0]+r-1,c[1]+r-1],
                          fill=fill,start=start,end=end)

def round_corner(radius, outline, inner, fill):
    """Draw a round corner"""
    corner = Image.new('RGBA', (s+e, s+e), (0, 0, 0, 0))
    idraw = ImageDraw.Draw(corner)
    create_pie(idraw,[s+e,s+e],s+e,fill=outline)
    create_pie(idraw,[s+e,s+e],s,fill=inner)
    create_pie(idraw,[s+e,s+e],s-e,fill=fill)
    return corner
 
def round_rectangle(size, radius, outline,inner, fill):
    """Draw a rounded rectangle"""
    width, height = size
    box = 0,0,width-1,height-1
    rect = Image.new('RGBA', size, fill)
    draw = ImageDraw.Draw(rect)
    corner = round_corner(radius, outline, inner, fill)
    draw.rectangle(box, fill=outline)
    # The outer rectangle
    draw.rectangle( # The inner rectangle
        (box[0] + e, box[1] + e, box[2] - e, box[3] - e),
        fill=inner)
    draw.rectangle( # The innermost rectangle
        (box[0] + 2*e, box[1] + 2*e, box[2] - 2*e, box[3] - 2*e),
        fill=fill)
    rect.paste(corner, (0, 0))
    rect.paste(corner.rotate(90), (0, height - radius-e))
    # Rotate the corner and paste it
    rect.paste(corner.rotate(180), (width - radius-e, height - radius-e))
    rect.paste(corner.rotate(270), (width - radius-e, 0))
    return rect
 
img = round_rectangle((we, he), s, "lightblue", "blue", 'white')
#img.show()
img.save('rounded_rect_out'+str(j)+'.png')
