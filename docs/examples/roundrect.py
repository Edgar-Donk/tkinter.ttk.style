"""
provides common methods to generate widgets

Base_Rect single border, plain fill
Bi_Base_Rect double border, plain fill
Gr_Base_Rect single border, gradient fill
Gr_Bi_Base_Rect double border, gradient fill

All methods can make an open side as used in notebook tab
"""

from PIL import Image, ImageDraw

class Base_Rect():
    """ base class for rounded rectangles, single border, no gradient"""

    def __init__(self,fout,w,h,exp,radius,first,second,tab=0):
        """Creates widget single border, plain fill

        Parameters
        ----------
        fout: str
            output png file
        w,h: int
            width, height output file
        exp: int
            enlargment factor
        radius: int
            corner radius or gap in border
        first: tuple of integers
            outer border
        second: tuple of integers
            internal fill
         tab: int
            0 normal widget - default, 1 open ended tab
        """
        self.fout = fout
        self.w = w
        self.h = h
        self.exp = exp
        self.radius = radius
        self.first = first
        self.second = second
        self.tab = tab

        we = w*exp
        he = h*exp
        re = radius*exp

        img = self.base(we,he,exp,re,first,second,tab)
        self.trans(img,fout,w,h,radius)

    def base(self,we,he,exp,re,first,second,tab):
        """
        Draws base rectangle with rounded corners

        Parameters
        ----------
        we,he: int
            enlarged width, height
        exp: int
            enlargement factor
        re: int
            enlarged corner radius or gap in border
        first: tuple of integers
            outer border
        second: tuple of integers
            internal fill
        tab: int
            0 normal widget - default, 1 open ended tab

        Returns
        -------
        PIL Image handle
        """
        rect = Image.new('RGBA', (we,he), first)
        rdraw = ImageDraw.Draw(rect)

        tex = (0 if tab==1 else exp)
        rdraw.rectangle([exp,exp,we-exp-1,he-tex-1], fill=second)

        corner = self.round_corner(re, exp, first,second)
        if tab == 0:
            rect.paste(corner.rotate(90), (0, he - re))
            rect.paste(corner.rotate(180), (we - re, he - re))
        rect.paste(corner, (0, 0))
        rect.paste(corner.rotate(270), (we - re, 0))
        return rect

    def trans(self,img,fout,w,h,radius):
        """
        Resizes image to final size and makes transparent corners

        Parameters
        ----------
        img: str
            PIL image handle
        fout: str
            output png file
        w,h: int
            width, height output file
        radius: int
            corner radius or gap in border
        """
        img = img.resize((w,h),Image.LANCZOS)

        pixdata = img.load()
        clear = radius//2
        # create transparent pixels at 4 corners
        for x in range(0, img.size[0]):
            for y in range(0, img.size[1]):
                # find near white pixels
                if (x<clear and y<clear) or (x<clear and y>h-clear-1)\
                    or (x>w-clear-1 and y<clear) or (x>w-clear-1 and y>h-clear-1):
                    if sum(pixdata[x,y][:3]) >= 759:
                        pixdata[x,y] = (255,255,255,0)

        img.save(fout)
        return(img)

    def round_corner(self, rad, exp, ofill, ifill):
        """Draw a round corner, single border

        Parameters
        ----------
        rad: int
            corner radius or gap in border
        exp: int
            enlargement factor
        ofill: tuple of integers
            outer border
        ifill: tuple of integers
            internal fill

        Returns
        -------
        corner: str
            handle PIL Image
        """
        corner = Image.new('RGBA', (rad, rad), 'white')
        cdraw = ImageDraw.Draw(corner)
        self.create_pie(cdraw,[rad,rad],rad,fill=ofill)
        self.create_pie(cdraw,[rad,rad],rad-exp,fill=ifill)
        return corner

    def bi_round_corner(self, rad, exp, ofill, mfill, ifill):
        """Draw a round corner, double border

        Parameters
        ----------
        rad: int
            corner radius or gap in border
        exp: int
            enlargement factor
        ofill: tuple of integers
            outer border
        mfill: tuple of integers
            inner border
        ifill: tuple of integers
            internal fill

        Returns
        -------
        corner: str
            handle PIL Image
        """
        corner = Image.new('RGBA', (rad, rad), 'white')
        cdraw = ImageDraw.Draw(corner)
        self.create_pie(cdraw,[rad,rad],rad,fill=ofill)
        self.create_pie(cdraw,[rad,rad],rad-exp,fill=mfill)
        self.create_pie(cdraw,[rad,rad],rad-2*exp,fill=ifill)
        return corner

    def create_pie(self, idraw,c,r,fill='#888888',start=180,end=270):
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

    def LerpColour(self,c1,c2,t):
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

    def icol(self, startc, endc, steps, re, exp):
        """ Find the intermediate colours on the gradient

        Parameters
        ----------
        startc, endc: tuple of integers
            Colours in rgb
        steps: int
            number colour steps
        exp: int
            enlargement factor
        re: int
            enlarged corner radius or gap in border

        Returns
        -------
        startci, endci: tuple of integers
            Colours in rgb
        """
        y = (re - exp)/2
        startci = self.LerpColour(startc, endc, y/steps)
        endci = self.LerpColour(endc, startc, y/steps)
        return startci, endci


