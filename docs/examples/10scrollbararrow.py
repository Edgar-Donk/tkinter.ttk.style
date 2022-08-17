'''
create right and up arrows

lime scrollbar thumb - used as template for other lime
widgets

'''
from PIL import Image, ImageDraw
from tools import transx


img = Image.open('../images/lime/slider-hn.png')
pimg = img
w, h = img.size
rdraw = ImageDraw.Draw(img)
pdraw = ImageDraw.Draw(pimg)

# draw right arrow
# upper surface lightest, lower surface darkest
light = 'GreenYellow'
med = 'LawnGreen'
border = '#5D9B90'
width = 17 #13
height = 17 #13
mid = 5 #4
st = (w - width) / 2, (h - height) / 2

rdraw.polygon([st[0],st[1],st[0]+mid,st[1]+(width-1)/2,
               st[0],st[1]+(width-1)],fill=light)
rdraw.polygon([st,st[0]+(height-1),st[1]+(width-1)/2,
               st[0]+mid,st[1]+(width-1)/2],fill=med)
rdraw.polygon([st[0],st[1]+(width-1),st[0]+(height-1),st[1]+(width-1)/2,
               st[0]+mid,st[1]+(width-1)/2], fill=border)

img.save('../images/lime/arrowright-n.png')

aimg = img.point(lambda p: int(p * 1.1))
aimg.save('../images/lime/arrowright-a.png')

dimg = img.convert('L')
dimg = dimg.convert('RGBA')
transx(dimg,w,h)
dimg.save('../images/lime/arrowright-d.png')

img.transpose(Image.ROTATE_90).save('../images/lime/arrowup-n.png')
#uimg = img.rotate(90)
uimg = Image.open('../images/lime/arrowup-n.png')

auimg = uimg.point(lambda p: int(p * 1.1))
auimg.save('../images/lime/arrowup-a.png')

duimg = uimg.convert('L')
duimg = duimg.convert('RGBA')
transx(duimg,w,h)
duimg.save('../images/lime/arrowup-d.png')

pdraw.polygon([st[0],st[1],st[0]+mid,st[1]+(width-1)/2,
               st[0],st[1]+(width-1)],fill=border)
pdraw.polygon([st,st[0]+(height-1),st[1]+(width-1)/2,
               st[0]+mid,st[1]+(width-1)/2],fill=med)
pdraw.polygon([st[0],st[1]+(width-1),st[0]+(height-1),st[1]+(width-1)/2,
               st[0]+mid,st[1]+(width-1)/2], fill=light)

pimg.save('../images/lime/arrowright-p.png')

#puimg = pimg.rotate(90)
pimg.transpose(Image.ROTATE_90).save('../images/lime/arrowup-p.png')
#puimg.save('../images/lime/arrowup-p.png')

img.transpose(Image.FLIP_LEFT_RIGHT).save('../images/lime/arrowleft-n.png')

pimg.transpose(Image.FLIP_LEFT_RIGHT).save('../images/lime/arrowleft-p.png')

limg = Image.open('../images/lime/arrowleft-n.png')

alimg = limg.point(lambda p: int(p * 1.1))
alimg.save('../images/lime/arrowleft-a.png')

dlimg = limg.convert('L')
dlimg = dlimg.convert('RGBA')
transx(dlimg,w,h)
dlimg.save('../images/lime/arrowleft-d.png')

#ndimg = img.rotate(270)
img.transpose(Image.ROTATE_270).save('../images/lime/arrowdown-n.png')
ndimg = Image.open('../images/lime/arrowdown-n.png')

adimg = ndimg.point(lambda p: int(p * 1.1))
adimg.save('../images/lime/arrowdown-a.png')

ddimg = ndimg.convert('L')
ddimg = ddimg.convert('RGBA')
transx(ddimg,w,h)
ddimg.save('../images/lime/arrowdown-d.png')

plimg = Image.open('../images/lime/arrowleft-p.png')
plimg.transpose(Image.ROTATE_90).save('../images/lime/arrowdown-p.png')
#drimg = plimg.rotate(90)
#drimg.save('../images/lime/arrowdown-p.png')
