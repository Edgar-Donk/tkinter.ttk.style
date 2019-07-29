from PIL import Image, ImageDraw
'''
create radial gradient using points of colour

radial gradient, plots colour from inside to outside
normally lighter colour on inside so becomes from_colour

odd number pixels gives to_colour 4 corners and from_colour centre pixel
even number not quite from_colour at central area
'''

def LerpColour(c1,c2,t):
    return (int(c1[0]+(c2[0]-c1[0])*t),int(c1[1]+(c2[1]-c1[1])*t),
            int(c1[2]+(c2[2]-c1[2])*t))

w=25 # best if odd
h=25 # best if odd
centreX = (w-1)/2
centreY = (h-1)/2
hypotSq = (w-1)*(w-1) + (h-1)*(h-1)

from_colour = (241,239,234)
to_colour = (172,161,150)

img = Image.new('RGB', (w,h), '#FFFFFF')
idraw = ImageDraw.Draw(img)

for y in range(h):
    rise = centreY - y
    rise *= rise

    for x in range(w):
        run = centreX - x
        run *= run

        distSq = run + rise
        dist = 4 * distSq / hypotSq

        idraw.point([x,y],fill=LerpColour(from_colour,to_colour,dist))

# img.show()
img.save('rad.png')