class Bi_Base_Rect(Base_Rect):
    # base class for rounded rectangles, double border, no gradient
    def __init__(self,fout,w,h,exp,radius,first,second,third,tab=0):
        '''Creates widget double border, plain fill

        Parameters
        ----------
        fout: str
            output png file
        w,h: int
            width, height output file
        exp: int
            enlargment factor
        radius: int
            corner radius or gap in border
        first: tuple of integers
            outer border
        second: tuple of integers
            inner border
        third: tuple of integers
            internal fill
         tab: int
            0 normal widget - default, 1 open ended tab
        '''
        self.fout = fout
        self.w = w
        self.h = h
        self.exp = exp
        self.radius = radius
        self.first = first
        self.second = second
        self.tab = tab
        Base_Rect.__init__(self,fout,w,h,exp,radius,first,second,tab)
        self.third = third

        we = w*exp
        he = h*exp
        re = radius*exp

        img = self.bi_base(we,he,exp,re,first,second,third,tab)
        self.trans(img,fout,w,h,radius)

    def bi_base(self,we,he,exp,re,first,second,third,tab):
        """
        Draws base rectangle with rounded corners

        Parameters
        ----------
        we,he: int
            enlarged width, height
        exp: int
            enlargement factor
        re: int
            enlarged corner radius or gap in border
        first: tuple of integers
            outer border
        second: tuple of integers
            inner border
        third: tuple of integers
            internal fill
        tab: int
            0 normal widget - default, 1 open ended tab

        Returns
        -------
            PIL Image handle
        """
        rect = Image.new('RGBA', (we,he), first)
        rdraw = ImageDraw.Draw(rect)

        tex = (0 if tab==1 else exp)
        rdraw.rectangle([exp,exp,we-exp-1,he-tex-1], fill=second)
        rdraw.rectangle([2*exp,2*exp,we-2*exp-1,he-2*tex-1], fill=third)

        corner = self.bi_round_corner(re, exp, first,second,third)
        if tab == 0:
            rect.paste(corner.rotate(90), (0, he - re))
            rect.paste(corner.rotate(180), (we - re, he - re))
        rect.paste(corner, (0, 0))
        rect.paste(corner.rotate(270), (we - re, 0))
        return rect

class Gr_Base_Rect(Base_Rect):
    # class for rounded rectangles, single border, with gradient
    def __init__(self,fout,w,h,exp,radius,first,second,startc,stopc,tab=0):
        '''Creates widget single border, gradient fill

        Parameters
        ----------
        fout: str
            output png file
        w,h: int
            width, height output file
        exp: int
            enlargment factor
        radius: int
            corner radius or gap in border
        first: tuple of integers
            outer border
        second: tuple of integers
            internal fill
        startc: tuple of integers
            gradient start colour - must be RGB
        stopc: tuple of integers
            gradient finish colour - must be RGB
         tab: int
            0 normal widget - default, 1 open ended tab

        '''
        self.fout = fout
        self.w = w
        self.h = h
        self.exp = exp
        self.radius = radius
        self.first = first
        self.second = second
        self.tab = tab
        Base_Rect.__init__(self,fout,w,h,exp,radius,first,second,tab)
        self.startc = startc
        self.stopc = stopc

        we = w*exp
        he = h*exp
        re = radius*exp

        img = self.gr_base(we,he,exp,re,first,second,startc,stopc,tab)
        self.trans(img,fout,w,h,radius)

    def gr_base(self,we,he,exp,re,first,second,startc,stopc,tab):
        """Draws gradient filled rectangle with rounded corners

        Parameters
        ----------
        we,he: int
            enlarged width, height
        exp: int
            enlargement factor
        re: int
            enlarged corner radius or gap in border
        first: tuple of integers
            outer border
        second: tuple of integers
            internal fill
        startc: tuple of integers
            gradient start colour - must be RGB
        stopc: tuple of integers
            gradient finish colour - must be RGB
        tab: int
            0 normal widget - default, 1 open ended tab

        Returns
        -------
            PIL Image handle
        """
        rect = Image.new('RGBA', (we,he), first)
        rdraw = ImageDraw.Draw(rect)

        tex = (0 if tab==1 else exp)
        steps = he - 2*tex

        for j in range(steps):
            cr,cg,cb = self.LerpColour(startc,stopc,j/(steps))
            rdraw.line([exp,j+exp,we-exp-1,j+exp],fill=(cr,cg,cb))

        inter = self.icol(startc, stopc, steps, re, exp)
        ufill = inter[0]
        lfill = inter[1]
        ucorner = self.round_corner(re, exp, first,ufill)
        lcorner = self.round_corner(re, exp, first,lfill)
        if tab == 0:
            rect.paste(lcorner.rotate(90), (0, he - re))
            rect.paste(lcorner.rotate(180), (we - re, he - re))
        rect.paste(ucorner, (0, 0))
        rect.paste(ucorner.rotate(270), (we - re, 0))
        return rect

