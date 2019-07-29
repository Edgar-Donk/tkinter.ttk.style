from PIL import Image, ImageDraw

# based on elegance_button-default.gif
# creating radial interpolation, then darken lower half

# lerpcolour gives the colour found between 2 colours at fraction of whole
# c1 and c2 are rgb, 0 <= t <= 1
def LerpColour(c1,c2,t):
    return (int(c1[0]+(c2[0]-c1[0])*t),int(c1[1]+(c2[1]-c1[1])*t),
            int(c1[2]+(c2[2]-c1[2])*t))

we = 60
he = 34
img = Image.new('RGB', (we,he), '#A4A4A4')
idraw = ImageDraw.Draw(img)

w = we-6 
h = he//2-1 
centreX = (w-1)/2
centreY = (h-1)/2
hypotSq = (w-1)*(w-1) + (h-1)*(h-1)
    
to_colour = (230, 231, 230)
from_colour = (200, 200, 200)
to_colour2 = (199,199,198)
from_colour2 = (168,168,168)
    
# pixdata = img.load() # pixdata can be thought as the source

idraw.line([0,0,we-1,0],fill=(164,164,164))
idraw.line([0,0,0,he-1],fill=(164,164,164))
idraw.line([1,he-1,we-1,he-1],fill=(231,231,231))
idraw.line([we-1,0,we-1,he-1],fill=(231,231,231))
idraw.rectangle([1,1,we-2,he-2],fill=(67,67,67))
idraw.line([2,2,we-3,2],fill=(245,245,245))
idraw.line([2,2,2,he-3],fill=(245,245,245))
idraw.line([3,he-3,we-3,he-3],fill=(176,175,175))
idraw.line([we-3,2,we-3,he-3],fill=(176,175,175))

for y in range(3,h+3): # (3,h+3)
    rise = centreY - y
    rise *= rise
    
    for x in range(3,w+3): # (3,w+3)
        run = centreX - x
        run *= run
    
        distSq = run + rise
        dist = 4 * distSq / hypotSq
    
        idraw.point([x,y],fill=LerpColour(from_colour,to_colour,dist))

for y in range(h+1,he-3): # (3,h+3)
    rise = centreY - y
    rise *= rise
    
    for x in range(3,w+3): # (3,w+3)
        run = centreX - x
        run *= run
    
        distSq = run + rise
        dist = 4 * distSq / hypotSq
    
        idraw.point([x,y],fill=LerpColour(from_colour2,to_colour2,dist))
    

# darken image in lower half

pixdata = img.load()
for y in range(int(centreY+4),h+4):
    for x in range(3,w+4):
        r,g,b = pixdata[x,y]
        pixdata[x,y] = r-20,g-20,b-20


#img.show()    
img.save('../figures/09eleg_button2.png')
