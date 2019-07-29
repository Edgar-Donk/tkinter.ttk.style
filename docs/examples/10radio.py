'''
Radiobuttons

round buttons with central dark area when selected
'''

from PIL import Image, ImageDraw
from tools import transx, LerpColour, create_circle

exp = 9 # enlargement, also thickness between rectangles
w=17
h=17

we = w*exp  
he = h*exp
# make allowance for borders, shadow and highlight
ce = we//2 +1  # centre
steps = ce # gradient steps ce-e

back = 'white' #(102,153,204)
border = '#5D9B90' 
stopc = (144,237,215)
startc = (239,252,249)
mid = '#BDF3E7'
toc = (144,237,215)
fromc = (239,252,249)
middle = '#2D4C46'

img = Image.new('RGBA', (we,he), 'white')
idraw = ImageDraw.Draw(img)

create_circle(idraw,(ce,ce),ce,
                  fill=mid) # toc

for j in range(steps):
    cr,cg,cb = LerpColour(startc,stopc,j/(steps-1))
    create_circle(idraw,(ce+j//2,ce+j//2),ce-exp-j,
                  fill=(cr,cg,cb))

img = img.resize((w,h),Image.LANCZOS)

transx(img,w,h)

img.save('../images/lime/radio-n.png')
dimg = img.convert('L')
dimg = dimg.convert('RGBA')
transx(dimg,w,h)
dimg.save('../images/lime/radio-d.png')

simg = Image.new('RGBA', (we,he), 'white')
sidraw = ImageDraw.Draw(simg)

create_circle(sidraw,(ce,ce),ce,fill=border) 

for j in range(steps):
    cr,cg,cb = LerpColour(toc,fromc,j/(steps-1))
    create_circle(sidraw,(ce,ce-j//2),ce-exp-j,
                  fill=(cr,cg,cb))

create_circle(sidraw,(ce,ce),ce//3,
                  fill=middle)

simg = simg.resize((w,h),Image.LANCZOS)

transx(simg,w,h)

simg.save('../images/lime/radio-s.png')
dsimg = simg.convert('L')
dsimg = dsimg.convert('RGBA')
transx(dsimg,w,h)
dsimg.save('../images/lime/radio-ds.png')
