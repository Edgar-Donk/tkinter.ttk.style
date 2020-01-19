'''
create up and down arrows

lime spinbox arrs - used as background for arrows

'''

from PIL import Image, ImageDraw

light = 'GreenYellow'
med = 'LawnGreen'
border = '#5D9B90'
dark = '#878787'
pale = '#CECECE'

img = Image.open('../images/lime/arrspd-n.png')
width, height = img.size
draw = ImageDraw.Draw(img)
print(width,height)
mid = width//2

p1 = [2,1,width-3,1,mid,height-3,4,4]
p2 = [2,1,9,1,6,9,3,2]

# when setting up arrow use outline,
# adjust last point so that both slopes are mirror images
draw.polygon(p1, fill=border) # outline=border)
draw.polygon(p2, fill = light) # outline=light)

img.save('../images/lime/arrspd-n.png')
img.transpose(Image.FLIP_TOP_BOTTOM).save('../images/lime/arrspu-n.png')

pimg = Image.open('../images/lime/arrspd-p.png')
draw = ImageDraw.Draw(pimg)

draw.polygon(p1, fill=border) # outline=border)
draw.polygon(p2, fill = light) # outline=light)

pimg.save('../images/lime/arrspd-p.png')
pimg.transpose(Image.FLIP_TOP_BOTTOM).save('../images/lime/arrspu-p.png')

himg = Image.open('../images/lime/arrspd-h.png')
draw = ImageDraw.Draw(himg)

draw.polygon(p1, fill=border) # outline=border)
draw.polygon(p2, fill = light) # outline=light)

himg.save('../images/lime/arrspd-h.png')
himg.transpose(Image.FLIP_TOP_BOTTOM).save('../images/lime/arrspu-h.png')

dimg = Image.open('../images/lime/arrspd-d.png')
draw = ImageDraw.Draw(dimg)

draw.polygon(p1, fill=border) # outline=border)
draw.polygon(p2, fill = light) # outline=light)

dimg.save('../images/lime/arrspd-d.png')
dimg.transpose(Image.FLIP_TOP_BOTTOM).save('../images/lime/arrspu-d.png')



