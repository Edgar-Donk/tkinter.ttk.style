from PIL import Image, ImageDraw

e = 9 # enlargement, also thickness between rectangles
d = (e-1)//2 # displacement
w=16
h=24
we = w*e  
he = h*e
gap = 5 # gap size
s=gap*e # space

back = (246,244,242)
outer = (171,158,146)

acol = (110,110,109) #= '#6E6E6D'
afill = (158,157,156) # '#9E9D9C'
lcol = (255,165,0) #  = 'orange'
rcol = (255,255,0) # = 'yellow'

# arrow vertices, top left, top right, point
atl = (5,11)
atr = (11,11)
ap = (8,15)

pcent = {0: back,
      1: (int(back[0]-acol[0]*0.25),int(back[1]-acol[1]*0.25),
          int(back[2]-acol[2]*0.25)),
      2: (int(back[0]-acol[0]*0.5),int(back[1]-acol[1]*0.5),
          int(back[2]-acol[2]*0.5)),
      3: (int(back[0]-acol[0]*0.75),int(back[1]-acol[1]*0.75),
          int(back[2]-acol[2]*0.75))}

def tally(x,y,pos):
    tot = 0
    if pos == 'l':
        left = ((x,y-1),(x+1,y-1),(x+1,y),(x+1,y+1),(x,y+1))
        for il,lef in enumerate(left):
            if img.getpixel(lef) == (110,110,109,255):
                tot = tot + 1
        idr.point([x,y],fill= pcent[tot])
    else:
        right = ((x,y-1),(x-1,y-1),(x-1,y),(x-1,y+1),(x,y+1))
        for ir,rig in enumerate(right):
            if img.getpixel(rig) == (110,110,109,255):
                tot = tot + 1
        idr.point([x,y],fill= pcent[tot])

# create pieslice with centre and radius, assume only fill used
def create_pie(idraw,c,r,fill='#888888',start=180,end=270):
    return idraw.pieslice([c[0]-r,c[1]-r,c[0]+r-1,c[1]+r-1],
                          fill=fill,start=start,end=end)

def round_corner(radius, back, outer):
    """Draw a round corner"""
    corner = Image.new('RGBA', (s, s), 'white')
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
# img.show()
img = img.resize((w,h),Image.LANCZOS)

pixdata = img.load() # pixdata can be thought as the source
for x in range(0, img.size[0]):
    for y in range(0, img.size[1]):
        # find near white pixels
        if sum(pixdata[x,y][:3]) >= 759:
            # top and bottom lefhand corners
            if (x<3 and y<3) or (x<3 and y>h-3) or\
             (x>w-3 and y<3) or (x>w-3 and y>h-3):
                pixdata[x,y] = (255,255,255,0)

idr = ImageDraw.Draw(img)

idr.polygon([atl,atr,ap,(atl[0]+1,atl[1]+1)],fill=afill,outline=acol)
idr.line([(atl[0]-1,atl[1]),(ap[0]-1,ap[1])],fill=lcol)
idr.line([(atr[0]+1,atr[1]),(ap[0]+1,ap[1])],fill=rcol)
idr.point([ap[0],ap[1]+1],fill=rcol)

# find out where construction lines exist
for x in range(0, img.size[0]):
    for y in range(0, img.size[1]):
        (r,g,b,a) = pixdata[x,y]
        if (r,g,b,a) == (255,255,0,255):
            tally(x,y,'r')
        elif (r,g,b,a) == (255,165,0,255):
            tally(x,y,'l')

# done after antialiasing
idr.point([ap[0],ap[1]-1],fill=acol)


img.save('../figures/09comboarrow'+str(gap)+'.png')
