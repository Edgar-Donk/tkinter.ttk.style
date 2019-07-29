from PIL import Image
from math import modf, ceil

'''
Find the average rgb values in rows and columns
'''

# round float up or down depending on fractional part
def rupdown(x):
    if modf(x)[0] >= 0.5:
        rud = ceil(x)
    else:
        rud = int(x)
    return rud
    
img = Image.open('../images/keramik_button-n.gif')
# '../images/cl_button-n.gif'elegance_button-default.gif
img = img.convert('RGBA')
pixdata = img.load() # pixdata can be thought as the source
w = img.size[0]
h = img.size[1]

print('rows')
for y in range(2,h-3): # lower h//2,h-4
    # upper (3,h//2-1) #cl (2,h-3)
    count = 0
    r,g,b,a = 0,0,0,0
    for x in range(6,w-7): # 3,w-4 (2,w-3)
        pixr,pixg,pixb,pixa = pixdata[x,y]
        r += pixr
        g += pixg
        b += pixb
        a += pixa
        count += 1
    r,g,b = rupdown(r/count),rupdown(g/count),rupdown(b/count)       
    print('(',r,',',g,',',b,')')

print('cols')
for x in range(6,w-7): #3,w-4 (2,h-3)
    count = 0
    r,g,b,a = 0,0,0,0
    for y in range(2,h-3): # lower h//2,h-4
        #upper (3,h//2-1): # (2,w-3)
        pixr,pixg,pixb,pixa = pixdata[x,y]
        r += pixr
        g += pixg
        b += pixb
        a += pixa
        count += 1
    r,g,b = rupdown(r/count),rupdown(g/count),rupdown(b/count)       
    print('(',r,',',g,',',b,')')    
