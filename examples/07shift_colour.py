'''
Make simple colour replacement based on the darkest main colour
component (pivot) being replaced by the target colour. Other
colours are chosen according to their lightness. For simplicity
source colours are all taken to be of much the same hue, final
colours are based on the target colour selected by lightness.

A simple linear comparison is made between the pivot and source
colours, where we know that if the source is the same as the pivot
we will use the target colour for our final colour and if the source is
white then the final colour will also be white.
'''
from PIL import Image
from colorsys import rgb_to_yiq, yiq_to_rgb

sourceFile = '../images/comboarrow-n' # file name less .png
pivot = (182, 171, 160) # use the combo-n rim as basis
#pivot = (233, 135, 94) # use as basis for combo-rf
#pivot = (215, 208, 200) # source for comboarrow-a
ptot = sum(pivot)

#target = (0, 255, 255) # cyan
#target = (64,224,208) # use as basis for combo-rf
target = (127,255,212) # aquamarine
rtar = 127 # use as target 
gtar = 255 # use as target
btar = 212 # use as target

img = Image.open(sourceFile+'.png')
img = img.convert("RGBA")
pixdata = img.load() # pixdata can be thought as the source

for x in range(0, img.size[0]):
    for y in range(0, img.size[1]):
        # skip white and transparent pixels
        if pixdata[x,y] in ((255,255,255,255),(254,254,254,255),
                            (246,244,242,0)):
            continue
        # mask used in combo-rd
        #elif (x > 1 and x < 24) and (y > 1 and y < 22):
            #pixdata[x,y] = (200,200,200,255)
            
        # mask used in comboarrow
        elif (x > 3 and x < 13) and (y > 10 and y < 17):
            continue
            
        # mask used in arrow
        #elif (x > 2 and x < 12) and (y > 5 and y < 12):
            #continue
        
        else:
            alpha = pixdata[x,y][-1]
            if pixdata[x, y] == pivot:
                pixdata[x,y] = (rtar, gtar, btar,alpha)
            else:
                # first estimate of lightness
                stot = sum(pixdata[x,y][:3]) # source sum
                
                finalr = int((rtar-255)*(stot-765)/(ptot-765)+255)
                finalg = int((gtar-255)*(stot-765)/(ptot-765)+255)
                finalb = int((btar-255)*(stot-765)/(ptot-765)+255) 
                
                pixdata[x,y] = (finalr, finalg, finalb, alpha) # final colour

img.save(sourceFile+'_new.png') # new image - check before using
        
