from PIL import Image, ImageDraw, ImageColor
from colorsys import rgb_to_hsv, hsv_to_rgb

size = width, height = 512, 256

halfh = height / 2

def LerpColourRGB(c1,c2,t):
    return (int(c1[0]+(c2[0]-c1[0])*t),int(c1[1]+(c2[1]-c1[1])*t),
            int(c1[2]+(c2[2]-c1[2])*t))

# used for HSV and YIQ
def LerpColour(c1,c2,t):
    return ((c1[0]+(c2[0]-c1[0])*t),(c1[1]+(c2[1]-c1[1])*t),
            (c1[2]+(c2[2]-c1[2])*t))

def rgb2hsv(t):
    """ convert PIL-like RGB tuple (0 .. 255) to colorsys-like
    HSV tuple (0.0 .. 1.0) """
    r,g,b = t
    r /= 255.0
    g /= 255.0
    b /= 255.0
    return rgb_to_hsv(r,g,b)

def hsv2rgb(t):
    """ convert a colorsys-like HSV tuple (0.0 .. 1.0) to a
    PIL-like RGB tuple (0 .. 255) """
    r,g,b = hsv_to_rgb(*t)
    r *= 255
    g *= 255
    b *= 255
    return (int(r),int(g),int(b))



img = Image.new('HSV', (size),'white')
idraw = ImageDraw.Draw(img)

startc = ImageColor.getrgb('hsv(0,100%,100%)')
endc = ImageColor.getrgb('hsv(0,0%,100%)')
startf = rgb2hsv(startc)
endf = rgb2hsv(endc)
ctry = 'hsv(60,100%,100%)'
idraw.rectangle([100,100,200,200],fill=ctry)
'''
for i in range(width):
    stepc = i / width
    idraw.line([i,0,i,halfh],fill=LerpColourRGB(startc,endc,stepc))
    idraw.line([i,halfh,i,height],fill=
               hsv2rgb(LerpColour(startf,endf,stepc)))
'''
img.show()