class Gr_Bi_Base_Rect(Gr_Base_Rect):
    # class for rounded rectangles, double border, with gradient
    def __init__(self,fout,w,h,exp,radius,first,second,third,startc,stopc,tab=0):
        '''Creates widget double border, gradient fill

        Parameters
        ----------
        fout: str
            output png file
        w,h: int
            width, height output file
        exp: int
            enlargment factor
        radius: int
            corner radius or gap in border
        first: tuple of integers
            outer border
        second: tuple of integers
            inner border
        third: tuple of integers
            internal fill
        startc: tuple of integers
            gradient start colour - must be RGB
        stopc: tuple of integers
            gradient finish colour - must be RGB
         tab: int
            0 normal widget - default, 1 open ended tab
        '''
        self.fout = fout
        self.w = w
        self.h = h
        self.exp = exp
        self.radius = radius
        self.first = first
        self.second = second
        self.tab = tab
        self.startc = startc
        self.stopc = stopc
        #Bi_Base_Rect.__init__(self,fout,w,h,exp,radius,first,second,third,tab)


        we = w*exp
        he = h*exp
        re = radius*exp

        img = self.gr_bi_base(we,he,exp,re,first,second,third,startc,stopc,tab)
        self.trans(img,fout,w,h,radius)

    def gr_bi_base(self,we,he,exp,re,first,second,third,startc,stopc,tab):
        """Draws gradient filled rectangle, double border with rounded corners

        Parameters
        ----------
        we,he: int
            enlarged width, height
        exp: int
            enlargement factor
        re: int
            enlarged corner radius or gap in border
        first: tuple of integers
            outer border
        second: tuple of integers
            inner border
        third: tuple of integers
            internal fill
        startc: tuple of integers
            gradient start colour - must be RGB
        stopc: tuple of integers
            gradient finish colour - must be RGB
        tab: int
            0 normal widget - default, 1 open ended tab

        Returns
        -------
            PIL Image handle
        """
        rect = Image.new('RGBA', (we,he), first)
        rdraw = ImageDraw.Draw(rect)
        tex = (0 if tab==1 else exp)
        steps = he - 2*exp  - 2*tex

        rdraw.rectangle([exp,exp,we-exp-1,he-tex-1], fill=second)
        for j in range(steps):
            cr,cg,cb = self.LerpColour(startc,stopc,j/(steps))
            rdraw.line([2*exp,j+2*exp,we-2*exp-1,j+2*exp],fill=(cr,cg,cb))

        inter = self.icol(startc, stopc, steps, re, exp)
        ufill = inter[0]
        lfill = inter[1]

        ucorner = self.bi_round_corner(re, exp, first,second,ufill)
        lcorner = self.bi_round_corner(re, exp, first,second,lfill)
        if tab == 0:
            rect.paste(lcorner.rotate(90), (0, he - re))
            rect.paste(lcorner.rotate(180), (we - re, he - re))
        rect.paste(ucorner, (0, 0))
        rect.paste(ucorner.rotate(270), (we - re, 0))
        return rect

if __name__ == "__main__":

    Fout = 'test.png'
    W=25
    H=25
    Exp = 9 # enlargement, also thickness between radii
    Radius = 4 # gap
    '''
    First = '#5D9B90'
    Second = 'white'
    Third = None
    '''
    First = '#A3CCC4'
    Second = '#5D9B90'
    Third = 'white'

    Tab = 0
    Startc = (222,247,222)
    Stopc = (143,188,143)

    #Base_Rect(Fout, W, H, Exp, Radius, First, Second, Tab)
    #Bi_Base_Rect(Fout, W, H, Exp, Radius, First, Second, Third, Tab)
    #Gr_Base_Rect(Fout,W,H,Exp,Radius,First,Second,Startc,Stopc,Tab)
    Gr_Bi_Base_Rect(Fout,W,H,Exp,Radius,First,Second,Third,Startc,Stopc,Tab)


