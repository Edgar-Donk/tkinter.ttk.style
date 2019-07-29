from PIL import Image, ImageDraw
from math import sqrt

'''
Toolbox of functions
'''

def LerpColour(c1,c2,t):
    '''
    Gives the colour found between 2 colours

    Args:
        c1, c2: colours in rgb
        t: ratio of colour mix 0 <= t <= 1

    Returns:
        colour in rgb
    '''
    return (int(c1[0]+(c2[0]-c1[0])*t),int(c1[1]+(c2[1]-c1[1])*t),
            int(c1[2]+(c2[2]-c1[2])*t))

def create_circle(idraw,c,r,fill):
    '''
    create circle using centre and radius

    Args:
        idraw: call to drawing function
        c: centre co-ordinates
        r: radius
        fill: fill colour

    Returns:
        Circle
    '''
    return idraw.ellipse([c[0]-r,c[1]-r,c[0]+r-1,c[1]+r-1],
            fill=fill)

def create_pie(idraw,c,r,fill='#888888',start=180,end=270):
    '''
    create pieslice using centre and radius, outline not used

    defaults to 90° in upper left quadrant
    Args:
        idraw: call to drawing function
        c: centre co-ordinates
        r: radius
        fill: fill colour
        start, end: start and end angles
    '''
    return idraw.pieslice([c[0]-r,c[1]-r,c[0]+r-1,c[1]+r-1],
                          fill=fill,start=start,end=end)

def icol(startc, endc, steps, re, exp):
    ''' find the intermediate colours on the gradient
    
    Args:
        startc: start rgb colour
        endc: finish rgb colour
        steps: number steps in gradient
        re: enlarged radius
        exp: enlargment factor
    '''
    y = (re - exp)/2
    startci = LerpColour(startc, endc, y/steps)
    endci = LerpColour(endc, startc, y/steps)
    return startci, endci

def trans(img,w,h,radius,cmax=759):
    '''
    create transparent pixels at 4 corners

    Args:
        img: call to image function
        w,h: image size width height
        radius: widget radius/ gap size
        cmax: near white colour sum
    '''
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
    '''
    find all near white pixels and change into transparent pixels 

    Args:
        img: call to image function
        w,h: image size width height
        cmax: near white colour sum
    '''
    pixdata = img.load()
    for x in range(0, img.size[0]):
        for y in range(0, img.size[1]):
            # find near white pixels
            rgba = pixdata[x,y]
            if sum(pixdata[x,y][:3]) >= cmax:
                pixdata[x,y] = (255,255,255,0)
    return(img)

def round_corner(rad, exp, ofill, ifill):
    """Draw a round corner, single border"""
    corner = Image.new('RGBA', (rad, rad), 'white')
    cdraw = ImageDraw.Draw(corner)
    create_pie(cdraw,[rad,rad],rad,fill=ofill)
    create_pie(cdraw,[rad,rad],rad-exp,fill=ifill)
    return corner

def gr_base(we,he,exp,re,first,second,startc,stopc):
    """Single border rounded rectangle with gradient"""  
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
    lcorner = round_corner(re, exp, first,lfill)
    rect.paste(lcorner.rotate(90), (0, he - re)) 
    rect.paste(lcorner.rotate(180), (we - re, he - re))
    rect.paste(ucorner, (0, 0))
    rect.paste(ucorner.rotate(270), (we - re, 0))
    return rect

def gr_2d_rect(we,he,exp,re,first,second,startc,stopc):
    '''Creates most widget single border, gradient fill
    
    Need to reduce in size and add transparent pixels

    Args:
        we, he: enlarged size
        exp: enlargment factor
        re: enlarged radius
        first: border rgb colour
        second: fill rgb colour
        startc: rgb gradient colour
        endc: rgb gradient colour
    '''                                               
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
    ucorner = round_corner(re, exp, first,ufill)
    lcorner = round_corner(re, exp, first,ufill)
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
