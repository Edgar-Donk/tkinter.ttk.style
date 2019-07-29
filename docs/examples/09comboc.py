from PIL import Image, ImageDraw, ImageOps

# http://nadiana.com/pil-tutorial-basic-advanced-drawing

e = 9 # enlargement, also thickness between rectangles
d = (e-1)//2 # displacement
w=26
h=24
we = w*e  # based on circle sizes
he = h*e
j = 4 # gap size
s=j*e # space

outer =  "#EDEBE7"#'white' #
inner =  (171,158,146) #"#B6ABA0" # (151,136,120)
fill = 'white'

# create pieslice with centre and radius, assume only fill used
def create_pie(idraw,c,r,fill='#888888',start=180,end=270):
    return idraw.pieslice([c[0]-r,c[1]-r,c[0]+r-1,c[1]+r-1],
                          fill=fill,start=start,end=end)

def round_corner(radius, ofill, ifill, grad):
    """Draw a round corner"""
    corner = Image.new('RGBA', (s+e, s+e), '#FFFFFF')
    idraw = ImageDraw.Draw(corner)
    create_pie(idraw,[s+e,s+e],s+e,fill=ofill)                   
    create_pie(idraw,[s+e,s+e],s,fill=ifill)
    create_pie(idraw,[s+e,s+e],s-e,fill=grad)
    return corner
 
def round_rectangle(size, radius, outer,inner,fill):
    """Draw a rounded rectangle"""
    width, height = size
    box = 0,0,width-1,height-1
    rect = Image.new('RGBA', size, fill)
    draw = ImageDraw.Draw(rect)
    corner = round_corner(radius, outer, inner, fill)
    draw.rectangle(box, fill=outer)
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
 
img = round_rectangle((we, he), s, outer,inner,fill)
#img.show()
#img.save('rounded_rect_out'+str(j)+'.png')
img = img.resize((w,h),Image.LANCZOS) # BICUBIC


# make the corners transparent
pixdata = img.load() # pixdata can be thought as the source
for x in range(0, img.size[0]):
    for y in range(0, img.size[1]):
        # find near white pixels
        if sum(pixdata[x,y][:3]) >= 759:
            # top and bottom lefhand corners
            if (x<3 and y<3) or (x<3 and y>20):
                pixdata[x,y] = (255,255,255,0)

im = ImageDraw.Draw(img)

im.line([23,4,23,19],fill='white')
im.line([4,21,21,21],fill='white')

ImageOps.crop(img,(0,0,j-2,0)).save('../figures/09combo.png')
# crop alone compressed the image to a smaller size

#img.save('../figures/rounded_rect_outf'+str(j)+'.png')
