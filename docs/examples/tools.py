"""
Toolbox of functions used while creating theme
"""

from PIL import Image, ImageDraw
from math import sqrt

def LerpColour(c1,c2,t):
    """
    Gives the colour found between 2 colours

    Parameters
    ----------
    c1, c2: tuple of integers
        Colours in rgb
    t: decimal
        Ratio of colour mix 0 <= t <= 1

    Returns
    -------
        colour in rgb
    """
    return (int(c1[0]+(c2[0]-c1[0])*t),int(c1[1]+(c2[1]-c1[1])*t),
            int(c1[2]+(c2[2]-c1[2])*t))

def create_circle(idraw,c,r,fill):
    """
    create circle using centre and radius

    Parameters
    ----------
        idraw: str
            PIL drawing handle
        c: int
            centre co-ordinates
        r: int
            radius
        fill: str or tuple of int
            fill colour name, hash or tuple

    Returns
    -------
        Circle
    """
    return idraw.ellipse([c[0]-r,c[1]-r,c[0]+r-1,c[1]+r-1],
            fill=fill)

def create_pie(idraw,c,r,fill='#888888',start=180,end=270):
    """
    create pieslice using centre and radius, outline not used

    defaults to 90° in upper left quadrant
    Parameters
    ----------
        idraw: str
            PIL drawing handle
        c: int
            centre co-ordinates
        r: int
            radius
        fill: str or tuple of int
            fill colour name, hash or tuple
        start, end: int
            start and end angles in degrees
    """
    return idraw.pieslice([c[0]-r,c[1]-r,c[0]+r-1,c[1]+r-1],
                          fill=fill,start=start,end=end)

def icol(startc, stopc, steps, re, exp):
    """ find the intermediate colours on the gradient

    Parameters
    ----------
        startc: tuple of int
            start rgb colour
        stopc: tuple of int
            finish rgb colour
        steps: int
            number steps in gradient
        re: int
            enlarged radius
        exp: int
            enlargement factor
    """
    y = (re - exp)/2
    startci = LerpColour(startc, stopc, y/steps)
    stopci = LerpColour(stopc, startc, y/steps)
    return startci, stopci

def trans(img,w,h,radius,cmax=759):
    """
    create transparent pixels at 4 corners

    Parameters
    ----------
        img: str
            PIL drawing handle
        w,h: int
            image size width height
        radius: int
            corner radius/ gap size
        cmax: int
            near white colour sum
    """
    pixdata = img.load()
    clear = radius//2
    for x in range(0, img.size[0]):
        for y in range(0, img.size[1]):
            # find near white pixels
            if (x<clear and y<clear) or (x<clear and y>h-clear-1)\
                or (x>w-clear-1 and y<clear) or (x>w-clear-1 and y>h-clear-1):
                if sum(pixdata[x,y][:3]) >= cmax:
                    pixdata[x,y] = (255,255,255,0)

    return(img)

def transx(img,w,h,cmax=759):
    """
    find all near white pixels and change into transparent pixels

    Parameters
    ----------
        img: str
            PIL drawing handle
        w,h: int
            image size width height
        cmax: int
            near white colour sum
    """
    pixdata = img.load()
    for x in range(0, img.size[0]):
        for y in range(0, img.size[1]):
            # find near white pixels
            rgba = pixdata[x,y]
            if sum(pixdata[x,y][:3]) >= cmax:
                pixdata[x,y] = (255,255,255,0)
    return(img)

def round_corner(rad, exp, ofill, ifill):
    """Draw a round corner, single border

    Parameters
    ----------
    rad: int
        corner radius
    exp: int
        enlargement factor, normally 9
    ofill: str or int
        outer fill
    ifill: str or int
        inner fill

    """
    corner = Image.new('RGBA', (rad, rad), 'white')
    cdraw = ImageDraw.Draw(corner)
    create_pie(cdraw,[rad,rad],rad,fill=ofill)
    create_pie(cdraw,[rad,rad],rad-exp,fill=ifill)
    return corner

def gr_base(we,he,exp,re,first,second,startc,stopc):
    """Single border rounded rectangle with gradient

    Parameters
    ----------
    we, he: int
        width, height of enlarged image
    exp: int
        enlargement factor
    re: int
        enlarged corner radius/ gap size
    first, second: str or int
        colours of corners
    startc: tuple of int
        start rgb colour
    stopc: tuple of int
        finish rgb colour

    """
    rect = Image.new('RGBA', (we,he), first)
    rdraw = ImageDraw.Draw(rect)

    #tex = (0 if tab==1 else exp)
    steps = he - 2*exp

    for j in range(steps):
        cr,cg,cb = LerpColour(startc,stopc,j/(steps))
        rdraw.line([exp,j+exp,we-exp-1,j+exp],fill=(cr,cg,cb))

    inter = icol(startc, stopc, steps, re, exp)
    ufill = inter[0]
    lfill = inter[1]
    ucorner = round_corner(re, exp, first,ufill)
    lcorner = round_corner(re, exp, second,lfill)
    rect.paste(lcorner.rotate(90), (0, he - re))
    rect.paste(lcorner.rotate(180), (we - re, he - re))
    rect.paste(ucorner, (0, 0))
    rect.paste(ucorner.rotate(270), (we - re, 0))
    return rect

def gr_2d_rect(we,he,exp,re,first,second,startc,stopc):
    """Creates most widget single border, gradient fill

    Need to reduce in size and add transparent pixels

    Parameters
    ----------
        we, he: int
            width, height enlarged sizes
        exp: int
            enlargment factor
        re: int
            enlarged radius
        first: tuple of int
            border rgb colour
        second: tuple of int
            fill rgb colour
        startc: tuple of int
            rgb gradient colour
        stopc: tuple of int
            rgb gradient colour
    """
    rect = Image.new('RGBA', (we,he), first)
    rdraw = ImageDraw.Draw(rect)

    steps = we//2+1-exp

    for j in range(steps):
        #j = j//2
        cr,cg,cb = LerpColour(startc,stopc,j/(steps-1))
        rdraw.rectangle([j+exp,j+exp,we-exp-1-j,he-exp-1-j],fill=(cr,cg,cb))

    inter = icol(startc, stopc, steps, re, exp)
    ufill = inter[0]
    lfill = inter[1]
    ucorner = round_corner(re, exp, first, ufill)
    lcorner = round_corner(re, exp, second, ufill)
    rect.paste(lcorner.rotate(90), (0, he - re))
    rect.paste(lcorner.rotate(180), (we - re, he - re))
    rect.paste(ucorner, (0, 0))
    rect.paste(ucorner.rotate(270), (we - re, 0))
    return rect

if __name__ == "__main__":
    fout = '../images/lime/test2.png'
    w=26
    h=24
    radius = 5
    img = Image.open(fout)

    trans(w,h,radius,img)
    transx(w,h,img)
