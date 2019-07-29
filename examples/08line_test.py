from PIL import Image, ImageDraw

w = 23  # used to set width
h = 23  # used to set height
transparent = (255,255,255,0)
# used to set background colour - using an RGBA format

img = Image.new('RGBA', (w,h), transparent)
# create a new image organized with RGBA pixels,
# of a given size with the set background colour,
# in this instance transparent
idraw = ImageDraw.Draw(img)
# create function for drawing within the new image img.

idraw.line([0,0,w-1,0],fill='black',width=1)
# draw line on upper part of the image
idraw.line([0,0,0,h-1],fill='black',width=1)
# draw line on left part of the image
idraw.line([w-1,0,w-1,h-1],fill='black',width=1)
# draw line on left part of the image
idraw.line([0,h-1,w-1,h-1],fill='black',width=1)
# draw line on lower part of the image

idraw.ellipse([0,0,w-1,h-1],outline='red')

img.save('line_test.png') # save to file