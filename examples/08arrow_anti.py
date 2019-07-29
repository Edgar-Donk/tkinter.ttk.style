from PIL import Image, ImageDraw
'''
antialiased arrow

simple downward pointing arrow
construct left and right lines adjacent to arrow
diagonals, then find how many arrow pixels
are next to every construction line pixels
then change their colours to antialias pixels
'''

back = (246,244,242,255) # = '#F6F4F2' 
acol = (110,110,109,255) #= '#6E6E6D'
afill = (158,157,156,255) # '#9E9D9C'
lcol = (255,165,0,255) #  = 'orange'
rcol = (255,255,0,255) # = 'yellow'

pcent = {0: back,
      1: (int(back[0]-acol[0]*0.25),int(back[1]-acol[1]*0.25),
          int(back[2]-acol[2]*0.25),255),
      2: (int(back[0]-acol[0]*0.5),int(back[1]-acol[1]*0.5),
          int(back[2]-acol[2]*0.5),255),
      3: (int(back[0]-acol[0]*0.75),int(back[1]-acol[1]*0.75),
          int(back[2]-acol[2]*0.75),255)}

# arrow vertices, top left, top right, point
atl = (5,11)
atr = (11,11)
ap = (8,15)

def tally(x,y,pos):
    tot = 0
    if pos == 'l':
        left = ((x,y-1),(x+1,y-1),(x+1,y),(x+1,y+1),(x,y+1))
        for il,lef in enumerate(left):
            if img.getpixel(lef) == (110,110,109,255):
                tot = tot + 1
        idraw.point([x,y],fill= pcent[tot])
    else:
        right = ((x,y-1),(x-1,y-1),(x-1,y),(x-1,y+1),(x,y+1))
        for ir,rig in enumerate(right):
            if img.getpixel(rig) == (110,110,109,255):
                tot = tot + 1
        idraw.point([x,y],fill= pcent[tot])
    

img = Image.new('RGBA', (16,24), back)
idraw = ImageDraw.Draw(img)
idraw.polygon([atl,atr,ap,(atl[0]+1,atl[1]+1)],fill=afill,outline=acol)
idraw.line([(atl[0]-1,atl[1]),(ap[0]-1,ap[1])],fill=lcol)
idraw.line([(atr[0]+1,atr[1]),(ap[0]+1,ap[1])],fill=rcol)
pixdata = img.load()

# find out where construction lines exist
for x in range(0, img.size[0]):
    for y in range(0, img.size[1]):
        (r,g,b,a) = pixdata[x,y]
        if (r,g,b,a) == (255,255,0,255):
            tally(x,y,'r')
        elif (r,g,b,a) == (255,165,0,255):
            tally(x,y,'l')

# done after antialiasing
idraw.point([ap[0],ap[1]-1],fill=acol)
 
# img.show()
img.save('../figures/08arrow_anti.png')